from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

SPECIAL_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)],
}

FREE_OFFERS = {
    "E": (2, "B"),
    "N": (3, "M"),
    "R": (3, "Q"),
}

SAME_ITEM_FREE_OFFERS = {
    "F": (3, 2),
    "U": (4, 3),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # check if all skus are valid
    for sku in skus:
        if sku not in PRICE_TABLE:
            return -1

    item_counts = Counter(skus)
    item_counts = _apply_free_offer(item_counts)
    item_counts = _apply_same_item_free_offer(item_counts)
    total_price = 0

    total_price += _apply_special_offer(item_counts)
    return total_price


def _apply_special_offer(item_counts: Counter) -> int:
    total_price = 0
    for sku, count in item_counts.items():
        if sku in SPECIAL_OFFERS:
            for special_offer_count, special_offer_price in SPECIAL_OFFERS[sku]:
                # Only apply special offer if there are enough items
                if count >= special_offer_count:
                    apply_count = count // special_offer_count
                    total_price += apply_count * special_offer_price
                    count -= apply_count * special_offer_count

        total_price += count * PRICE_TABLE[sku]
    return total_price


def _apply_free_offer(item_counts: Counter) -> Counter:
    for item, (required_qty, free_item) in FREE_OFFERS.items():
        if item in item_counts and free_item in item_counts:
            free_count = item_counts[item] // required_qty
            item_counts[free_item] = max(0, item_counts[free_item] - free_count)
    return item_counts


def _apply_same_item_free_offer(item_counts: Counter) -> Counter:
    for item, (required_qty, free_qty) in SAME_ITEM_FREE_OFFERS.items():
        if item in item_counts:
            free_count = item_counts[item] // required_qty
            item_counts[item] = max(0, item_counts[item] - free_count)
    return item_counts
