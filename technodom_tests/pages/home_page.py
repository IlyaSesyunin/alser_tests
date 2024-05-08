from selene import browser, have, be
import allure


class OpenPage:
    def open(self):
        with allure.step("Open home page"):
            browser.open("/")

    def find_region(self, region):
        with allure.step("Find the region"):
            browser.element('#CitiesModalSearch').should(be.blank).type(region.name_region)

    def select_region(self):
        with allure.step("Select region"):
            browser.element('[data-testid="citiesList"] .CitiesList_listItem__dVrVg').click()

    def check_changed_region_correct(self, region):
        with allure.step("Check correct changed region"):
            browser.element('.CitySelector_title__AhpR5').should(have.text(region.name_region))

    def check_changed_region_incorrect(self):
        with allure.step("Check error of changing region"):
            browser.element('.Typography.Typography__L.Typography__L_Bold').should(
                have.text('К сожалению, мы не нашли ваш город'))

    def find_product(self, product):
        with allure.step("Find product"):
            browser.element('#SearchInput').type(product.name).press_enter()
            browser.element('[data-testid="product-title"]').click()

    def check_found_product(self, product):
        with allure.step("Check found product"):
            browser.element('h1.Typography').should(have.text(product.name))
            browser.element('[data-testid="product-price"]').should(have.text(product.price))
            browser.element('.ProductActions_ratingGuarantee__kN3uy').should(have.text(f'Артикул: {product.code}'))

    def add_to_card(self):
        with allure.step("Add product to the card"):
            browser.element('[data-testid="buy-buttons"]').click()

    def go_to_card(self):
        with allure.step("Go to the card"):
            browser.element('[data-testid="add-to-cart-modal"] .AddedToCartModal_button__cwKMJ').click()

    def check_product_in_card(self, product):
        with allure.step("Check product in the card"):
            browser.element('[data-testid="cart-product-item"] .ProductCardInfoPriceBonus_title__scNbc').should(
                have.text(product.name))
            browser.element('[data-plw="cart-product-price"]').should(have.text(product.price))

    def clear_card(self):
        with allure.step("Clear card"):
            browser.element('[data-testid="delete-checked-products"]').should(be.visible).click()

    def check_cleared_card(self):
        with allure.step("Check cleared card"):
            browser.element('.EmptyCart_wrapper__voEgr').should(have.text('Корзина пуста'))

    def add_to_favorites(self):
        with allure.step("Add product to the favorites list"):
            browser.element('[data-plw="add-to-wishlist"]').click()

    def go_to_favorites(self):
        with allure.step("Go to the favorites list"):
            browser.element('.Message__Button').click()

    def check_favorites(self, product):
        with allure.step("Check the product in the favorites list"):
            browser.element('[data-testid="product-title"]').should(have.text(product.name))
            browser.element('[data-testid="product-price"]').should(have.text(product.price))

    def clear_favorite(self):
        with allure.step("Clear favorite list"):
            browser.element('[data-testid="heart-button"]').should(be.visible).click()

    def check_cleared_favorites(self):
        with allure.step("Check cleared favorite list"):
            browser.element('.EmptyList_block__6dEA5').should(have.text('В избранном пока нет товаров'))


home_page = OpenPage()
