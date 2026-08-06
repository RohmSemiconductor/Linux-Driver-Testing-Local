import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import bm1390
bm1390 = sensor(bm1390)

def test_000_sanitycheck(command):
    result = bm1390.config_validate_default("bm1390")
    check_result(result)

    result = bm1390.config_validate_i2c()
    check_result(result)
