import pytest

from src.category import Category
from src.product import Product




@pytest.fixture
def product():
    return Product(name='Test', description='Test description', price=10.5, quantity=20)

@pytest.fixture
def category(product):
    return Category(name='Test', description='Test description', products=[product, product])

@pytest.fixture
def test_correct_init_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_for_second_class(test_correct_init_product):
    assert test_correct_init_product.name == 'Samsung Galaxy C23 Ultra'
    assert test_correct_init_product.description == '256GB, Серый цвет, 200MP камера'
    assert test_correct_init_product.price == 180000.0
    assert test_correct_init_product.quantity == 5


@pytest.fixture()
def test_summ_numb(test_correct_init_numb):
    assert test_correct_init_numb.all_quantity_unique_product == 8
    assert test_correct_init_numb.all_quantity_category == 1