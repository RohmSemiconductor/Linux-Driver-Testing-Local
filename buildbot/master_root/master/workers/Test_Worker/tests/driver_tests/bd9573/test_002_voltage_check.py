import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd9573
from test_util import check_result
from pmic_class import pmic
bd9573 = pmic(bd9573)

def test_voltage_run(command):
    for regulator in bd9573.board.data['regulators'].keys():
        if regulator == 'VOUTS1':
            result = bd9573.regulator_voltage_driver_get(regulator,command)
            result['expect'] = bd9573.mv_to_uv(3300)
            check_result(result)
        else:
            result = bd9573.regulator_voltage_driver_get(regulator,command)
            result['expect'] = bd9573.i2c_to_uv(regulator,command)
            check_result(result)
