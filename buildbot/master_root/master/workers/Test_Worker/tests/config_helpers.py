
# This file contains helpers for validating configs. Ideally these would be
# part of some ``Board`` parent class, but this will suffice for now.

def config_validate_default(self, name: str):
    self.result["stage"] = "config_validate_default"
    self.result["product_name"] = name
    self.result["expect_product_name"] = self.board.data["name"]

    return self.result

def config_validate_i2c(self):
    self.result["stage"] = "config_validate_i2c"
    self.result["i2c_bus_type"] = type(self.board.data["i2c"]["bus"])
    self.result["i2c_address_type"] = type(self.board.data["i2c"]["address"])

    return self.result

def config_validate_gpio(self):
    self.result["stage"] = "config_validate_gpio"
    self.result["expect"] = True
    self.result["return"] = False

    if not "gpio" in self.board.data:
        return self.result

    for gpio in self.board.data["gpio"].values():
        if not "label" in gpio or not type(gpio["label"]) is str:
            return self.result
        if not "index" in gpio or not type(gpio["index"]) is int:
            return self.result

    self.result["return"] = True
    return self.result
