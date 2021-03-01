from envs.monkey_zoo.blackbox.island_configs.config_templates.base_template import BaseTemplate
from envs.monkey_zoo.blackbox.island_configs.config_templates.config_template import ConfigValueDescriptor


class Ssh(BaseTemplate):

    @staticmethod
    def should_run(class_name: str) -> bool:
        return True

    config_value_list = [
        ConfigValueDescriptor("basic.exploiters.exploiter_classes", ["SSHExploiter"]),
        ConfigValueDescriptor("basic_network.scope.subnet_scan_list",
                              ["10.2.2.11",
                               "10.2.2.12"]),
        ConfigValueDescriptor("basic.credentials.exploit_password_list",
                              ["Password1!",
                               "12345678",
                               "^NgDvY59~8"
                               ]),
        ConfigValueDescriptor("basic.credentials.exploit_user_list",
                              ["Administrator",
                               "m0nk3y",
                               "user"
                               ]),
        ConfigValueDescriptor("internal.classes.finger_classes",
                              ["SSHFinger",
                               "PingScanner",
                               "HTTPFinger"
                               ])
    ]
