class Human:
    def __init__(self, pos_x: int, pos_y: int, speed: int, stamina: int) -> None:
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina

    def move_right(self) -> None:
        self.__pos_x += self.__speed

    def move_left(self) -> None:
        self.__pos_x -= self.__speed

    def move_up(self) -> None:
        self.__pos_y += self.__speed

    def move_down(self) -> None:
        self.__pos_y -= self.__speed

    def get_position(self) -> tuple[int, int]:
        return (self.__pos_x, self.__pos_y)

    def sprint_right(self) -> None:
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x += 2 * self.__speed

    def sprint_left(self) -> None:
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x -= 2 * self.__speed

    def sprint_up(self) -> None:
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y += 2 * self.__speed

    def sprint_down(self) -> None:
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y -= 2 * self.__speed

    def __raise_if_cannot_sprint(self) -> None:
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self) -> None:
        self.__stamina -= 1

