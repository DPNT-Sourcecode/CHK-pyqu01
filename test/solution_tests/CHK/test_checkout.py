from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("A", 50),
            ("XYZ", -1),
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


