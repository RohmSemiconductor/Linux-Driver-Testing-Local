import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd9573
from test_util import check_result
from pmic_class import pmic
bd9573 = pmic(bd9573)

def test_ovd_uvd_disable(command, dts):
    for regulator in bd9573.board.data['regulators'].keys():
        for setting in bd9573.board.data['regulators'][regulator]['settings'].keys():
            if setting != 'voltage':
                result = bd9573.read_dt_setting(regulator, setting, dts, command)
                result['return'] = [dts, setting, bd9573.i2c_to_lim_uv(regulator, setting, command)]
                check_result(result)
