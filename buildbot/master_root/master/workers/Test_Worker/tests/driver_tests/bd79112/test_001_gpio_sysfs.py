import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from addac_class import addac
from gpio_helpers import gpio_sysfs_check_value
import bd79112
bd79112 = addac(bd79112)

def test_001_gpio_sysfs(command):
    in0 = bd79112.board.data["gpio"]["in0"]
    in1 = bd79112.board.data["gpio"]["in1"]

    result = gpio_sysfs_check_value(bd79112, command,
                                    in0["label"], in0["index"],
                                    in1["label"], in1["index"], 0)
    check_result(result)

    result = gpio_sysfs_check_value(bd79112, command,
                                    in0["label"], in0["index"],
                                    in1["label"], in1["index"], 1)
    check_result(result)
