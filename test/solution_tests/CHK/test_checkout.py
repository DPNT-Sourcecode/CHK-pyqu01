from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            # One B is free
            ("AAABBBEE", 255),
            
            ("QQQRRRUUUU", 330)
        ]
    )
    def test_checkout__mixed_cases(self, skus: str, expected: int):
        assert checkout_solution.checkout(skus) == expected

    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("A", 50),
            ("AAABB", 175),
            ("AAAAC", 200),
            ("ABBBD", 140),
            ("HHHHHHHHHH", 80),
            ("HHHHHHHHHHHHHHHH", 135),
            ("KK", 150),
            ("KKK", 230),
            ("PPPPPPP", 300),
            ("QQQQ", 110),
            ("VVVV", 180),
            ("VVVVV", 220),
            ("VVVVVV", 260)
        ]
    )
    def test_checkout__special_offer(self, skus, expected):
        assert checkout_solution.checkout(skus) == expected

    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("EEB", 80),
            ("EEBB", 110),
            # One B is free, two Bs are 45
            ("EEBBB", 125),
            ("EEEE", 160),
            ("NNNM", 120),
            ("NNNN", 160),
            ("NNNNNM", 200),
            ("RRRQ", 150),
            ("RRRR", 200),
            ("RRRRRQ", 250),
        ]
    )
    def test_checkout__free_offer(self, skus, expected):
        assert checkout_solution.checkout(skus) == expected

    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFFF", 40),
            ("UUU", 120),
            ("UUUU", 120),
            ("UUUUUUU", 240),
        ]
    )
    def test_checkout__same_item_free_offer(self, skus, expected):
        assert checkout_solution.checkout(skus) == expected

    def test_checkout__edge_cases(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("123") == -1






