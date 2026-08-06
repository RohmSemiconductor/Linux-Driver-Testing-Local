
def _iio_sysfs_device_abspath(command, dev: str) -> str | None:
    stdout, _, ret = command.run(f"grep -rls {dev} /sys/bus/iio/devices/*/name | xargs dirname")
    return stdout[0] if ret == 0 else None

def iio_sysfs_read_attribute(command, dev: str, attr: str) -> float | None:
    stdout = ""
    stderr = ""

    path = _iio_sysfs_device_abspath(command, dev)
    if path:
        stdout, stderr, ret = command.run(f"cat {path}/{attr}")
        if ret == 0:
            print(f"iio: read value '{stdout[0]}' from attribute '{attr}'")
            return float(stdout[0])

    print(f"iio: failed to read attribute '{attr}': {stdout, stderr}")
    return None

def iio_sysfs_write_attribute(command, dev: str, attr: str, value: float) -> bool:
    stdout = ""
    stderr = ""

    path = _iio_sysfs_device_abspath(command, dev)
    if path:
        stdout, stderr, ret = command.run(f"echo {value} > {path}/{attr}")
        if ret == 0:
            print(f"iio: write value '{value}' to attribute '{attr}'")
            return True

    print(f"iio: failed to write value '{value}' to attribute '{attr}': {stdout, stderr}")
    return False
