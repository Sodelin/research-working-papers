#!/usr/bin/env python3
"""Exact arithmetic for the conditional three-cycle comparison.

This checks two inputs against the six displayed quartet coefficients and
the rational inequalities used in the time/rate and time-order arguments.
It does not simulate a coalescent, verify the source-model correspondence,
check the JC forward law, or run Lean.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def coefficients(point):
    """The six scalar coefficients in Allman et al. (2024), Proposition 36."""
    g, x, l1, l2, l3, h1, h2 = point
    q = 1 - g
    return (
        l1 * l2 * (g * g * h1 + 2 * g * q + q * q * h2 * x) / 3,
        l1 * (g * g * h1 + g * q * (3 - x) + q * q * h2) / 3,
        l2 * (x + g - g * x) / 3,
        l3 * (1 - g + g * x) / 3,
        l1 * l3 * (g * g * h1 * x + 2 * g * q + q * q * h2) / 3,
        x * l2 * l3 / 3,
    )


def main():
    first = tuple(map(F, ("1/2", "1/2", "1/2", "1/2", "1/2", "1", "9/10")))
    second = tuple(map(F, ("20/33", "32/65", "41/80", "15/32", "13/24", "1", "368/533")))
    expected = tuple(map(F, ("23/320", "11/60", "1/8", "1/8", "17/240", "1/24")))

    assert first != second
    for point in (first, second):
        g, x, l1, l2, l3, h1, h2 = point
        assert h1 == 1 and all(0 < v < 1 for v in (g, x, l1, l2, l3, h2))
        assert coefficients(point) == expected

    # With b=-log(l1), c=-log(l2), d=-log(h2), s=-log(x):
    # first: c=b and s>d; second: c<3b/2 and 3d/2<s.
    assert first[2] == first[3] and first[1] < first[6]
    assert second[3] ** 2 > second[2] ** 3
    assert second[1] ** 2 < second[6] ** 3

    # Additional exact inequalities imply t0(first)<13/8<t0(second)
    # for the specific realization in QUARTET-ZERO-EDGE-EXAMPLE.md.
    assert first[1] == first[3] and first[6] ** 4 > first[2]
    assert second[6] ** 2 < second[2]
    assert second[1] ** 4 < second[3] ** 3

    labels = ("a1", "a2", "b1", "b2", "c1", "c2")
    patterns = Counter("".join(sorted(label[0] for label in group))
                       for group in combinations(labels, 4))
    assert patterns == {"aabb": 1, "aacc": 1, "bbcc": 1,
                        "aabc": 4, "abbc": 4, "abcc": 4}

    print("PASS: both distinct tuples give the same six exact coefficients:",
          ", ".join(map(str, expected)))
    print("PASS: zero h1 edge, strict free probabilities, both rational domain",
          "certificates, and all 15 four-label sampling patterns")
    print("PASS: three rational inequalities for the conditional t0 ordering")
    print("Scope: displayed formula arithmetic and rational certificates only;",
          "no stochastic source/JC-law or Lean verification.")


if __name__ == "__main__":
    main()
