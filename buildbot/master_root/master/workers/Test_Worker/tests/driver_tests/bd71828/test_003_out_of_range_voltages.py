import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
import bd71828
from test_util import check_result
from pmic_class import pmic
bd71828 = pmic(bd71828)

def test_003_out_of_range_voltages(command):
    regulators = bd71828.board.data["regulators"]
    for regulator in regulators.keys():
        if not "dts_only" in regulators[regulator].keys():
            if "voltage" in regulators[regulator]["settings"].keys():
                regulator_is_on = bd71828.regulator_is_on(regulator, command)
                check_result(regulator_is_on)

                if "volt_change_not_allowed_while_on" in regulators[regulator]: # and regulator_is_on["return"]:
                    print(f"Cannot change regulator "{regulator}" voltage - out of range tests skipped")
                else:
                    result, min, max = bd71828.get_min_max_volt(regulator)

                    bd71828.regulator_voltage_driver_set(regulator, min, command)
                    result["expect"] = ["min", bd71828.i2c_to_uv(regulator, command)]

                    bd71828.regulator_voltage_driver_set(regulator, min - 10000, command)
                    result["return"] = ["min", bd71828.i2c_to_uv(regulator, command)]

                    check_result(result)

                    bd71828.regulator_voltage_driver_set(regulator, max, command)
                    result["expect"] = ["max", bd71828.i2c_to_uv(regulator, command)]

                    bd71828.regulator_voltage_driver_set(regulator, max + 10000, command)
                    result["return"] = ["max", bd71828.i2c_to_uv(regulator, command)]

                    check_result(result)
