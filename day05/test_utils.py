import pytest

from utils import (
    validate_percentage,
    calculate_cpu_alert,
    calculate_memory_alert,
    calculate_disk_alert,
    get_health_status,
)


@pytest.mark.parametrize(
    "cpu_usage, expected",
    [
        (0, "OK"),
        (10, "OK"),
        (50, "OK"),
        (79, "OK"),
        (80, "ALERT"),
        (90, "ALERT"),
        (100, "ALERT"),
    ],
)
def test_cpu_alert(cpu_usage, expected):
    assert calculate_cpu_alert(cpu_usage) == expected


@pytest.mark.parametrize(
    "memory_usage, expected",
    [
        (20, "OK"),
        (79, "OK"),
        (80, "ALERT"),
        (95, "ALERT"),
    ],
)
def test_memory_alert(memory_usage, expected):
    assert calculate_memory_alert(memory_usage) == expected


@pytest.mark.parametrize(
    "disk_usage, expected",
    [
        (40, "OK"),
        (79, "OK"),
        (80, "ALERT"),
        (99, "ALERT"),
    ],
)
def test_disk_alert(disk_usage, expected):
    assert calculate_disk_alert(disk_usage) == expected


def test_health_status():
    result = get_health_status(
        cpu_usage=90,
        memory_usage=50,
        disk_usage=85,
    )

    assert result["cpu"] == "ALERT"
    assert result["memory"] == "OK"
    assert result["disk"] == "ALERT"


def test_custom_threshold():
    result = get_health_status(
        cpu_usage=71,
        memory_usage=69,
        disk_usage=75,
        threshold=70,
    )

    assert result["cpu"] == "ALERT"
    assert result["memory"] == "OK"
    assert result["disk"] == "ALERT"


@pytest.mark.parametrize(
    "value",
    [
        -1,
        -10,
        101,
        150,
    ],
)
def test_invalid_percentage(value):
    with pytest.raises(ValueError):
        validate_percentage(value)


def test_invalid_cpu_percentage():
    with pytest.raises(ValueError):
        calculate_cpu_alert(150)


def test_invalid_memory_percentage():
    with pytest.raises(ValueError):
        calculate_memory_alert(-20)


def test_invalid_disk_percentage():
    with pytest.raises(ValueError):
        calculate_disk_alert(110)