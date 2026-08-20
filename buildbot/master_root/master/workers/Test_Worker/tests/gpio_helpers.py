
def _gpio_sysfs_export(command, label: str, index: int) -> int | None:
    """
    Attemps to export the GPIO chip based on the given label (e.g. bd79112)
    and the given GPIO pin index.

    Returns the number of the GPIO if successful, None otherwise.
    """

    stdout, _, ret = command.run(f"grep -rls {label} /sys/class/gpio/gpiochip* | sed \"s/[^0-9]//g\"")
    if ret != 0:
        return None

    num = int(stdout[0]) + index
    print(f"gpio: using GPIO '{num}' for export")

    stdout, stderr, ret = command.run(f"echo {num} > /sys/class/gpio/export")
    if ret != 0:
        print(f"gpio: failed to export GPIO '{num}': {stdout, stderr}")
        return None

    return num

def _gpio_sysfs_unexport(command, num: int):
    stdout, stderr, ret = command.run(f"echo {num} > /sys/class/gpio/unexport")
    if ret != 0:
        print(f"gpio: failed to unexport GPIO '{num}': {stdout, stderr}")

def _gpio_sysfs_set_attr(command, num: int, attr: str, val: str) -> bool:
    """
    Attemps to set the given GPIO attribute to the given value using the GPIO
    number.

    Returns True if successful, False otherwise.
    """

    stdout, stderr, ret = command.run(f"echo {val} > /sys/class/gpio/gpio{num}/{attr}")
    if ret != 0:
        print(f"gpio: failed to set '{attr}' to '{val} for GPIO '{num}': {stdout, stderr}")
        return False

    print(f"gpio: set '{val}' to '{attr}'")

    return True

def _gpio_sysfs_get_attr(command, num: int, attr: str) -> str | None:
    """
    Attemps to get the given GPIO attribute using the GPIO number.

    Returns the value if successful, None otherwise.
    """

    stdout, stderr, ret = command.run(f"cat /sys/class/gpio/gpio{num}/value")
    if ret != 0:
        print(f"gpio: failed to get '{attr}' from GPIO '{num}': {stdout, stderr}")
        return None

    print(f"gpio: got '{stdout[0]}' from '{attr}'")

    return stdout[0]

def gpio_sysfs_check_value(self, command, a_label: str, a_index: int,
                           b_label: str, b_index: int, expect: int):
    """
    Attempts to set GPIO A to the expected value, and tests whether that value
    was read back from GPIO B.
    """

    self.result["stage"] = "gpio_sysfs_check_value"
    self.result["expect"] = expect
    self.result["return"] = None

    a_num = _gpio_sysfs_export(command, a_label, a_index)
    b_num = _gpio_sysfs_export(command, b_label, b_index)
    if (a_num != None and b_num != None and
        _gpio_sysfs_set_attr(command, a_num, "direction", "out") and
        _gpio_sysfs_set_attr(command, b_num, "direction", "in") and
        _gpio_sysfs_set_attr(command, a_num, "value", str(expect)) and
        (val := _gpio_sysfs_get_attr(command, b_num, "value")) != None):
            self.result["return"] = int(val)

    if a_num:
        _gpio_sysfs_unexport(command, a_num)
    if b_num:
        _gpio_sysfs_unexport(command, b_num)

    return self.result
