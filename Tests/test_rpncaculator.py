import pytest
from Calculator.rpncalculator import RpnCalculator as calc

def test_push():
    testcalc = calc()
    testcalc.push(0)
    assert testcalc.result() == 0

def test_stack():
    testcalc = calc()
    testcalc.push(1)
    testcalc.push(2)
    testcalc.push(3)

    assert testcalc.stack() == [1,2,3]

def test_pop():
    testcalc = calc()
    testcalc.push(1)
    testcalc.push(2)
    result = testcalc.pop()
    
    assert result == 2

def test_clear():
    testcalc = calc()
    testcalc.push(1)
    testcalc.push(2)
    testcalc.clear()
    result = len(testcalc.stack())
    assert result == 0

#Push 2, Push 3 (add) -> 5
@pytest.mark.parametrize("a, b, c",
   [(2, 3, 5),
    (2, -3, -1),
    (5, 3, 8)])
def test_add(a, b, c):
    testcalc = calc()
    testcalc.push(a)
    testcalc.push(b)
    testcalc.add()
    r = testcalc.result()
    assert r == c

# Push 5, Push 2, (div) -> 2.5
@pytest.mark.parametrize("a, b, c",
    [(5, 2, 3),
    (6, 2, 4),
    (3, 9, -6)])
def test_sub(a, b, c):
    testcalc = calc()
    testcalc.push(a)
    testcalc.push(b)
    testcalc.sub()
    r = testcalc.result()
    assert r == c

@pytest.mark.parametrize("a, b, c",
    [(5, 2, 2.5),
    (6, 2, 3),
    (9, 3, 3)])
def test_div(a, b, c):
    testcalc = calc()
    testcalc.push(a)
    testcalc.push(b)
    testcalc.div()
    r = testcalc.result()
    assert r == c 


#Push 2, Push 3, (mul) -> 6
@pytest.mark.parametrize("a, b, c",
    [(2, 3, 6),
    (1, 3, 3),
    (3, 3, 9)])
def test_mul(a, b, c):
    testcalc = calc()
    testcalc.push(a)
    testcalc.push(b)
    testcalc.mul()
    r = testcalc.result()
    assert r == c
    
#Push 9, (sqrt) -> 3
@pytest.mark.parametrize("a, c",
    [(9, 3),
    (1, 1),
    (16, 4)])
def test_sqrt(a, c):
    testcalc = calc()
    testcalc.push(a)
    testcalc.sqrt()
    r = testcalc.result()
    assert r == c