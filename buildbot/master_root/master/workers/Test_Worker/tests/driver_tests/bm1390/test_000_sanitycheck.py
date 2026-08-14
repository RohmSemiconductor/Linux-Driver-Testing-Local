import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import config_helpers
import bm1390
bm1390 = sensor(bm1390)

def test_000_sanitycheck(command):
    result = config_helpers.config_validate_default(bm1390, "bm1390")
    check_result(result)

    result = config_helpers.config_validate_i2c(bm1390)
    check_result(result)
