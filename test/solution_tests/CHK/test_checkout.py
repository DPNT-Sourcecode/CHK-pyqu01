from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    @pytest.mark.parametrize(
        ("skus", "expected"),
        [
            ("A", 50),
            ("ABCDG", -1),
            ("AAAB", )
        ]
    )
    def test_checkout(self, skus: str, expected: int):
        assert checkout_solution.checkout(skus) == expected

