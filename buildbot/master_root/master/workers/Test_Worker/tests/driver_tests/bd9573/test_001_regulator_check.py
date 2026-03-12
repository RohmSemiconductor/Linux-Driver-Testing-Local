import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd9573
from test_util import check_result
from pmic_class import pmic
bd9573 = pmic(bd9573)

def test_regulator_check(command):
    vout1_en_low=bd9573.check_bd9576_vout1_en_low(command)

    for regulator in bd9573.board.data['regulators'].keys():
        regulator_is_on = bd9573.regulator_is_on(regulator,command)
        check_result(regulator_is_on)

        if regulator == 'VD50' and vout1_en_low == 1:
            result = bd9573.regulator_is_on_driver(regulator,command)
            result['expect'] = 0
            check_result(result)

        elif regulator_is_on['return'] == 1:
            result = bd9573.regulator_is_on_driver(regulator,command)
            result['expect'] = 1
            check_result(result)
