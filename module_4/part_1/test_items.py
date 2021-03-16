link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
add_to_basket_button_locator = '#add_to_basket_form > button'
# надо добавить остальные языки
button_names = {
    'ru' : 'Добавить в корзину',
    'en-gb' : 'Add to basket',
    'de' : 'In Warenkorb legen',
    'da' : 'Læg i kurv',
    'es' : 'Añadir al carrito',
    'fr' : 'Ajouter au panier'
}


def test_button_language(browser, browser_lang):
    browser.get(link)
    assert browser.find_element_by_css_selector(add_to_basket_button_locator).text == \
           button_names[browser_lang], 'Language mismatch'