import pytest
import sys
sys.path.append('..')
sys.path.append('./configs')
import bd71828
from test_board import get_board
from test_util import check_result
from pmic_class import pmic
bd71828 = pmic(bd71828)

def test_006_gpio_sysfs(command, board):
    board = get_board("pmic", board)
    assert board and "bd71828" in board["products"] and len(board["pins"]) > 0

    dev_label = board["pins"][0]["label"]
    dev_index = board["pins"][0]["index"]

    test_label = bd71828.board.data["gpio"]["label"]
    test_index = bd71828.board.data["gpio"]["index"]

    result = bd71828.gpio_get_value_via_sysfs(command, dev_label, dev_index, test_label, test_index, 0)
    check_result(result)

    result = bd71828.gpio_get_value_via_sysfs(command, dev_label, dev_index, test_label, test_index, 1)
    check_result(result)
