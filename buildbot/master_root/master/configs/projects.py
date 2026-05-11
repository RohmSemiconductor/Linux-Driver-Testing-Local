from buildbot.plugins import util

# Project layout:
#
# <project name> {                      The name for the project.
#     kernel: {                         Defines what kernel and branch to use. Must have either
#                                       'remote' or 'local' defined, if both are, then 'local' is used.
#         remote: <string>              URL to a remote repository.
#         local: <string>               Path to a local repository.
#         branch: <string>              The branch to use.
#     }
#     modules: {                        Same as above, but for the kernel modules.
#         remote: <string>
#         local: <string>
#         branch: <string>
#     }
#     pollInterval: <number>            Time between polls, in seconds.
#     pollCooldown: <number>            Cooldown after a change is made, in seconds. Helps during
#                                       merge windows, so not every change triggers a rebuild.
#     builderNames: [<string> ...]      Separate builder for each project, these appear separately
#                                       in the BuildBot Web view.
#     workerNames: [<string> ...]       List of workers which can build and run this project,
#                                       'Linux_Worker' is a local worker.
#     schedulerName: <string>           Name for the scheduler.
#     schedulerType: <string>           Type of the scheduler, must be one of 'default', 'release',
#                                       'next', 'stable' or 'rolling_stable'.
#     workdir: <string>                 Optional name for the working directory. Uses the project
#                                       name by default.
#     factory:                          The factory used for this project. This is added automatically.
# }

default_modules = {
    "remote": "https://github.com/RohmSemiconductor/Linux-Driver-Testing.git",
    "branch": "dev-addac-test-kernel-modules",
}

projects = {
    # "linux_mainline": {
    #     "kernel": {
    #         "remote": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
    #         "branch": "master",
    #     },
    #     "modules": default_modules,
    #     "pollInterval": 480,
    #     "pollCooldown": 1100,
    #     "builderNames": ["Linux_Mainline"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-linux_mainline",
    #     "schedulerType": "release",
    # },

    # "test_linux": {
    #     "kernel": {
    #         "remote": "https://github.com/RohmSemiconductor/Linux-Driver-Testing.git",
    #         "branch": "test_linux",
    #     },
    #     "modules": default_modules,
    #     "pollInterval": 60,
    #     "pollCooldown": 80,
    #     "builderNames": ["Test_Linux"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-test_linux",
    #     "schedulerType": "default",
    # },

    # "linux_next": {
    #     "kernel": {
    #         "remote": "https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git",
    #         "branch": "master",
    #     },
    #     "modules": {
    #         "remote": "https://github.com/RohmSemiconductor/Linux-Driver-Testing.git",
    #         "branch": "test-kernel-modules_linux-next",
    #     },
    #     "pollInterval": 480,
    #     "pollCooldown": 1100,
    #     "builderNames": ["linux-next"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-linux-next",
    #     "schedulerType": "next",
    # },

    # "linux_rohm_devel": {
    #     "kernel": {
    #         "remote": "https://github.com/RohmSemiconductor/Linux-Kernel-PMIC-Drivers.git",
    #         "branch": "rohm-pmic-test-temporary",
    #     },
    #     "modules": default_modules,
    #     "pollInterval": 20,
    #     "pollCooldown": 30,
    #     "builderNames": ["linux-rohm-devel"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-linux_rohm_devel",
    #     "schedulerType": "default",
    # },

    # "linux_stable": {
    #     "remote": "https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git",
    #     # "branch": "",
    #     # "pollInterval": 0,
    #     # "pollCooldown": 0,
    # },

    # "linux_fast_test": {
    #     "kernel": {
    #         "remote": "https://github.com/KalleNiemi/linux-fast-test.git",
    #         "branch": "main",
    #     },
    #     "modules": default_modules,
    #     # "pollInterval": 20,
    #     # "pollCooldown": 30,
    #     "builderNames": ["linux-fast-test"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-fast-test",
    #     "schedulerType": "default",
    # },

    # "linux_local_test": {
    #     "kernel": {
    #         # "remote": "https://github.com/RohmSemiconductor/Linux-Driver-Testing-Local.git",
    #         "local": "/home/linuxtest/src/linux",
    #         # "branch": "kernel",
    #         "branch": "master",
    #     },
    #     "modules": {
    #         # "remote": "https://github.com/RohmSemiconductor/Linux-Driver-Testing-Local.git",
    #         "local": "/home/linuxtest/src/Linux-Driver-Testing-Local-Test-Kernel-Modules",
    #         "branch": "test-kernel-modules",
    #     },
    #     "pollInterval": 20,
    #     "pollCooldown": 30,
    #     "builderNames": ["linux-local-test"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": "scheduler-local-test",
    #     "schedulerType": "default",
    # }
}

stable_branches = [
    "linux-5.15.y",             # LTS kernels
    "linux-6.1.y",
    "linux-6.6.y",
    "linux-6.12.y",
    "linux-rolling-stable",     # Rolling short time stable
]

for branch in stable_branches:
    branch = branch.replace(".", "_")

    # projects[f"linux_stable_{branch}"] = {
    #     "kernel": {
    #         "remote": "https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git",
    #         "branch": branch,
    #     },
    #     "modules": default_modules,
    #     "pollInterval": 480,
    #     "pollCooldown": 1100,
    #     "builderNames": [f"linux_stable_{branch}"],
    #     "workerNames": ["Linux_Worker"],
    #     "schedulerName": f"scheduler-linux_stable_{branch}",
    #     "schedulerType": "rolling_stable" if branch == "linux-rolling-stable" else "stable",
    #     "workdir": "linux_stable",
    # }


for project_name in projects:
    projects[project_name]["factory"] = util.BuildFactory()
