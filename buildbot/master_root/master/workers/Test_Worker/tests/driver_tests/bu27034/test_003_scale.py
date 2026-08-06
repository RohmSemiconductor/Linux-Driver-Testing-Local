import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from sensor_class import sensor
import bu27034
bu27034 = sensor(bu27034)

def test_003_scale(command):
    result = bu27034.try_write_attribute_gts(command, "bu27034", 0.25,
                                             "in_intensity1_scale",
                                             "integration_time",
                                             "in_intensity1_hardwaregain")
    check_result(result)

    result = bu27034.try_write_attribute_scale(command, "bu27034", 0.25,
                                               "in_intensity1_scale",
                                               "integration_time",
                                               "in_intensity2_hardwaregain",
                                               "in_intensity2_scale")
    check_result(result)

    result = bu27034.try_write_attribute_gts(command, "bu27034", 0.25,
                                             "in_intensity2_scale",
                                             "integration_time",
                                             "in_intensity2_hardwaregain")
    check_result(result)

    result = bu27034.try_write_attribute_scale(command, "bu27034", 0.25,
                                               "in_intensity2_scale",
                                               "integration_time",
                                               "in_intensity1_hardwaregain",
                                               "in_intensity1_scale")
    check_result(result)
