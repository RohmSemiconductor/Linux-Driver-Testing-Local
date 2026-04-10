import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from rtc_class import rtc
import bd72720
bd72720 = rtc(bd72720)

def test_004_rtc_test(command):
    rtc = bd72720.board.data["rtc"]
    bd72720.result["result_dir"] = "PMIC"

    # Set Component RTC to known date, and check that it was set succesfully
    result = bd72720.reset_and_check_date(command, rtc["component_rtc"], rtc["rtc_reset"])
    check_result(result)

    # Set BBB RTC to test server time
    result = bd72720.set_rtc_from_srv_time(command, rtc["sys_rtc"])
    check_result(result)

    # Set BBB system clock to BBB RTC
    result = bd72720.set_bbb_sys_from_rtc(command, rtc["sys_rtc"])
    check_result(result)

    # Set Component RTC to BBB system clock
    result = bd72720.set_rtc_from_bbb_sys_time(command, rtc["component_rtc"])
    check_result(result)
