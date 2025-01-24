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
            # ("EEB", 80),
        ]
    )
    def test_checkout(self, skus: str, expected: int):
        assert checkout_solution.checkout(skus) == expected

