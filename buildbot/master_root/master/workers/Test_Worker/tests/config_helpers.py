
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
