# VERSION 1.0.1

# Vector

Vectors are used in science to describe anything that has both a direction and a magnitude. They are usually drawn as pointed arrows, the length of which represents the vector's magnitude. Vectors have many real-life applications, including situations involving force or velocity. For example, consider the forces acting on a boat crossing a river. The boat's motor generates a force in one direction, and the current of the river generates a force in another direction. Both forces are vectors

## Official Release

<a href="https://pypi.org/project/numerical-analysis-aman/">Pypi</a> ,
<a href="https://pepy.tech/project/numerical-analysis-aman">Pepy</a>

## How to Install

Pip install this module from your console<br/>

```bash

pip install numerical-analysis-aman

```

Import this module to your Work Space<br/>

```python

# Import In Python File
from Numerical_analysis_aman import Vector

# Import all
from Numerical_Analysis_Aman import *

```

## Explore (How It Works)

### Representation of Vector in Module

Representaion of vector in module when we declare an array to be Vector :<br>
`Vector : ( 1, 2, 3, 4 )`

### Basic Operation on Vector

Addition, Subtraction, Product( Cross , Dot), equality

```python
# Declaration
v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
a = 5

# Addition
print( v1 + v2 )

# Subtraction
print( v1 -  v2 )

# Cross Product
print( v1.cross(v2) )

# Dot Product
print( v1.dot(v2) )

# Equality
print( v1 == v2 )

# Scaler Product
print( v1.times_scalar(a))
```

### Get Property

Get property helps to to get basic property of Declared Vector

```python
# Declaration
v1 = Vector([3,4,5])
v2 = Vector([2,4,6])
a = 5

# Magnitude
print( v1.magnitude() )

# Normalized Vector
print( v1.normalized() )

# Angle
print( v1.angle(v2) ) #RADIAN output
print( v1.angle( v2, deg=True ) ) #Degree output

```

### Between two Vector

```python
# Declaration
v1 = Vector([1,5,8])
v2 = Vector([6,2,5])
a = 3

# Check Parallel
print(v1.is_parallel(v2))

# Check orthogonal
print(v1.is_orthogonal(v2))

# Check Parallel
print(v1.is_zero())

# Parallel Component of Projection
print( v1.com_parallel_to(v2))

# Orthogonal Component of Projection
print( v1.com_orthogonal_to(v2))
```

**_Maybe in future Version You will get more Advanced functions for Vector so stay Tuned_**

## Contact

### Authors

- [@AmanKanojiya](https://www.github.com/AMANKANOJIYA)

If any Issue Contact Me through Email <a herf="mailto:aman.kanojiya4203@gmail.com">aman.kanojiya4203@gmail.com</a>

## license

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) <br>
This repository is licensed under the MIT license.
See LICENSE for details.





