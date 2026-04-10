import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from pmic_class import pmic
import bd72720
bd72720 = pmic(bd72720)

def test_000_sanitycheck(command):
    result = bd72720.validate_config("bd72720")
    check_result(result)

    for regulator in bd72720.board.data["regulators"].keys():
        result = bd72720.sanity_check(regulator,command)
        check_result(result)

        result = bd72720.sanity_check_sysfs_en(regulator, command)
        check_result(result)

        result = bd72720.sanity_check_sysfs_set(regulator, command)
        check_result(result)
