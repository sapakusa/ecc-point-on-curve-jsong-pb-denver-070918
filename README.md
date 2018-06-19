=== Coding Elliptic Curves in Python

We are not interested in the curve itself, but specific points on the curve. For example, in the curve y^2^=x^3^+5x+7, we are interested in the coordinate (-1,1). We are thus going to define the class `Point` to be the actual point on a specific curve. The curve has a specifc form, y^2^=x^3^+ax+b so we can define the curve with just the two numbers *a* and *b*.

[source,python]
----
class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3+self.a*self.x + self.b: # <1>
	    raise ValueError('Point ({},{}) is not on the curve where a,b={},{}'.format(x,y,a,b))

    def __eq__(self, other): # <2>
        return self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y

----
<1> We check here that the point is actually on the curve.
<2> Points are equal iff they are on the same curve and have the same coordinates


#### 4.1. For the curve \\(y^2 = x^3 + 5x + 7\\), which of these are on the curve?

\\((-2,4), (3,7), (18,77)\\)

#### 4.2. Make [this test](/edit/session1/ecc.py) pass
```
ecc.py:PointTest:test_on_curve
```


```python
# Exercise 4.1

# (-2,4), (3,7), (18,77)
# equation in python is: y**2 == x**3 + 5*x + 7

points = ((-2,4), (3,7), (18,77))

for x, y in points:
    # determine whether (x,y) is on the curve
```


```python
# Exercise 4.2

reload(ecc)
run_test(ecc.PointTest('test_on_curve'))
```
