import pytest
from Polynomial import Polynomial  # Import the Polynomial class from your module

from MutantPolynomial import MutantPolynomial

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

def test_str():
    """Modified tests will account for AOR mutants"""
    
    # Original
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    # mutant tests (AOR)
    mutant_poly = MutantPolynomial(poly.coefficients)

    mutated_str_1 = mutant_poly._str_aor_mutant_1(poly)
    assert not str(mutated_str_1) == "3x^2 + 2"

    mutated_str_2 = mutant_poly._str_aor_mutant_2(poly)
    assert not str(mutated_str_2) == "3x^2 + 2"

    mutated_str_3 = mutant_poly._str_aor_mutant_3(poly)
    assert not str(mutated_str_3) == "3x^2 + 2"


    # edge cases
    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""



def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

    # AOR mutants 
    mutant_poly1 = MutantPolynomial(poly1.coefficients)
    mutant_poly2 = MutantPolynomial(poly2.coefficients)

    mutant_poly_sum1 = mutant_poly1._add_aor_mutant_1(mutant_poly2)
    assert not mutant_poly_sum1.coefficients == [3,1,1] 

    mutant_poly_sum2 = mutant_poly1._add_aor_mutant_2(mutant_poly2)
    assert not mutant_poly_sum1.coefficients == [3,1,1] 

    mutant_poly_sum3 = mutant_poly1._add_aor_mutant_3(mutant_poly2)
    assert not mutant_poly_sum1.coefficients == [3,1,1]

    mutant_poly_sum4 = mutant_poly1._add_aor_mutant_4(mutant_poly2)
    assert not mutant_poly_sum1.coefficients == [3,1,1]


def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6
   

