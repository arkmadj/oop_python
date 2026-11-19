class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


class Dragon(Unit):
    def __init__(
        self,
        name: str,
        pos_x: int,
        pos_y: int,
        height: int,
        width: int,
        fire_range: int,
    ) -> None:
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range
        self.__hitbox: Rectangle = Rectangle(
            self.pos_x - (self.width / 2),
            self.pos_y - (self.height / 2),
            self.pos_x + (self.width / 2),
            self.pos_y + (self.height / 2),
        )

    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        area: Rectangle = Rectangle(x1, y1, x2, y2)
        return area.overlaps(self.__hitbox)


class Rectangle:
    def overlaps(self, rect: "Rectangle") -> bool:
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_bottom_y() <= rect.get_top_y()
            and self.get_top_y() >= rect.get_bottom_y()
        )

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> float:
        return min(self.__x1, self.__x2)

    def get_right_x(self) -> float:
        return max(self.__x1, self.__x2)

    def get_top_y(self) -> float:
        return max(self.__y1, self.__y2)

    def get_bottom_y(self) -> float:
        return min(self.__y1, self.__y2)

    def __repr__(self) -> str:
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
