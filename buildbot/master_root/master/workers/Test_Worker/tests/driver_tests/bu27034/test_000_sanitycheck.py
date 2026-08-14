import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import config_helpers
import bu27034
bu27034 = sensor(bu27034)

def test_000_sanitycheck(command):
    result = config_helpers.config_validate_default(bu27034, "bu27034")
    check_result(result)

    result = config_helpers.config_validate_i2c(bu27034, )
    check_result(result)
