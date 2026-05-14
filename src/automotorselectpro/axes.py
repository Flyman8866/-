from dataclasses import dataclass

@dataclass
class AxisRequirement:
    axis_type: str
    peak_torque_nm: float
    rms_torque_nm: float
    max_speed_rpm: float
    load_inertia: float
    vertical_needs_brake: bool = False


def calc_ball_screw_axis(force_n: float, lead_mm: float, eff: float, speed_rpm: float, inertia: float, vertical=False) -> AxisRequirement:
    peak = (force_n * (lead_mm / 1000.0)) / (2 * 3.1415926 * eff)
    return AxisRequirement("ball_screw", peak, peak * 0.55, speed_rpm, inertia, vertical)


def calc_conveyor_axis(mass_kg: float, radius_m: float, speed_rpm: float, inertia: float) -> AxisRequirement:
    peak = mass_kg * 9.81 * radius_m * 0.12
    return AxisRequirement("conveyor", peak, peak * 0.6, speed_rpm, inertia, False)


def calc_turntable_axis(payload_kg: float, radius_m: float, speed_rpm: float, inertia: float) -> AxisRequirement:
    peak = payload_kg * radius_m * 0.9
    return AxisRequirement("turntable", peak, peak * 0.5, speed_rpm, inertia, False)
