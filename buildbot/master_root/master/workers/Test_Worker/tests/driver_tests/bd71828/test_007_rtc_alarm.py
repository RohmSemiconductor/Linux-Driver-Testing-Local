import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd71828
from test_util import check_result
from rtc_class import rtc
bd71828 = rtc(bd71828)

def test_007_rtc_alarm(command):
    name = bd71828.board.data["rtc"]["component_rtc"]

    result = bd71828.rtc_set_and_test_alarm(command, name)
    check_result(result)
