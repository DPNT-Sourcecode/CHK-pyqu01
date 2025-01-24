from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("A", 50),
            ("1234", -1),
            ("AAABB", 175),
            ("AAAAC", 200),
            ("ABBBD", 140),
            ("", 0),
            ("EEB", 80),
            ("EEBB", 110),
            # One B is free, two Bs are 45
            ("EEBBB", 125),
            ("EEEE", 160),
            ("AAAAA", 200),
            ("AAAAAA", 250),
            ("AAAAAAA", 300),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFFF", 40)
        ]
    )
    def test_checkout(self, skus: str, expected: int):
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
    def test_checkout_special_offer(self, skus, expected):
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
    def test_checkout_free_offer(self, skus, expected):
        assert checkout_solution.checkout(skus) == expected




