from .axes import AxisRequirement


def hard_filter_motors(req: AxisRequirement, motors: list[dict], inertia_ratio_limit: float = 10.0) -> list[dict]:
    out = []
    for m in motors:
        reasons = []
        if m["peak_torque_nm"] < req.peak_torque_nm:
            reasons.append("peak_torque_insufficient")
        if m["cont_torque_nm"] < req.rms_torque_nm:
            reasons.append("rms_torque_insufficient")
        if m["max_speed_rpm"] < req.max_speed_rpm:
            reasons.append("max_speed_insufficient")
        ratio = req.load_inertia / max(m["inertia"], 1e-12)
        if ratio > inertia_ratio_limit:
            reasons.append("inertia_ratio_too_large")
        if req.vertical_needs_brake and not m.get("brake", False):
            reasons.append("brake_required")
        if reasons:
            m2 = dict(m)
            m2["status"] = "rejected"
            m2["reasons"] = reasons
            out.append(m2)
        else:
            m2 = dict(m)
            m2["status"] = "accepted"
            m2["inertia_ratio"] = ratio
            out.append(m2)
    return out
