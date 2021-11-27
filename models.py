from typing import Any, Union


class Condition:
    key: str
    operator: str
    operand: Union[str, list, int]

    def __init__(self, key: str, operator: str, operand: Union[str, list[str, Any], int]):
        self.key = key
        self.operator = operator
        self.operand = operand
