import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd9573
from test_util import check_result
from pmic_class import pmic
bd9573 = pmic(bd9573)

def test_out_of_range_voltages(command):
    for regulator in bd9573.board.data['regulators'].keys():
        regulator_is_on=bd9573.regulator_is_on(regulator,command)
        check_result(regulator_is_on)

        if ("volt_change_not_allowed_while_on" in bd9573.board.data['regulators'][regulator] and regulator_is_on['return'] == 1):
            print("Cannot change regulator: "+regulator+" voltage - out of range tests skipped")

        elif 'volt_reg_bitmask' in bd9573.board.data['regulators'][regulator]['settings']['voltage']:
            result, min, max = bd9573.get_min_max_volt(regulator)

            bd9573.regulator_voltage_driver_set(regulator,min,command)
            result['expect']= ['min', bd9573.i2c_to_uv(regulator,command)]

            bd9573.regulator_voltage_driver_set(regulator,min-10000,command)
            result['return']= ['min', bd9573.i2c_to_uv(regulator,command)]

            check_result(result)

            bd9573.regulator_voltage_driver_set(regulator,max,command)
            result['expect']= ['max', bd9573.i2c_to_uv(regulator,command)]
            bd9573.regulator_voltage_driver_set(regulator,max+10000,command)
            result['return']= ['max', bd9573.i2c_to_uv(regulator,command)]

            check_result(result)
