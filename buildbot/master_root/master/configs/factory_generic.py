from buildbot.plugins import util, steps
from factory_helpers import *
from test_boards import *
import functools
import string

import test_config as config

factory_generic_test = util.BuildFactory()

def _initialize_generic_report(product):
    doStepIf_initialize_product_partial = functools.partial(doStepIf_initialize_product, product=product)

    factory_generic_test.addStep(steps.ShellCommand(
        command=["python3", "report_janitor.py", "initialize_product", "generic", product],
        workdir="../tests",
        name=f"Initialize test report: {product}",
        doStepIf=doStepIf_initialize_product_partial,
    ))

def run_generic_tests():
    for power_port in test_boards["generic"]["power_ports"]:
        for test_board in test_boards["generic"]["power_ports"][power_port]:
            for product in test_boards["generic"]["power_ports"][power_port][test_board]["products"]:
                _initialize_generic_report(product)

                generate_dts(factory_generic_test, product, "default")
                copy_generated_dts(factory_generic_test, product, "default")
                build_dtbo(factory_generic_test, product, "default", test_type="generic")
                build_dts(factory_generic_test, product, "default", test_type="generic")
                dts_report(factory_generic_test, product, "default")

                copy_test_kernel_modules_to_nfs(factory_generic_test,
                                                product, "default")

                initialize_driver_test(factory_generic_test, power_port, test_board,
                                       product, "default", test_type="generic")
                generate_driver_tests(factory_generic_test, power_port,
                                      test_boards["generic"]["power_ports"][power_port][test_board]["name"],
                                      product, "generic", "default",
                                      result_dir="generic")

                # dts_tests = check_dts_tests(product)
                # for dts in dts_tests:
                #     generate_dts(factory_generic_test, product, dts)
                #     copy_generated_dts(factory_generic_test, product, dts)
                #     build_dts(factory_generic_test, product, dts, test_type="generic")
                #     dts_report(factory_generic_test, product, dts)

                #     copy_test_kernel_modules_to_nfs(factory_generic_test,
                #                                     product, dts)

                #     initialize_driver_test(factory_generic_test, power_port,
                #                            test_board, product, dts,
                #                            test_type="generic")
                #     generate_driver_tests(factory_generic_test, power_port,
                #                           test_board, product, "dts", dts)

                finalize_product(factory_generic_test, product, "generic")

set_factory_type(factory_generic_test, "generic")
run_generic_tests()
copy_temp_results(factory_generic_test)
save_properties(factory_generic_test, "generic")
