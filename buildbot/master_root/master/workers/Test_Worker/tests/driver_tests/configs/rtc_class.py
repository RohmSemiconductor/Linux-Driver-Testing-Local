from dataclasses import dataclass, field
import pytest
from time import sleep
import sys
import os
import copy
import math
import numbers
sys.path.append(os.path.abspath("."))

from test_class_helpers import get_srv_time, get_srv_epoch, find_rtc_files, set_rtc_time, get_rtc_date, get_rtc_epoch, split_datetime, get_beagle_epoch, set_beagle_time_from_rtc, set_rtc_time_from_bbb_sys
@dataclass
class rtc:
    board: dict
    result: dict = field(default_factory=lambda: {
    'type':         None,
    'result_dir':   None,
    'stage':        None,
    'product':      None,
    'return':       [],
    'expect':       [],
    })

    info: dict = field(default_factory=lambda: {
        'srv_time':     None,
    })

    ### RTC functions
    def set_rtc_from_bbb_sys_time(self, command, rtc_name):
        self.result['rtc'] = rtc_name
        self.result['stage'] = 'set_rtc_from_bbb_sys_time'
        path, dev_file, returncode = find_rtc_files(command, rtc_name)
        if returncode == 0:
            self.result['expect_low'] = get_beagle_epoch(command)

            returncode = set_rtc_time_from_bbb_sys(command, dev_file)
            self.result['return'] = get_rtc_epoch(command, rtc_name)

            self.result['expect_high'] = get_beagle_epoch(command)
        else:
            self.result['return'] = "RTC files not found"
            self.result['rc'] = -1

        self.result['dev_file'] = dev_file
        self.result['sysfs_path'] = path

        return self.result

    def set_bbb_sys_from_rtc(self, command, rtc_name):
        self.result['rtc'] = rtc_name
        self.result['stage'] = 'set_bbb_from_rtc_time'

        path, dev_file, returncode = find_rtc_files(command, rtc_name)

        if returncode == 0:
            self.result['expect_low'] = get_rtc_epoch(command, rtc_name)

            returncode = set_beagle_time_from_rtc(command, dev_file)
            self.result['return'] = get_beagle_epoch(command)

            self.result['expect_high'] = get_rtc_epoch(command, rtc_name)
        else:
            self.result['return'] = "RTC files not found"
            self.result['rc'] = -1

        self.result['dev_file'] = dev_file
        self.result['sysfs_path'] = path

        return self.result

    def set_rtc_from_srv_time(self, command, rtc_name):
        self.result['rtc'] = rtc_name
        self.result['stage'] = 'set_rtc_from_srv_time'
        self.result['expect'] = 'range'

        path, dev_file, returncode = find_rtc_files(command, rtc_name)

        self.result['expect_low'] = get_srv_epoch()
        self.info['srv_time'] = get_srv_time()

        if returncode == 0:
            stdout, stderr, returncode = set_rtc_time(command, dev_file, self.info['srv_time'])
            self.result['return'] = int(get_rtc_epoch(command, rtc_name))
            self.result['expect_high'] = get_srv_epoch()

        else:
            self.result['return'] = "RTC files not found"
            self.result['rc'] = -1

        self.result['dev_file'] = dev_file
        self.result['sysfs_path'] = path

        return self.result

    def reset_and_check_date(self, command, rtc_name, datetime):
        self.result['rtc'] = rtc_name
        self.result['stage'] = 'reset_and_check_date'
        self.result['rc'] = 0

        path, dev_file, returncode = find_rtc_files(command, rtc_name)
        date, time = split_datetime(datetime)

        if returncode == 0:
            stdout, stderr, returncode = set_rtc_time(command, dev_file, datetime)
            self.result['return'] = get_rtc_date(command, rtc_name)

        else:
            self.result['return'] = "RTC files not found"
            self.result['rc'] = -1
        self.result['dev_file'] = dev_file
        self.result['sysfs_path'] = path

        self.result['expect'] = date

        return self.result


    # Returns the interrupt count if successful, None otherwise.
    #
    def _rtc_get_interrupt_count(self, command, rtc_name):
        stdout, stderr, returncode = command.run(f"grep {rtc_name} /proc/interrupts | awk '{{print $2}}'")
        if returncode != 0:
            return None

        count = int(stdout[0])
        print(f"_rtc_get_interrupt_count: {count}")

        return count

    # Returns True if successful, False otherwise
    #
    def _rtc_set_alarm_for_1s(self, command, rtc_name):
        stdout, stderr, returncode = command.run(f"grep -rls {rtc_name} /sys/class/rtc/rtc* | sed \"s/[^0-9]//g\"")
        if returncode != 0:
            return False

        num = int(stdout[0])

        stdout, stderr, returncode = command.run(f"echo +1 > /sys/class/rtc/rtc{num}/wakealarm")
        if returncode != 0:
            return False

        return True

    def rtc_set_and_test_alarm(self, command, rtc_name):
        self.result["stage"] = "rtc_set_and_test_alarm"

        self.result["expect"] = 0
        self.result["return"] = None

        count_before = self._rtc_get_interrupt_count(command, rtc_name)
        if count_before == None:
            print("rtc_set_and_test_alarm: no count_before")
            return self.result

        self.result["expect"] = count_before + 1

        if not self._rtc_set_alarm_for_1s(command, rtc_name):
            return self.result

        sleep(1)

        count_after = self._rtc_get_interrupt_count(command, rtc_name)
        if count_after == None:
            print("rtc_set_and_test_alarm: no count_after")
            return self.result

        self.result["expect"] = count_after

        return self.result
