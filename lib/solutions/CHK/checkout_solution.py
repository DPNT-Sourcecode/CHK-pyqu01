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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

SPECIAL_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
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

GROUP_DISCOUNT_ITEMS = {"S", "T", "X", "Y", "Z"}
GROUP_DISCOUNT_PRICE = 45
GROUP_DISCOUNT_COUNT = 3


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # check if all skus are valid
    for sku in skus:
        if sku not in PRICE_TABLE:
            return -1

    item_counts = Counter(skus)
    item_counts = _apply_free_offer(item_counts, FREE_OFFERS)
    item_counts = _apply_same_item_free_offer(item_counts, SAME_ITEM_FREE_OFFERS)

    total_price, item_counts = _apply_group_discount(
        item_counts, GROUP_DISCOUNT_ITEMS, GROUP_DISCOUNT_PRICE, GROUP_DISCOUNT_COUNT
    )
    total_price += _apply_special_offer(item_counts, SPECIAL_OFFERS)
    return total_price


def _apply_special_offer(item_counts: Counter, special_offers: dict) -> int:
    total_price = 0
    for sku, count in item_counts.items():
        if sku in special_offers:
            for special_offer_count, special_offer_price in special_offers[sku]:
                # Only apply special offer if there are enough items
                if count >= special_offer_count:
                    apply_count = count // special_offer_count
                    total_price += apply_count * special_offer_price
                    count -= apply_count * special_offer_count

        total_price += count * PRICE_TABLE[sku]
    return total_price


def _apply_free_offer(item_counts: Counter, free_offers: dict) -> Counter:
    for item, (required_qty, free_item) in free_offers.items():
        if item in item_counts and free_item in item_counts:
            free_count = item_counts[item] // required_qty
            item_counts[free_item] = max(0, item_counts[free_item] - free_count)
    return item_counts


def _apply_same_item_free_offer(
    item_counts: Counter, same_item_free_offers: dict
) -> Counter:
    for item, (required_qty, free_qty) in same_item_free_offers.items():
        if item in item_counts:
            free_count = item_counts[item] // required_qty
            item_counts[item] = max(0, item_counts[item] - free_count)
    return item_counts


def _apply_group_discount(
    item_counts: Counter,
    group_discount_items: set,
    group_discount_price: int,
    group_discount_count: int,
) -> tuple[int, Counter]:
    total_price = 0
    group_items = []
    for item in group_discount_items:
        if item in item_counts:
            group_items.extend([item] * item_counts[item])
            item_counts[item] = 0

    # Sort items by price, apply discount to the most expensive items
    group_items.sort(reverse=True, key=lambda x: PRICE_TABLE[x])

    while len(group_items) >= group_discount_count:
        total_price += group_discount_price
        group_items = group_items[group_discount_count:]

    # Update remaining items
    remaining_item_counts = Counter(group_items)
    for item, count in remaining_item_counts.items():
        item_counts[item] = count
    return total_price, item_counts




