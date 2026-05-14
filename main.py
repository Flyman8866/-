import argparse
from src.automotorselectpro.axes import calc_ball_screw_axis
from src.automotorselectpro.filtering import hard_filter_motors
from src.automotorselectpro.motor_db import demo_motors


def smoke_test() -> None:
    req = calc_ball_screw_axis(force_n=1800, lead_mm=10, eff=0.9, speed_rpm=2500, inertia=0.0012, vertical=True)
    db = demo_motors()
    res = hard_filter_motors(req, db["motors"])
    assert db["notice"] == "DEMO_ONLY_NOT_FOR_ENGINEERING_USE"
    assert any(x["status"] == "accepted" for x in res)
    assert any("brake_required" in x.get("reasons", []) for x in res)
    print("Smoke test passed")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--smoke-test", action="store_true")
    args = p.parse_args()
    if args.smoke_test:
        smoke_test()
    else:
        from src.automotorselectpro.gui import run_gui
        raise SystemExit(run_gui())
