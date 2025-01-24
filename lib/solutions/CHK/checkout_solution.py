
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

    
