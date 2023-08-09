from __future__ import annotations

from app.knights.knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def battle(self) -> None:
        self.first_knight.hp -= \
            self.second_knight.power - self.first_knight.protection

        self.second_knight.hp -= \
            self.first_knight.power \
            - self.second_knight.protection

        # check if someone fell in battle
        for knight in [self.first_knight, self.second_knight]:
            if knight.hp <= 0:
                knight.hp = 0