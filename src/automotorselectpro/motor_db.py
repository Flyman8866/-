from .constants import DATA_SOURCE_NOTICE


def demo_motors() -> dict:
    return {
        "notice": DATA_SOURCE_NOTICE,
        "motors": [
            {"model": "MSP-100", "peak_torque_nm": 1.2, "cont_torque_nm": 0.5, "max_speed_rpm": 3000, "inertia": 0.00015, "brake": False},
            {"model": "MSP-200B", "peak_torque_nm": 2.6, "cont_torque_nm": 1.1, "max_speed_rpm": 3000, "inertia": 0.0003, "brake": True},
            {"model": "MSP-400B", "peak_torque_nm": 4.5, "cont_torque_nm": 2.0, "max_speed_rpm": 5000, "inertia": 0.0007, "brake": True},
        ],
    }
