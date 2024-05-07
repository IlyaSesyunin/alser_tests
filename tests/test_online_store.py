import allure
from model.pages.home_page import home_page
from data.regions import DataRegion
from data.products import DataProduct
from selene import browser

region = DataRegion(name_region='Астана')
product = DataProduct(
    name='Планшет Apple iPad Air 10.9 2022 64GB WiFi Space Grey (MM9C3RK/A)',
    price='384 990',
    code='259249'
)


@allure.tag('web')
@allure.title('Successful a region change to an existing')
def test_change_region_correct():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.check_changed_region_correct(region)


def test_change_region_incorrect():
    incorrect_region = DataRegion(name_region='Qwerty')

    home_page.open()
    home_page.find_region(incorrect_region)
    home_page.check_changed_region_incorrect()


def test_find_product():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.find_product(product)
    home_page.check_found_product(product)


def test_add_product_to_card():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.find_product(product)
    home_page.add_to_card()
    home_page.go_to_card()
    home_page.check_product_in_card(product)


def test_clear_card():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.find_product(product)
    home_page.add_to_card()
    home_page.go_to_card()
    home_page.clear_card()
    home_page.check_cleared_card()


def test_add_favorite():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.find_product(product)
    home_page.add_to_favorites()
    home_page.go_to_favorites()
    home_page.check_favorites(product)


def test_cleared_favorites():
    home_page.open()
    home_page.find_region(region)
    home_page.select_region()
    home_page.find_product(product)
    home_page.add_to_favorites()
    home_page.go_to_favorites()
    home_page.clear_favorite()
    home_page.check_cleared_favorites()
