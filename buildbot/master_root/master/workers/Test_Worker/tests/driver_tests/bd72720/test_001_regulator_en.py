import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
import bd72720
from test_util import check_result
from pmic_class import pmic
bd72720 = pmic(bd72720)

def test_001_regulator_en(command):
    regulators = bd72720.board.data["regulators"]
    for regulator in regulators.keys():
        if not "dts_only" in regulators[regulator].keys():
            # skip = ["buck4"]
            # if regulator in skip:
            #     continue

            # if "idle_on" in bd72720.board.data["regulators"][regulator]["settings"].keys():
            #     idle_mode_status = bd72720.disable_idle_mode(regulator, command)
            #     assert idle_mode_status == 0

            if bd72720.check_regulator_enable_mode(regulator, command):
                result = bd72720.regulator_enable(regulator, command)
                check_result(result)

            if bd72720.check_regulator_enable_mode(regulator, command) and not bd72720.check_regulator_always_on_mode(regulator, command):
                result = bd72720.regulator_disable(regulator, command)
                check_result(result)
