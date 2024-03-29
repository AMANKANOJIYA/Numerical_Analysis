"""
Auther : Aman Kanojiya
--------------------------------------------------------------------------
|                  Numerical-ANALYSIS (Nuerical Methods)                 |
--------------------------------------------------------------------------

* Creater Message To all users --
==================================

This Liberary Is based On one of the most fundamental Numerical Methods Topics
.It contain a set of calculations and direct formula based functions which can 
be used In all types of projects as well as to solve the complex problem ,

I am very Much glad to Get contribution on github If any one intrested can visit
my profile or contact me through my email "aman.kanojiya4203@gmail.com"

This project have no restriction evry one can use it as there own and create there
own version. if you like you can give me a small credit It will boost me to create
more such projects and motivate to contribute more in open source

 - Thank You 

"""

# IMPORTS
import numpy as np
import math

# ERROR HANDLING


def Error_Handler(func):
    def inner(*args):
        try:
            return func(*args)
        except Exception as e:
            print(
                f"{type(e).__name__}\n==============\n {e} \n in {func.__name__} function")
            return "error"
    return inner

# MAIN CLASS START


class Numerical_Analysis:
    """Numerical analysis, area of mathematics and computer science that creates,  
    analyzes, and implements algorithms for obtaining numerical solutions to  
    problems involving continuous variables. Such problems arise throughout the 
    natural sciences, social sciences, engineering, medicine, and business.

    In this Module We have Three Methods
    ---> Eular mathod
    ---> Eular Modified method
    ---> Runga Kutta method

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<
     """
    @Error_Handler
    def __init__(self, x_0: float, y_0: float, x_given: float, gap: float, function: str):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_given = x_given
        self.gap = gap
        self.function = str(function)

    @Error_Handler
    def functionToWork(self):
        """
        This Help to generate The Function Output Given as per queestion 
        you can change this value for the code
        may be in next version you can see an another update so that
        the function can also be generated by the given user function input
        """
        return eval(self.function)

    @Error_Handler
    def EularModified(self, itration: int = None):
        """
    >============ Eular Modified Method =================<

    The objective in numerical methods is, as always, to achieve the most accurate (and reliable!) 
    result with the least effort.  
    For integrating the initial value problem (3)  
    the effort is usually measured by the number of times the function 
    $f(t,y)$ must be evaluated in stepping from $a$ to $b$. As we will see, 
    a simple improvement doubles the number of function evaluations per step, 
    but yields a second order method - a winning strategy.

      EularModified() 

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        itration = 4 if itration == None else itration
        create_x = [
            self.x_0+i*self.gap for i in range(2*itration) if (self.x_0+i*self.gap) <= self.x_given]
        create_y = [self.y_0]
        for i in range(0, len(create_x)-1):
            y_get = create_y[-1]+(self.gap *
                                  self.functionToWork(create_x[i], create_y[-1]))
            y_confirm = create_y[-1]+((self.gap/2)*(self.functionToWork(
                create_x[i], create_y[-1])+self.functionToWork(create_x[i]+self.gap, y_get)))
            create_y.append(y_confirm)
        return create_x, create_y

    @Error_Handler
    def Eular(self, itration: int = None):
        """
    >============ Eular Method =================<

    The Euler method is a first-order method, 
    which means that the local error (error per step) is  
    proportional to the square of the step size,  
    and the global error (error at a given time) is proportional  
    to the step size.

      Eular() 

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        itration = 4 if itration == None else itration
        create_x = [
            self.x_0+i*self.gap for i in range(2*itration) if (self.x_0+i*self.gap) <= self.x_given]
        create_y = [self.y_0]
        for i in range(0, len(create_x)-1):
            y_get = create_y[-1]+(self.gap *
                                  self.functionToWork(create_x[i], create_y[-1]))
            create_y.append(y_get)
        return create_x, create_y

    @Error_Handler
    def RungaKutta(self, itration: int = None):
        """
    >============ Eular Modified Method =================<

    listen) RUUNG-ə-KUUT-tah) are a family of implicit and explicit 
    iterative methods, which include the well-known routine called the 
    Euler Method, used in temporal discretization for the approximate 
    solutions of ordinary differential equations.

      RungaKutta()

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        itration = 4 if itration == None else itration
        create_x = [
            self.x_0+i*self.gap for i in range(2*itration) if (self.x_0+i*self.gap) <= self.x_given]
        create_y = [self.y_0]
        for i in range(0, len(create_x)-1):
            k_1 = self.gap * self.functionToWork(create_x[i], create_y[-1])
            k_2 = self.gap * \
                self.functionToWork(
                    create_x[i]+(self.gap/2), create_y[-1]+(k_1/2))
            k_3 = self.gap * \
                self.functionToWork(
                    create_x[i]+(self.gap/2), create_y[-1]+(k_2/2))
            k_4 = self.gap * \
                self.functionToWork(create_x[i]+self.gap, create_y[-1]+k_3)
            k = (k_1+(2*k_2)+(2*k_3)+k_4)/6
            yOut = create_y[-1] + k
            create_y.append(yOut)
        return create_x, create_y


class Numerical_Integration:
    """
    Numerical integration methods can generally be described as combining 
    evaluations of the integrand to get an approximation to the integral. 
    The integrand is evaluated at a finite set of points called integration
    points and a weighted sum of these values is used to approximate 
    the integral.

    In this Module We have Three Methods
    ---> Trapazoid
    ---> Simpson 1/3
    ---> Simpson 3/8

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<

    """
    @Error_Handler
    def __init__(self, lower: float, upper: float, function: str):
        self.x, self.y = eval(str(lower)), eval(str(upper))
        self.function = str(function)

    @Error_Handler
    def Trapazoid(self, itration: int = 2):
        """
    >============ Trapazoid =================<

    Trapezoidal Rule is a rule that evaluates the area under 
    the curves by dividing the total area into smaller trapezoids 
    rather than using rectangles. This integration works by approximating 
    the region under the graph of a function as a trapezoid, 
    and it calculates the area.

      Trapazoid() 

    call this function to get Your Values 
    """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code

                functionToWork(x)
            this function takes 1 input
            """
            return eval(self.function)
        gap = (self.y-self.x)/(itration)
        create_x = [self.x+(i*gap) for i in range(0, itration+1)]
        create_y = [functionToWork(i) for i in create_x]
        formula = (gap/2)*((create_y[0]+create_y[-1])+2 *
                           sum([create_y[i] for i in range(1, len(create_y)-1)]))
        return formula

    @Error_Handler
    def Simpson_38(self, itration: int = 2):
        """
    >============ Simpson 1/3 =================<

    The trapezoidal rule was based on approximating the 
    integrand by a first order polynomial, and then integrating 
    the polynomial over interval of integration. Simpson’s 1/3 rule is an 
    extension of Trapezoidal rule where the integrand is approximated by a 
    second order polynomial.

      Simpson_13() 

    call this function to get Your Values 

        """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code

                functionToWork(x)
            this function takes 1 input
            """
            return eval(self.function)
        gap = (self.y-self.x)/(itration)
        create_x = [self.x+(i*gap) for i in range(0, itration+1)]
        create_y = [functionToWork(i) for i in create_x]
        formula = ((3*gap)/8)*((create_y[0]+create_y[-1])+3*(sum([create_y[i] for i in range(1, len(
            create_y)) if (i) % 3 != 0]))+2*(sum([create_y[i] for i in range(2, len(create_y)-1, 3)])))
        return formula

    @Error_Handler
    def Simpson_13(self, itration: int = 2):
        """
    >============ Simpson 3/8 =================<

    Simpson's 3/8 rule, also called Simpson's second rule 
    requests one more function evaluation inside the integration range,
    and is exact if f is a polynomial up to cubic degree.

      Simpson_38() 

    call this function to get Your Values 
        """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code

                functionToWork(x)
            this function takes 1 input
            """
            return eval(self.function)
        gap = (self.y-self.x)/(itration)
        create_x = [self.x+(i*gap) for i in range(0, itration+1)]
        create_y = [functionToWork(i) for i in create_x]
        formula = (gap/3)*((create_y[0]+create_y[-1])+4*(sum([create_y[i] for i in range(
            1, len(create_y)-1, 2)]))+2*(sum([create_y[i] for i in range(2, len(create_y)-1, 2)])))
        return formula


class Numerical_Interpolation:
    """
    In the mathematical field of numerical analysis,
    interpolation is a type of estimation, a method of constructing 
    new data points within the range of a discrete set of known data points.

    In this Module We have Three Methods
    ---> Langrangian
    ---> Newton Divided Differences
    ---> Newton Forward
    ---> Newton Backward

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<
    """
    @Error_Handler
    def __init__(self, x_list, y_list, find_value):
        self.x_l = x_list
        self.y_l = y_list
        self.find_val = find_value

    @Error_Handler
    def Langrangian(self):
        """
        In numerical analysis, Lagrange polynomials are used for polynomial interpolation.
        For a given set of points  (x_j,y_j) with no two x_j values equal, 
        the Lagrange polynomial is the polynomial of lowest degree that assumes at each 
        value x_j the corresponding value y_j, so that the functions coincide at each point.

        Langrangian()

        call this function to get Your Values
        """
        function = 0
        for i in range(len(self.x_l)):
            list_up = [self.find_val-j for j in self.x_l if j != self.x_l[i]]
            list_down = [self.x_l[i]-j for j in self.x_l if j != self.x_l[i]]
            function = function+self.y_l[i] * \
                (np.prod(list_up)/np.prod(list_down))
        return function

    @Error_Handler
    def Newton_Divided(self):
        """
        In mathematics, divided differences is an algorithm, 
        historically used for computing tables of logarithms and trigonometric functions. 
        ... Divided differences is a recursive division process. 
        The method can be used to calculate the coefficients in the 
        interpolation polynomial in the Newton form.

        Newton_Divided() 

        call this function to get Your Values
        """
        length = len(self.x_l)
        overall = [self.y_l]
        x_gap = 1

        def divisor(x_0, x_1, y_0, y_1):
            y = (y_1-y_0)/(x_1-x_0)
            return y
        for i in range(length, 1, -1):
            local = []
            y_list_itrate = overall[-1]
            for j in range(i-1):
                z = divisor(self.x_l[j], self.x_l[j+x_gap],
                            y_list_itrate[j], y_list_itrate[j+1])
                local.append(z)
            overall.append(local)
            x_gap += 1
        function = 0
        for x in range(len(overall)):
            if x+1 == 1:
                function += overall[x][0]
            else:
                set = ""
                for z in range(x):
                    set = set+(f"*(self.find_val-({self.x_l[z]}))")
                function += ((overall[x][0])*(eval(set[1:])))
        return function

    @Error_Handler
    def Newton_Forward(self):
        """
        Forward Differences: The differences y1 – y0, y2 – y1, y3 – y2, ……,
        yn – yn–1 when denoted by dy0, dy1, dy2, ……, dyn–1 are respectively, 
        called the first forward differences.

        Newton_Forward()

        call this function to get Your Values
        """
        length = len(self.x_l)
        overall = [self.y_l]
        x_gap = 1
        for i in range(length, 1, -1):
            local = []
            y_list_itrate = overall[-1]
            for j in range(i-1):
                z = y_list_itrate[j+1] - y_list_itrate[j]
                local.append(z)
            overall.append(local)
            x_gap += 1
        u = (self.find_val-self.x_l[0])/(self.x_l[1]-self.x_l[0])
        function = 0
        for x in range(len(overall)):
            if x+1 == 1:
                function += overall[x][0]
            else:
                set = ""
                for z in range(x):
                    set += (f"*(u-({z}))")
                function += ((eval(set[1:]))*overall[x][0])/math.factorial(x)
        return function

    @Error_Handler
    def Newton_Backward(self):
        """
        Backward Differences: The differences y1 – y0, y2 – y1, ……, yn – yn–1 
        when denoted by dy1, dy2, ……, dyn, respectively, are called first backward difference.

        Newton_Backward()

        call this function to get Your Values
        """
        length = len(self.x_l)
        overall = [self.y_l]
        x_gap = 1
        for i in range(length, 1, -1):
            local = []
            y_list_itrate = overall[-1]
            for j in range(i-1):
                z = y_list_itrate[j+1] - y_list_itrate[j]
                local.append(z)
            overall.append(local)
            x_gap += 1
        u = (self.find_val-self.x_l[-1])/(self.x_l[1]-self.x_l[0])
        function = 0
        for x in range(len(overall)):
            if x+1 == 1:
                function += overall[x][-1]
            else:
                set = ""
                for z in range(x):
                    set += (f"*(u+({z}))")
                function += ((eval(set[1:]))*overall[x][-1])/math.factorial(x)
        return function


class Numerical_Algebra:
    """
    Numerical linear algebra, sometimes called applied linear algebra,
    is the study of how matrix operations can be used to create computer 
    algorithms which efficiently and accurately provide approximate 
    answers to questions in continuous mathematics. 
    It is a subfield of numerical analysis, and a type of linear algebra.

    In this Module We have Three Methods
    ---> Jacobi
    ---> Gauss Seidel for 3 variables
    ---> Gauss Seidel for 4 variables


>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<
    """
    @Error_Handler
    def __init__(self, l_1: list, l_2: list, l_3: list):
        self.l_1 = l_1
        self.l_2 = l_2
        self.l_3 = l_3

    @Error_Handler
    def Jacobi(self, itration: int = 6):
        """
        In numerical linear algebra, the Jacobi method is an iterative
        algorithm for determining the solutions of a strictly diagonally 
        dominant system of linear equations. Each diagonal element is solved for,
        and an approximate value is plugged in.
        The process is then iterated until it converges.

        Jacobi() 
        Also can pass number of Itration to Perform By default :=> 6
        call this function to get Your Values 
        """
        x_list = [0]
        y_list = [0]
        z_list = [0]
        for i in range(itration):
            x, y, z = x_list[-1], y_list[-1], z_list[-1]
            x_find = (self.l_1[-1]-((self.l_1[1])*(y)) -
                      ((z)*(self.l_1[2])))/self.l_1[0]
            y_find = (self.l_2[-1]-((self.l_2[0])*(x)) -
                      ((z)*(self.l_2[2])))/self.l_2[1]
            z_find = (self.l_3[-1]-((self.l_3[0])*(x)) -
                      ((y)*(self.l_3[1])))/self.l_3[2]
            x_list.append(x_find)
            y_list.append(y_find)
            z_list.append(z_find)
        return x_list, y_list, z_list

    @Error_Handler
    def Gauss_Seidel(self, itration: int = 6):
        """
        In numerical linear algebra, the Gauss–Seidel method, 
        also known as the Liebmann method or the method of successive displacement,
        is an iterative method used to solve a system of linear equations.
        It is named after the German mathematicians Carl Friedrich Gauss
        and Philipp Ludwig von Seidel, and is similar to the Jacobi method.

        Gauss_Seidel() 
        Also can pass number of Itration to Perform By default :=> 6
        call this function to get Your Values 
        """
        x_list = [0]
        y_list = [0]
        z_list = [0]
        for i in range(itration):
            x, y, z = x_list[-1], y_list[-1], z_list[-1]
            x_find = (self.l_1[-1]-((self.l_1[1])*(y)) -
                      ((z)*(self.l_1[2])))/self.l_1[0]
            y_find = (self.l_2[-1]-((self.l_2[0])*(x_find)) -
                      ((z)*(self.l_2[2])))/self.l_2[1]
            z_find = (self.l_3[-1]-((self.l_3[0])*(x_find)) -
                      ((y_find)*(self.l_3[1])))/self.l_3[2]
            x_list.append(x_find)
            y_list.append(y_find)
            z_list.append(z_find)
        return x_list, y_list, z_list

    @Error_Handler
    def Gauss_Seidel_4(self, l_4: list, itration: int = 6):
        """
        In numerical linear algebra, the Gauss–Seidel method, 
        also known as the Liebmann method or the method of successive displacement,
        is an iterative method used to solve a system of linear equations.
        It is named after the German mathematicians Carl Friedrich Gauss
        and Philipp Ludwig von Seidel, and is similar to the Jacobi method.
        Gauss Seidel for 4 Variable 

        Gauss_Seidel_4() 
        Also can pass number of Itration to Perform By default :=> 6
        call this function to get Your Values 
        """
        x_list = [0]
        y_list = [0]
        z_list = [0]
        w_list = [0]
        for i in range(itration):
            x, y, z, w = x_list[-1], y_list[-1], z_list[-1], w_list[-1]
            x_find = (self.l_1[-1]-((self.l_1[1])*(y))-((z)
                      * (self.l_1[2]))-((w)*(self.l_1[3])))/self.l_1[0]
            y_find = (self.l_2[-1]-((self.l_2[0])*(x_find)) -
                      ((z)*(self.l_2[2]))-((w)*(self.l_2[3])))/self.l_2[1]
            z_find = (self.l_3[-1]-((self.l_3[0])*(x_find)) -
                      ((y_find)*(self.l_3[1]))-((w)*(self.l_3[3])))/self.l_3[2]
            w_find = (l_4[-1]-((l_4[0])*(x_find)) -
                      ((y_find)*(l_4[1]))-((z_find)*(l_4[2])))/l_4[3]
            x_list.append(x_find)
            y_list.append(y_find)
            z_list.append(z_find)
            w_list.append(w_find)
        return x_list, y_list, z_list, w_list


if __name__ == "__main__":

    # Test For Varification of error can be removed
    # y = na.Numerical_Analysis(0,1,0.2,0.1,"((x**3)*(math.e**(-2*x))-(2*y))") #2
    # print(y.Eular(  ))
    # print(y.EularModified(  ))
    # print(y.RungaKutta(  ))

    # Test For Varification of error can be removed
    # x = na.Numerical_Integration(2,7,"1/(5*x+3)") #0.4301 - 5
    # print(x.Trapazoid(6))
    # print(x.Simpson_13(6))
    # print(x.Simpson_38(6))

    # Test For Varification of error can be removed
    # z = na.Numerical_Interpolation([1891,1901,1911,1921,1931],[46,66,81,93,101],1925) # 14.666 - 10
    # print(z.Langrangian())
    # print(z.Newton_Divided())
    # print(z.Newton_Forward())
    # print(z.Newton_Backward())

    # Test For Varification of error can be removed
    # w = na.Numerical_Algebra([10,1,-1,11.19],[1,10,1,28.08],[-1,1,10,35.61]) #x=1.23 y=2.34 z=3.45
    # print(w.Jacobi())
    # print(w.Gauss_Seidel())
    # print(w.Gauss_Seidel_4())

    # Test For Varification of error can be removed
    # y = Numerical_Analysis(
    #     0, 1, 0.2, 0.1, "((x**3)*(math.e**(-2*x))-(2*y))")  # 2
    y = Numerical_Analysis(
        0, 1, 0.2, 0.1, "((x**3)*(math.e**(-2*x))-(2*y))")  # 2
    print(y.Eular())
    print(y.EularModified())
    print(y.RungaKutta())

    # Test For Varification of error can be removed
    x = Numerical_Integration(2, 7, "1/(5*x+3)")  # 0.4301 - 5
    print(x.Trapazoid(6))
    print(x.Simpson_13(6))
    print(x.Simpson_38(6))

    # Test For Varification of error can be removed
    z = Numerical_Interpolation([5, 6, 9, 11], [
        12, 13, 14, 16], 10)  # 14.666 - 10
    print(z.Langrangian())
    print(z.Newton_Divided())
    print(z.Newton_Forward())
    print(z.Newton_Backward())

    # Test For Varification of error can be removed
    w = Numerical_Algebra(
        [10, 1, -1, 11.19], [1, 10, 1, 28.08], [-1, 1, 10, 35.61])  # x=1.23 y=2.34 z=3.45
    print(w.Jacobi())
    print(w.Gauss_Seidel())
    # print(w.Gauss_Seidel_4())
