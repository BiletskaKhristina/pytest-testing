
class Figure:
    FIGURES = ("трикутник", "квадрат", "коло", "прямокутник")

    def __init__(self, figure_type, length):
        assert figure_type in self.FIGURES, "Неправильний тип фігури"
        assert isinstance(length, (int, float)), "Довжина має бути числом"
        assert length > 0, "Довжина має бути більшою за нуль"

        self.type = figure_type
        self.length = length

    @property
    def get_figure_length(self):
        return self.length
