import math

def triangular_profile(distance_m: float, time_s: float) -> dict:
    a = 4 * distance_m / (time_s ** 2)
    vmax = a * time_s / 2
    return {"acc": a, "vmax": vmax}

def trapezoidal_profile(distance_m: float, accel_s: float, total_s: float) -> dict:
    if total_s <= accel_s:
        return triangular_profile(distance_m, total_s)
    vmax = distance_m / (total_s - accel_s)
    acc = vmax / accel_s
    return {"acc": acc, "vmax": vmax}

def rms_torque(samples: list[float]) -> float:
    if not samples:
        return 0.0
    return math.sqrt(sum(x * x for x in samples) / len(samples))
