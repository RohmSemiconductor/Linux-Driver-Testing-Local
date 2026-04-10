import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from pmic_class import pmic
import bd72720
bd72720 = pmic(bd72720)

def test_002_voltage_run(command):
    regulators = bd72720.board.data["regulators"]
    for regulator in regulators.keys():
        if not "dts_only" in regulators.keys():
            if regulator == "buck10":
                continue

            regulator_is_on = bd72720.regulator_is_on(regulator,command)
            check_result(regulator_is_on)

            settings = bd72720.board.data["regulators"][regulator]["settings"]

            if "voltage" in settings.keys():
                if "volt_change_not_allowed_while_on" in regulators[regulator]: # and regulator_is_on["return"]:
                    print(f"Cannot change regulator '{regulator}' voltage - voltage run skipped")
                elif "range" not in settings["voltage"].keys():
                    print("Not a regulator")
                else:
                    result = bd72720.regulator_voltage_run(regulator, command)
                    check_result(result)
