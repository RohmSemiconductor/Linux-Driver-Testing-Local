data={
'name':'bd9573',
'i2c':{
    'bus':      2,
    'address':  0x30,
    },

'regulators':{
    'VD50':{
        'name': 'buck1',
        'of_match': 'regulator-vd50',
        'regulator_en_address':         0x41,
        'regulator_en_bitmask':         0b11111111,

        'regulator_sel_bitmask':        0b00000010,
        'regulator_pwm_fix_bitmask':    0b00001000,

        'settings':{
            'voltage':{
                'volt_reg_address':             0x50,
                'volt_reg_bitmask':             0b00000111,

                'volt_sel': False,

                'range':{
                    'values':{
                        'is_linear':            True,
                        'is_offset_bipolar':    True,
                        'offset_sign_bitmask':  0b1000000,
                        'offset_sign_address':  0x50,
                        'start_mV':             5000,
                        'step_mV':              100,
                        'start_reg':            0x00,
                        'stop_reg':             0x05,
                    }
                },
            },
        },
    }, # VD50

    'VD18':{
        'name': 'buck2',
        'of_match':'regulator-vd18',

        'regulator_en_address':         0x42,
        'regulator_en_bitmask':         0b11111111,

        'regulator_sel_bitmask':        0b00000010,
        'regulator_pwm_fix_bitmask':    0b00001000,

        'settings':{
            'voltage':{
                'volt_reg_address':             0x53,
                'volt_reg_bitmask':             0b00000111,

                'volt_sel': False,

                'range':{
                    'values':{
                        'is_linear':    True,
                        'is_bipolar':   True,
                        'sign_bitmask': 0b1000000,
                        'sign_address': 0x53,
                        'start_mV':     1800,
                        'step_mV':      20,
                        'start_reg':    0x00,
                        'stop_reg':     0x07,
                    },
                },
            },
        },
    }, #VD18 END

    'VDDDR':{
        'name': 'buck3',
        'of_match': 'regulator-vdddr',
        'regulator_en_address':         0x43,
        'regulator_en_bitmask':         0b11111111,

        'regulator_sel_bitmask':        0b00000010,
        'regulator_pwm_fix_bitmask':    0b00001000,

        'settings':{
            'voltage':{
                'volt_reg_address':             0x56,
                'volt_reg_bitmask':             0b00011111,

                'volt_sel': False,

                'range':{
                    'values':{
                        'is_linear':    True,
                        'is_bipolar':   True,
                        'sign_bitmask': 0b1000000,
                        'sign_address': 0x56,
                        'start_mV':     1350,
                        'step_mV':      10,
                        'start_reg':    0x00,
                        'stop_reg':     0x1F,
                    },
                },
            },
        },
    }, #VDDDR END

    'VD10':{
        'name': 'buck4',
        'of_match':'regulator-vd10',

        'regulator_en_address':     0x44,
        'regulator_en_bitmask':     0b11111111,

        'settings':{
            'voltage':{
                'volt_reg_address':         0x59,
                'volt_reg_bitmask':         0b00011111,

                'volt_sel':False,

                'range':{
                    'values':{
                        'is_linear':    True,
                        'is_bipolar':   True,
                        'sign_bitmask': 0b1000000,
                        'sign_address': 0x59,
                        'start_mV':     1030,
                        'step_mV':      10,
                        'start_reg':    0x00,
                        'stop_reg':     0x1F,
                    },
                },
            },
        },
    }, #VD10 END

    'VOUTL1':{
        'name': 'buck5',
        'of_match':'regulator-voutl1',

        'regulator_en_address':     0x45,
        'regulator_en_bitmask':     0b11111111,

        'settings':{
            'voltage':{
                'volt_reg_address':         0x5C,
                'volt_reg_bitmask':         0b00000111,

                'volt_change_not_allowed_while_on': True,
                'volt_sel':False,

                'range':{
                    'values':{
                        'is_linear':    True,
                        'is_bipolar':   True,
                        'sign_bitmask': 0b1000000,
                        'sign_address': 0x5C,
                        'start_mV':     2500,
                        'step_mV':      40,
                        'start_reg':    0x00,
                        'stop_reg':     0x7,
                    },
                },
            },
        },
    }, #VOUTL1 END

    'VOUTS1':{
        'name': 'buck6',
        'of_match':'regulator-vouts1',

        'regulator_en_address':     0x46,
        'regulator_en_bitmask':     0b11111111,

        'settings':{
            'voltage':{
                'volt_sel':False,

                'range':{
                    'values':{
                        'is_linear':True,
                        'start_mV':3300,
                        'step_mV':0,
                        'start_reg':0x00,
                        'stop_reg':0x00,
                    },
                    # 'flat':{
                    #     'is_linear':True,
                    #     'start_mV':1600,
                    #     'step_mV':100,
                    #     'start_reg':0x00,
                    #     'stop_reg':0x03,
                    # }
                },
            },
            'ocp':{
                'of_match': 'regulator-oc-protection-microamp',
                'reg_bitmask':              0b00111111,
                'reg_address':              0x60,
                'range':{
                    'values':{
                        'is_linear':            True,
                        'start_mV':             300,
                        'step_mV':              50,
                        'start_reg':            0x06,
                        'stop_reg':             0x1B,
                    },
                    'clip_low':{
                        'is_linear':            True,
                        'start_mV':             300,
                        'step_mV':              0,
                        'start_reg':            0x01,
                        'stop_reg':             0x05,
                    },
                    'clip_high':{
                        'is_linear':            True,
                        'start_mV':             1350,
                        'step_mV':              0,
                        'start_reg':            0x1C,
                        'stop_reg':             0x3F,
                    },
                    'disabled':{
                        'is_linear':            True,
                        'start_mV':             0,
                        'step_mV':              0,
                        'start_reg':            0x00,
                        'stop_reg':             0x00,
                    }
                }
            }
        },

        #### DEVICE TREE TEST SECTION
        #   'dts' is used to generate device tree source files
        #   'dts_error_comments' is error message if setting failed

        'dts':{

            'default':{
                'dts_properties':{
                    'regulator-oc-protection-microamp': 1350000,
                    'regulator-oc-warn-microamp': 350000,
                },
                'dts_error_comments':{
                    'regulator-oc-error-microamp': ' FAILURE: OCP SET failed to set to 1350 mA (high clip)',
                    'regulator-oc-warn-microamp': ' FAILURE: OCW SET failed to set to 350 mA (low clip)',
                },
            },
        },
    }, #VOUTS1 END

} #regulators END
} #bd9576 END
