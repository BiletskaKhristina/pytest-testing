
import pytest
from app import Figure


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    figure = Figure(figure_type, 1)
    assert figure.type == figure_type


@pytest.fixture
def square():
    return Figure("квадрат", 10)


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length == 10

@pytest.mark.unit
def test_square_type(square):
    assert square.type == "квадрат"


@pytest.mark.parametrize("figure_type", [
    "ромб", "овал", "", "п'ятикутник"
])
def test_invalid_figure_type(figure_type):
    with pytest.raises(AssertionError):
        Figure(figure_type, 5)


@pytest.mark.parametrize("length", [0, -1, -10, 0.0])
def test_invalid_length(length):
    with pytest.raises(AssertionError):
        Figure("квадрат", length)


@pytest.mark.parametrize("length", ["10", None, "текст"])
def test_non_numeric_length(length):
    with pytest.raises(AssertionError):
        Figure("квадрат", length)


@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


def test_figures_count(allowed_figures):
    assert len(allowed_figures) == 4


def test_triangle_in_figures(allowed_figures):
    assert "трикутник" in allowed_figures
