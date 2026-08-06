import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import bu27034
bu27034 = sensor(bu27034)

def test_002_integration_time(command):
    result = bu27034.try_write_attribute_gts(command, "bu27034", 0.2,
                                             "integration_time",
                                             "in_intensity1_hardwaregain",
                                             "in_intensity1_scale")
    check_result(result)

    result = bu27034.try_write_attribute_gts(command, "bu27034", 0.2,
                                             "integration_time",
                                             "in_intensity2_hardwaregain",
                                             "in_intensity2_scale")
    check_result(result)
