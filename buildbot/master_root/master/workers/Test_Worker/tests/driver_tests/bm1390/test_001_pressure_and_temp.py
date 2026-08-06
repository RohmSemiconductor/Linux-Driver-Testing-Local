import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import bm1390
bm1390 = sensor(bm1390)

def test_001_pressure_and_temp(command):
    result = bm1390.try_read_attribute_range(command, "bm1390",
                                             "in_pressure_raw",
                                             2000000, 2100000)
    check_result(result)

    result = bm1390.try_read_attribute_range(command, "bm1390",
                                             "in_temp_raw",
                                             700, 900)
    check_result(result)
