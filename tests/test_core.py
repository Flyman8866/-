from src.automotorselectpro.units import mm_to_m, m_to_mm, rpm_to_rad_s, rad_s_to_rpm
from src.automotorselectpro.motion import triangular_profile, trapezoidal_profile, rms_torque
from src.automotorselectpro.axes import calc_ball_screw_axis, calc_conveyor_axis, calc_turntable_axis
from src.automotorselectpro.motor_db import demo_motors
from src.automotorselectpro.filtering import hard_filter_motors
from main import smoke_test


def test_mm_to_m(): assert mm_to_m(1000) == 1

def test_m_to_mm(): assert m_to_mm(1.5) == 1500

def test_rpm_rad_roundtrip(): assert abs(rad_s_to_rpm(rpm_to_rad_s(3000)) - 3000) < 1e-9

def test_triangular(): assert triangular_profile(1, 2)["vmax"] > 0

def test_trapezoidal(): assert trapezoidal_profile(2, 1, 4)["acc"] > 0

def test_rms(): assert abs(rms_torque([3,4]) - (12.5 ** 0.5)) < 1e-9

def test_rms_empty(): assert rms_torque([]) == 0

def test_ball_screw(): assert calc_ball_screw_axis(1000, 10, 0.9, 2000, 0.001).peak_torque_nm > 0

def test_conveyor(): assert calc_conveyor_axis(100, 0.1, 1200, 0.002).rms_torque_nm > 0

def test_turntable(): assert calc_turntable_axis(50, 0.2, 500, 0.003).peak_torque_nm > 0

def test_db_notice(): assert demo_motors()["notice"] == "DEMO_ONLY_NOT_FOR_ENGINEERING_USE"

def test_db_has_motors(): assert len(demo_motors()["motors"]) >= 3

def test_filter_peak_reject():
    req = calc_ball_screw_axis(5000, 20, 0.8, 4000, 0.001)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any("peak_torque_insufficient" in x.get("reasons", []) for x in out)

def test_filter_rms_reject():
    req = calc_ball_screw_axis(3500, 20, 0.8, 2000, 0.001)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any("rms_torque_insufficient" in x.get("reasons", []) for x in out)

def test_filter_speed_reject():
    req = calc_ball_screw_axis(500, 10, 0.9, 6000, 0.001)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any("max_speed_insufficient" in x.get("reasons", []) for x in out)

def test_filter_inertia_ratio_reject():
    req = calc_ball_screw_axis(500, 10, 0.9, 1000, 0.1)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any("inertia_ratio_too_large" in x.get("reasons", []) for x in out)

def test_filter_brake_reject_vertical():
    req = calc_ball_screw_axis(600, 10, 0.9, 2000, 0.0005, vertical=True)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any("brake_required" in x.get("reasons", []) for x in out)

def test_filter_has_accept():
    req = calc_ball_screw_axis(1000, 10, 0.9, 2500, 0.001, vertical=True)
    out = hard_filter_motors(req, demo_motors()["motors"])
    assert any(x["status"] == "accepted" for x in out)

def test_smoke_test(): smoke_test()
