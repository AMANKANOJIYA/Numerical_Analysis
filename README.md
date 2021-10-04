# VERSION 1.0.1

<img src="https://github.com/AMANKANOJIYA/Numerical_Analysis/blob/master/src/saved.jpg"></img>

[![Downloads](https://static.pepy.tech/personalized-badge/numerical-analysis-aman?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/numerical-analysis-aman)

# Numerical Analysis

This Module is Numerical analysis, area of mathematics and computer science that creates, analyzes, and implements algorithms for obtaining numerical solutions to problems involving continuous variables. Such problems arise throughout the natural sciences, social sciences, engineering, medicine, and business.

## New Added

- [Numerical-analysis](README.md)
- [Vector](Vector.md)

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
from Numerical_Analysis_Aman import <Module>
# =>> _MODULES_
# -> Numerical_Algebra
# -> Numerical_Analysis
# -> Numerical_Integration
# -> Numerical_Interpolation

# Import all
from Numerical_Analysis_Aman import *
```

## Explore (How It Works)

This at present contain 4 parts You can explore them from Below and have some
idea about all methods and Functions

### Numerical Integration

This part contain interpolation.  
`x=Numerical_Analysis_Aman.Numerical_Integration(lower,upper,function)`

- `x.Trapazoid(itration=2)` <a href="https://en.wikipedia.org/wiki/Trapezoidal_rule">Trapazoid Method</a>
- `x.Simpson_13(itration=2)` <a href="https://en.wikipedia.org/wiki/Simpson%27s_rule">Simpson 1/3</a>
- `x.Simpson_38(itration=2)` <a href="https://en.wikipedia.org/wiki/Simpson%27s_rule">Simpson 3/8</a>

### Numerical Analysis

This part contain Integration Method having Three method <br/>
`x = Numerical_Analysis_Aman.Numerical_Analysis(x_0,y_0,x_given,gap,function)`

- `x.Eular( itration = 4 )` <a href="https://en.wikipedia.org/wiki/Euler_method">Eular</a>
- `x.EularModified( itration = 4 )` <a href="https://en.wikipedia.org/wiki/Euler_method">EularModified</a>
- `x.RungaKutta( itration = 4 )` <a href="https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods">RungaKutta</a>

### Numerical Interpolation

This part contain Analysis Method having Four method <br/>
`x=Numerical_Analysis_Aman.Numerical_Interpolation(x_list,y_list,find_value)`

- `x.Langrangian()` <a href="https://en.wikipedia.org/wiki/Lagrange_polynomial">Langrangian</a>
- `x.Newton_Divided()` <a href="https://en.wikipedia.org/wiki/Divided_differences">Newton Divided Differences</a>
- `x.Newton_Forward()` <a href="https://en.wikipedia.org/wiki/Newton_polynomial">Newton Forward</a>
- `x.Newton_Backward()` <a href="https://en.wikipedia.org/wiki/Newton_polynomial">Newton Backward</a>

### Numerical Algebra

This part contain Analysis Method having Three method <br/>
`x=Numerical_Analysis_Aman.Numerical_Algebra(list_1,list_2,list_3)`

- `x.Jacobi(itration=6)` <a href="https://en.wikipedia.org/wiki/Jacobi_method">Jacobi</a>
- `x.Gauss_Seidel(itration=6)` <a href="https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method">Gauss Seidel</a>
- `x.Gauss_Seidel_4(list_4,itration=6)` <a href="https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method">Gauss Seidel for 4 variable</a>

## Usage/Examples

Example and sample for input and how to work on it

```python

import Numerical_Analysis_Aman as na

x = na.Numerical_Integration(2,7,"1/(5*x+3)")
y = na.Numerical_Analysis(0,1,0.2,0.1,"((x**3)*(math.e**(-2*x))-(2*y))")
z = na.Numerical_Interpolation([1891,1901,1911,1921,1931],[46,66,81,93,101],1925)
w = na.Numerical_Algebra([10,1,-1,11.19],[1,10,1,28.08],[-1,1,10,35.61])

# All of them are Initiated at once you can use them individualy as per requirement

# default Itrations - 2
print(x.Trapazoid(  ))
print(x.Simpson_13( ))
print(x.Simpson_38( ))

# default Itrations - 4
print(y.Eular( ))
print(y.EularModified( ))
print(y.RungaKutta( ))

print(z.Langrangian( ))
print(z.Newton_Divided( ))
print(z.Newton_Forward( ))
print(z.Newton_Backward( ))

# default Itrations - 6
print(w.Jacobi( ))
print(w.Gauss_Seidel( ))
# needed Additional list for 4 variable
# print(w.Gauss_Seidel_4(list_4))

```

## Contact

### Authors

- [@AmanKanojiya](https://www.github.com/AMANKANOJIYA)

If any Issue Contact Me through Email <a herf="mailto:aman.kanojiya4203@gmail.com">aman.kanojiya4203@gmail.com</a>

## license

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) <br>
This repository is licensed under the MIT license.
See LICENSE for details.
