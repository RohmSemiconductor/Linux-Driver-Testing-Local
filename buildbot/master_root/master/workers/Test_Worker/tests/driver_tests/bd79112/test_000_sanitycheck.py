import pytest
import sys

sys.path.append("..")
sys.path.append("./configs")
from test_util import check_result
from addac_class import addac
from config_helpers import config_validate_default
import bd79112
bd79112 = addac(bd79112)

def test_000_sanitycheck(command):
    result = config_validate_default(bd79112, "bd79112")
    check_result(result)
