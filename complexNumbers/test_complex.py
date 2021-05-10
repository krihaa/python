from complex import Complex
def test_complex_addition():
    """A unit test for complex numbers additions"""
    assert Complex(2,3) + Complex(1,1) == Complex(3,4)
def test_complex_substraction():
    """A unit test for complex numbers subtraction"""
    assert Complex(3,4) - Complex(1,2) == Complex(2,2)
    assert (2+3j) - Complex(1,1) == Complex(1,2)
    assert Complex(3,4) - 2 == Complex(1,4)
    assert 2 - Complex(3,4) == Complex(-1,-4)
def test_complex_conjugate():
    """A unit test for complex number conjugate"""
    assert Complex(3,4).conjugate() == Complex(3,-4)
def test_complex_modulus(): 
    """A unit test for complex number modulus"""
    assert Complex(3,4).modulus() == 5

# extra test
def test_complex_mul(): 
    """A unit test for complex number multiply"""
    assert Complex(3,2) * Complex(1,4) == Complex(-5,14)

# 3.4 tests
def test_complex_python():
    """Unit tests for how Complex behaves with default python types"""
    assert Complex(2,3) + (2+2j) == Complex(4,5)
    assert (2+2j) + Complex(2,3) == Complex(4,5)
    assert Complex(2,3) * 2 == Complex(4,6)
    assert 2j + Complex(2,3) == Complex(2,5)
    assert Complex(2,3) + 2j == Complex(2,5)
    assert Complex(2,3) + 2 == Complex(4,3)
    assert 2 * Complex(2,3) == Complex(4,6)
    assert (3+2j) * Complex(1,4) == Complex(-5,14)
    assert Complex(1,4) * (3+2j) == Complex(-5,14)