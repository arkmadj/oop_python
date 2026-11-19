class Human:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


class Archer(Human):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self) -> int:
        return self.__num_arrows

    def use_arrows(self, num: int) -> None:
        if num > self.__num_arrows:
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name, num_arrows)

    def triple_shot(self, target: Human) -> str:
        self.use_arrows(3)
        return f"{target.get_name()} was shot by 3 crossbow bolts"
