"""Check the note's finite examples exactly; this is not a proof checker."""

from fractions import Fraction as F
from itertools import combinations


def product_features(probabilities):
    return sum(probabilities), sum(a * b for a, b in combinations(probabilities, 2))


def main():
    for n in (3, 4, 10, 100):
        p = [F(3, 5), F(2, 5)] + [F(1, 2)] * (n - 2)
        assert product_features(p) == (F(n, 2), F(n * (n - 1), 8) - F(1, 100))
        assert sum((x - F(1, 2)) ** 2 for x in p) == F(1, 50)
        assert all(0 < x < 1 for x in p)

    law = {(0, 0, 0): F(6, 25), (1, 0, 0): F(1, 50), (1, 1, 0): F(37, 50)}
    assert sum(law.values()) == 1
    assert sum(sum(bits) * mass for bits, mass in law.items()) == F(3, 2)
    assert sum(F(sum(bits) * (sum(bits) - 1), 2) * mass for bits, mass in law.items()) == F(37, 50)
    first_zero = sum(mass for bits, mass in law.items() if bits[0] == 0)
    second_one = sum(mass for bits, mass in law.items() if bits[1] == 1)
    joint = sum(mass for bits, mass in law.items() if bits[0] == 0 and bits[1] == 1)
    assert first_zero * second_one > 0 and joint == 0
    print("PASS: four product witnesses and the nonproduct comparison, exact rational arithmetic")
    print("Scope: finite examples only; no general proof, Lean check or biological validation")


if __name__ == "__main__":
    main()
