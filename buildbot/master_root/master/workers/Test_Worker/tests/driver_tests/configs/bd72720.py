data = {
    "name": "bd72720",

    "i2c": {
        "bus": 2,
        "address": 0x4b
    },

    "rtc": {
        "sys_rtc": "omap_rtc",
        "component_rtc": "bd70528-rtc",
        "rtc_reset": "2001-02-03 00:00:00"
    },

    "regulators": {
        "buck1": {
            "name": "buck1",
            "of_match": "buck1",

            "regulator_en_address": 0x20,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x25,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0xC0
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0xC1,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x20,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x21,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 10000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 10 mV/us"
                    },
                },
            },
        }, # buck1

        "buck2": {
            "name": "buck2",
            "of_match": "buck2",

            "regulator_en_address": 0x2A,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x2F,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0xC0
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0xC1,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x2A,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x2B,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 10000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 10 mV/us"
                    },
                },
            },
        }, # buck2

        "buck3": {
            "name": "buck3",
            "of_match": "buck3",

            "regulator_en_address": 0x30,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x35,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0xC0
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0xC1,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x30,
                    "reg_bitmask": 0b00000010,
                },
            },
        }, # buck3

        "buck4": {
            "name": "buck4",
            "of_match": "buck4",

            "regulator_en_address": 0x36,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x3B,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0xC0
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0xC1,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x36,
                    "reg_bitmask": 0b00000010,
                },
            },
        }, # buck4

        "buck5": {
            "name": "buck5",
            "of_match": "buck5",

            "regulator_en_address": 0x3C,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x3E,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0x78
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0x79,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x3C,
                    "reg_bitmask": 0b00000010,
                },
            },
        }, # buck5

        "buck6": {
            "name": "buck6",
            "of_match": "buck6",

            "regulator_en_address": 0x3F,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x41,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 1500,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xB4
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 3300,
                            "step_mV": 0,
                            "start_reg": 0xB5,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x3F,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x40,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 10000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 10 mV/us"
                    },
                },
            },
        }, # buck6

        "buck7": {
            "name": "buck7",
            "of_match": "buck7",

            "regulator_en_address": 0x42,
            "regulator_en_bitmask": 0b00001000,
            "volt_change_not_allowed_while_on": True,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x44,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 1500,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xB4
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 3300,
                            "step_mV": 0,
                            "start_reg": 0xB5,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x42,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x43,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 5000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 5 mV/us"
                    },
                },
            },
        }, # buck7

        "buck8": {
            "name": "buck8",
            "of_match": "buck8",

            "regulator_en_address": 0x45,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x47,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0x78
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0x79,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x45,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x46,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 5000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 5 mV/us"
                    },
                },
            },
        }, # buck8

        "buck9": {
            "name": "buck9",
            "of_match": "buck9",

            "regulator_en_address": 0x48,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x4A,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0x78
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0x79,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x48,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x49,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 5000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 5 mV/us"
                    },
                },
            },
        }, # buck9

        "buck10": {
            "name": "buck10",
            "of_match": "buck10",

            "regulator_en_address": 0x4B,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x4D,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0xC0
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1700,
                            "step_mV": 0,
                            "start_reg": 0xC1,
                            "stop_reg":  0xFF
                        },
                    },
                },
                "idle_on": {
                    "reg_address": 0x4B,
                    "reg_bitmask": 0b00000010,
                },
                "ramprate": {
                    "of_match": "regulator-ramp-delay",
                    "reg_address": 0x4C,
                    "reg_bitmask": 0b11000000,
                    "range": {
                        "values": {
                            "is_linear": False,
                            "list_mV": [5, 7.5, 10, 12.5],
                            "start_reg": 0b00000000,
                            "stop_reg":  0b11000000
                        },
                    },
                },
            },
            "dts": {
                "default": {
                    "dts_properties": {
                        "regulator-ramp-delay": 5000,
                    },
                    "dts_error_comments": {
                        "regulator-ramp-delay": "FAILURE: ramp rate failed to set to 5 mV/us"
                    },
                },
            },
        }, # buck10

        "ldo1": {
            "name": "buck11",
            "of_match": "ldo1",

            "regulator_en_address": 0x4E,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x54,
                    "volt_reg_bitmask": 0b01111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0x50
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1000,
                            "step_mV": 0,
                            "start_reg": 0x51,
                            "stop_reg":  0x7F
                        }
                    }
                },
                "idle_on": {
                    "reg_address": 0x4E,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo1

        "ldo2": {
            "name": "buck12",
            "of_match": "ldo2",

            "regulator_en_address": 0x59,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x5E,
                    "volt_reg_bitmask": 0b01111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0x50
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1000,
                            "step_mV": 0,
                            "start_reg": 0x51,
                            "stop_reg":  0x7F
                        }
                    }
                },
                "idle_on": {
                    "reg_address": 0x59,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo2

        "ldo3": {
            "name": "buck13",
            "of_match": "ldo3",

            "regulator_en_address": 0x5F,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x64,
                    "volt_reg_bitmask": 0b01111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0x50
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1000,
                            "step_mV": 0,
                            "start_reg": 0x51,
                            "stop_reg":  0x7F
                        }
                    }
                },
                "idle_on": {
                    "reg_address": 0x5F,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo3

        "ldo4": {
            "name": "buck14",
            "of_match": "ldo4",

            "regulator_en_address": 0x65,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x6A,
                    "volt_reg_bitmask": 0b01111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 500,
                            "step_mV": 6.25,
                            "start_reg": 0x00,
                            "stop_reg":  0x50
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1000,
                            "step_mV": 0,
                            "start_reg": 0x51,
                            "stop_reg":  0x7F
                        }
                    }
                },
                "idle_on": {
                    "reg_address": 0x65,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo4

        "ldo5": {
            "name": "buck15",
            "of_match": "ldo5",

            "regulator_en_address": 0x6B,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x6D,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x6B,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo5

        "ldo6": {
            "name": "buck16",
            "of_match": "ldo6",

            "regulator_en_address": 0x6E,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x70,
                    "volt_reg_bitmask": 0b01111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 600,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0x78
                        },
                        "flat": {
                            "is_linear": True,
                            "start_mV": 1800,
                            "step_mV": 0,
                            "start_reg": 0x79,
                            "stop_reg":  0x7F
                        }
                    }
                },
                "idle_on": {
                    "reg_address": 0x6E,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo6

        "ldo7": {
            "name": "buck17",
            "of_match": "ldo7",

            "regulator_en_address": 0x71,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x73,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x71,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo7

        "ldo8": {
            "name": "buck18",
            "of_match": "ldo8",

            "regulator_en_address": 0x74,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x76,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x74,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo8

        "ldo9": {
            "name": "buck19",
            "of_match": "ldo9",

            "regulator_en_address": 0x77,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x79,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x77,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo9

        "ldo10": {
            "name": "buck20",
            "of_match": "ldo10",

            "regulator_en_address": 0x7A,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x7C,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x7A,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo10

        "ldo11": {
            "name": "buck21",
            "of_match": "ldo11",

            "regulator_en_address": 0x7D,
            "regulator_en_bitmask": 0b00001000,

            "settings": {
                "voltage": {
                    "volt_reg_address": 0x7F,
                    "volt_reg_bitmask": 0b11111111,

                    "volt_sel": False,

                    "range": {
                        "values": {
                            "is_linear": True,
                            "start_mV": 750,
                            "step_mV": 10,
                            "start_reg": 0x00,
                            "stop_reg":  0xFF
                        },
                    }
                },
                "idle_on": {
                    "reg_address": 0x7D,
                    "reg_bitmask": 0b00000010
                },
            },
        }, # ldo11
    }
}
