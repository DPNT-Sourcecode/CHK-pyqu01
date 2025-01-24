from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

SPECIAL_OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
}

FREE_OFFERS = {
    "E": (2, "B")
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
            # Only apply special offer if there are enough items
            if count >= special_offer_count:
                apply_count = count // special_offer_count
                total_price += apply_count * special_offer_price
                count -= apply_count * special_offer_count

        total_price += count * PRICE_TABLE[sku]
    return total_price


def _apply_special_offer(item_counts):
    pass
