import pytest
import sys
from time import sleep

sys.path.append("..")
sys.path.append("./configs")
from test_util import *
from kernel_modules import *

def test_merge_dt_overlay(command, product, result_dir):
    result["type"] = "generic"
    result["stage"] = "merge_dt_overlay"
    result["result_dir"] = result_dir

    overlays = kernel_modules["dt_overlays"][product]
    for overlay in overlays:
        stdout, stderr, returncode = command.run(f"dd if=/{overlay} of=/sys/kernel/mva_overlay/overlay_add bs=1M")
        if returncode != 0:
            print(stdout[-1])

    # Sleep is needed here because kernel functions take a bit of time to
    # actually load the modules after dd'ing. 'sleep(2)' is enough for now;
    # increase if this test fails. To manually check for false negatives,
    # run 'lsmod' after running 'dd' to see if the modules are loaded.
    sleep(2)

    stdout, stderr, returncode = command.run("lsmod")
    merged_overlays = kernel_modules["merged_dt_overlay"][product]
    for overlay in merged_overlays:
        result["expect"].append([overlay, 0])
        result["return"].append([overlay, checkStdOut(stdout, overlay)])

    result["lsmod"] = stdout
    check_result(result)
