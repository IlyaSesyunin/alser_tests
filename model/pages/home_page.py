from selene import browser, have, command, be


class OpenPage:
    def open(self):
        browser.open('https://www.technodom.kz/')
        return self

    def find_region(self, region):
        browser.element('.FieldNext.FieldNext_Size-L.FieldNext_WithLeftIcon.FieldNext_WithRightIcon'
                        '.CitiesModal_search__xAZXc').should(be.blank).type(region.name_region)

    def select_region(self):
        browser.element('.Typography.CitiesList_name__6yw7D.Typography__Body').click()

    def check_changed_region_correct(self, region):
        browser.element('.CitySelector_title__AhpR5').should(have.text(region.name_region))

    def check_changed_region_incorrect(self):
        browser.element('.Typography.Typography__L.Typography__L_Bold').should(
            have.text('К сожалению, мы не нашли ваш город'))

    def find_product(self, product):
        browser.element('#SearchInput').type(product.name).press_enter()
        browser.element(
            '.ProductCardV_titleWrapper__x5c25 .Typography.ProductCardV_title__U38HX.ProductCardV_loading___io2a'
            '.Typography__M').click()

    def check_found_product(self, product):
        browser.element('.Typography.Typography__XL.Typography__XL_Bold').should(
            have.text(product.name))
        browser.element('.ProductActions_price__BnEwP').should(have.text(product.price))
        browser.element('.ProductActions_ratingGuarantee__kN3uy').should(have.text(f'Артикул: {product.code}'))

    def add_to_card(self):
        browser.element('.ButtonNext_Theme-Secondary.BuyButtons_addToCart__M6fVx').click()

    def go_to_card(self):
        browser.element('.ButtonNext_Link.AddedToCartModal_button__cwKMJ').click()

    def check_product_in_card(self, product):
        browser.element('.ProductCardInfoPriceBonus_title__scNbc.Typography__Body').should(
            have.text(product.name))
        browser.element('[data-plw="cart-product-price"]').should(have.text(product.price))

    def clear_card(self):
        browser.element('.CartItemTop_remove__nJxl_').click()

    def check_cleared_card(self):
        browser.element('.EmptyCart_wrapper__voEgr').should(have.text('Корзина пуста'))

    def add_to_favorites(self):
        browser.element('[data-plw="add-to-wishlist"]').click()

    def go_to_favorites(self):
        browser.element('.Message__Button').click()

    def check_favorites(self, product):
        browser.element('[data-testid="product-title"]').should(have.text(product.name))
        browser.element('[data-testid="product-price"]').should(have.text(product.price))

    def clear_favorite(self):
        browser.element('[data-testid="heart-button"]').click()

    def check_cleared_favorites(self):
        browser.element('.EmptyList_block__6dEA5').should(have.text('В избранном пока нет товаров'))


home_page = OpenPage()
