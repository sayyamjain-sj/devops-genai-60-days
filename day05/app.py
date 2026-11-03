from utils import get_health_status


def main():
    health = get_health_status(
        cpu_usage=85,
        memory_usage=65,
        disk_usage=90,
    )

    print("SYSTEM HEALTH")
    print("=" * 30)

    for resource, status in health.items():
        print(f"{resource.upper()}: {status}")


if __name__ == "__main__":
    main()