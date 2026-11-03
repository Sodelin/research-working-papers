"""Check selected rational examples for the cap-three expository note."""

from fractions import Fraction as F
from itertools import combinations


VERTICES = tuple(range(4))
EDGES = tuple(combinations(VERTICES, 2))
MATCHINGS = {
    0: [()],
    1: [(edge,) for edge in EDGES],
    2: [(a, b) for a, b in combinations(EDGES, 2) if set(a).isdisjoint(b)],
}


def restrict(matching, retained):
    retained = set(retained)
    return tuple(edge for edge in matching if set(edge) <= retained)


def distribution(weights, retained):
    result = {}
    for count, matchings in MATCHINGS.items():
        for matching in matchings:
            outcome = restrict(matching, retained)
            result[outcome] = result.get(outcome, F(0)) + weights[count] / len(matchings)
    return result


def main():
    a = {0: F(1, 4), 1: F(1, 2), 2: F(1, 4)}
    b = {0: F(1, 3), 1: F(1, 3), 2: F(1, 3)}
    assert [len(MATCHINGS[k]) for k in (0, 1, 2)] == [1, 6, 3]
    for pair in combinations(VERTICES, 2):
        law = distribution(a, pair)
        assert law == distribution(b, pair)
        assert law[()] == F(5, 6)
    for triple in combinations(VERTICES, 3):
        law = distribution(a, triple)
        assert law == distribution(b, triple)
        assert law[()] == F(1, 2)
        assert all(law[(edge,)] == F(1, 6) for edge in combinations(triple, 2))
    assert distribution(a, VERTICES)[()] == F(1, 4)
    assert distribution(b, VERTICES)[()] == F(1, 3)

    d1, n1, d2, n2 = F(5, 6), F(1, 2), F(2, 3), F(8, 27)
    c1, c2 = (d1 - n1) / 2, (d2 - n2) / 2
    e1, e2 = (n1 - d1**3) / 6, (n2 - d2**3) / 6
    assert c1 * d2 + n1 * c2 == (d1 * d2 - n1 * n2) / 2
    assert (n1 * n2 - (d1 * d2)**3) / 6 == d2**3 * e1 + d1**3 * e2 + 6 * e1 * e2
    print("Exact checks passed: four-label matching example and selected serial identities")


if __name__ == "__main__":
    main()
