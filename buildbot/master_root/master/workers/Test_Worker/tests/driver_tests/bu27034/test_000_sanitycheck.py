import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import bu27034
bu27034 = sensor(bu27034)

def test_000_sanitycheck(command):
    result = bu27034.config_validate_default("bu27034")
    check_result(result)

    result = bu27034.config_validate_i2c()
    check_result(result)
