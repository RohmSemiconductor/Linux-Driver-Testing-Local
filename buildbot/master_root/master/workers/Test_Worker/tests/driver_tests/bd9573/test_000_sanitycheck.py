import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd9573
from test_util import check_result
from pmic_class import pmic
bd9573 = pmic(bd9573)

def test_sanitycheck(command):
    result = bd9573.validate_config('bd9573')
    check_result(result)

    for regulator in bd9573.board.data['regulators'].keys():
        result = bd9573.sanity_check(regulator,command)
        check_result(result)

        result = bd9573.sanity_check_sysfs_en(regulator, command)
        check_result(result)

        result = bd9573.sanity_check_sysfs_set(regulator, command)
        check_result(result)
