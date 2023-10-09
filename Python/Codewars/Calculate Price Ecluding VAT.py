def excluding_vat_price(price):
    if price:
        TAX = 0.15
        return price / (1 + TAX)
    return -1