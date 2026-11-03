def validate_percentage(value: float) -> float:
    """
    Validate that a percentage is between 0 and 100.
    """

    if value < 0 or value > 100:
        raise ValueError("Percentage must be between 0 and 100")

    return value


def calculate_cpu_alert(
    cpu_usage: float,
    threshold: float = 80,
) -> str:
    """
    Return ALERT when CPU usage reaches or exceeds threshold.
    """

    validate_percentage(cpu_usage)
    validate_percentage(threshold)

    if cpu_usage >= threshold:
        return "ALERT"

    return "OK"


def calculate_memory_alert(
    memory_usage: float,
    threshold: float = 80,
) -> str:
    """
    Return ALERT when memory usage reaches or exceeds threshold.
    """

    validate_percentage(memory_usage)
    validate_percentage(threshold)

    if memory_usage >= threshold:
        return "ALERT"

    return "OK"


def calculate_disk_alert(
    disk_usage: float,
    threshold: float = 80,
) -> str:
    """
    Return ALERT when disk usage reaches or exceeds threshold.
    """

    validate_percentage(disk_usage)
    validate_percentage(threshold)

    if disk_usage >= threshold:
        return "ALERT"

    return "OK"


def get_health_status(
    cpu_usage: float,
    memory_usage: float,
    disk_usage: float,
    threshold: float = 80,
) -> dict:
    """
    Return the health state of CPU, memory, and disk.
    """

    return {
        "cpu": calculate_cpu_alert(cpu_usage, threshold),
        "memory": calculate_memory_alert(memory_usage, threshold),
        "disk": calculate_disk_alert(disk_usage, threshold),
    }