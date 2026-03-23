import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd71828
from test_util import check_result
from pmic_class import pmic
bd71828 = pmic(bd71828)

GPIO_DVS0 = 0
GPIO_EPDEN = 1
GPIO_DVS1 = 2
HALL = 3

# This test uses BBB's pin P9_12 to set the value of the HALL pin on the test
# board. In the BeagleBone reference manual, P9_12 is labeled as GPIO1_28,
# but it is actually GPIO0_28 for some reason.

def test_006_gpio_sysfs(command):
    result = bd71828.gpio_get_value_via_sysfs(command, "gpio-0-31", 28, "bd71828-gpio", HALL, 0)
    check_result(result)

    result = bd71828.gpio_get_value_via_sysfs(command, "gpio-0-31", 28, "bd71828-gpio", HALL, 1)
    check_result(result)
