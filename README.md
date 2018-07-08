
# Coding Elliptic Curves in Python

We are not interested in the curve itself, but specific points on the curve. For example, in the curve \\(y^2 = x^3 + 5x + 7\\), we are interested in the coordinate (-1,1). We are thus going to define the class `Point` to be the actual point on a specific curve. The curve has a specifc form, \\(y^2 = x^3 + 5x + 7\\) so we can define the curve with just the two numbers *a* and *b*.

#### For the curve \\(y^2 = x^3 + 5x + 7\\), which of these are on the curve?

\\((-2,4), (3,7), (18,77)\\)


### Try it


```python
# (-2,4), (3,7), (18,77)
# equation in python is: y**2 == x**3 + 5*x + 7

points = ((-2,4), (3,7), (18,77))

# for x, y in points:
    # determine whether (x,y) is on the curve
```

### Test Driven Exercise


```python
class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # make sure that the elliptic curve equation is satisfied
        # y**2 == x**3 + a*x + b
        # if not, throw a RuntimeError
        pass
```
