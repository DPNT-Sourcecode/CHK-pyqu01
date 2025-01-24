from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

SPECIAL_OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # check if all skus are valid
    for sku in skus:
        if sku not in PRICE_TABLE:
            return -1

    item_counts = Counter(skus)
    total_price = 0

    for sku, count in item_counts.items():
        if sku in SPECIAL_OFFERS:
            special_offer_count, special_offer_price = SPECIAL_OFFERS[sku]
            if count >= special_offer_count:
                apply_count = count // special_offer_count
                total_price += apply_count * special_offer_price
                count -= apply_count * special_offer_count

        total_price += count * PRICE_TABLE[sku]
    return total_price




