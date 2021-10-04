"""
Auther : Aman Kanojiya

--------------------------------------------------------------------------
|                        Vector (Linear ALgebra)                         |
--------------------------------------------------------------------------

* Creater Message To all users --
==================================

This Liberary Is based On one of the most fundamental Vector Topics
.It contain a set of calculations and direct formula based functions which can 
be used In all types of projects as well as to solve the complex problem ,

I am very Much glad to Get contribution on github If any one intrested can visit
my profile or contact me through my email "aman.kanojiya4203@gmail.com"

This project have no restriction evry one can use it as there own and create there
own version. if you like you can give me a small credit It will boost me to create
more such projects and motivate to contribute more in open source

 - Thank You 

"""
# Import
import math

# MAIN CLASS START


class Vector(object):
    '''
    Vector is a library to get basic functions for Vector operation 
    this module will help user to do some operations on Vector and 
    get the desired Output 
    '''

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The Coordinates must be nonempty")
        except TypeError:
            raise TypeError("The Coordinates must be an iterable")

    def __str__(self):
        '''
        Inform the Matrix corresponding to the value
        '''
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        '''
        Verify wether the two Vectors are equal or not 
        '''
        return self.coordinates == v.coordinates

    def __add__(self, v):
        '''
        adding two Vector with same dimention
        '''
        new_coordinates = [x+y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v):
        '''
        Subtracting two Vector with same Dimention
        '''
        new_coordinates = [x-y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, c):
        '''
        Multiply two Vector with same Dimention
        '''
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        '''
        Scaler Product of a Constant with a Vector
        '''
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        '''
        Magnitude of a Vector
        '''
        return sum([i**2 for i in self.coordinates])**(1/2)

    def normalized(self):
        '''
        Find Unit Vector of a Given Vectors
        '''
        try:
            mag = self.magnitude()
            return Vector([i/mag for i in self.coordinates])
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, n):
        '''
        Dot Product of two Vectors
        '''
        list_zip = zip(self.coordinates, n.coordinates)
        return sum([x*y for x, y in list_zip])

    def angle(self, n, deg=False):
        '''
        Find angle between two Vectors (default Radian)
        '''
        try:
            num = self.dot(n)
            den = (self.magnitude())*(n.magnitude())
            if deg:
                return math.degrees(math.acos(num/den))
            else:
                return math.acos(num/den)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(
                    "Cannot Compute an angle With the Zero Vactor()")
            else:
                raise e

    def is_parallel(self, n):
        '''
        find if the two Give Vectors are parallel to each Other 
        '''
        return (self.is_zero() or v.is_zero() or self.angle(n) == 0 or self.angle(n) == math.pi)

    def is_zero(self, tolerance=1e-10):
        '''
        find if the Give Vectors is Zero Vector
        '''
        return self.magnitude() < tolerance

    def is_orthagonal(self, n, tolerance=1e-10):
        '''
        find if the two Give Vectors are parallel to each Other 
        '''
        return abs(self.dot(n) < tolerance)

    def com_orthogonal_to(self, n):
        """
        Orthogonal Component of Vector over other Vector 
        v.com_orthogonal_to(b)
        v = unit to projected
        b = Projected on
        """
        try:
            return self - self.com_parallel_to(n)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def com_parallel_to(self, n):
        """
        Parallel Component of Vector over other Vector 
        v.com_parallel_to(b)
        v = unit to projected
        b = Projected on
        """
        try:
            u = n.normalized()
            return u.times_scalar(self.dot(u))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, n):
        '''
        Cross Product of two Given Vector (3x3) Only
        '''
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = n.coordinates
            return Vector([y1*z2 - y2*z1, -(x1*z2 - x2*z1), x1*y2 - x2*y1])
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ("0",))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross((v_embedded_in_R3))
            elif (msg == 'too amny values to unpack' or msg == 'need mpre than 1 value to unpcak'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle(self, n):
        '''
        Area of triangle corresponding to the two givern Vector
        '''
        return self.area_of_parallelogram(n) / 2.0

    def area_of_parallelogram(self, n):
        '''
        Area of parallelogram corresponding to the two givern Vector
        '''
        platform = self.cross(n)
        return platform.magnitude()


if __name__ == "__main__":
    # mvr = Vector([-0.221, 7.437])
    # print(mvr.magnitude())  # 7.440282924728065

    # mvr = Vector([8.813, -1.331, -6.247])
    # print(mvr.magnitude())  # 10.884187567292289

    # mvr = Vector([5.581, -2.136])
    # print(mvr.normalized())  # Vector: (0.9339352140866403, -0.35744232526233)

    # mvr = Vector([0, 0, 0])
    ## Vector: (0.3404012959433014, 0.5300437012984873, -0.7766470449528028)
    # print(mvr.normalized())

    mvr = Vector([-8.987, -9.838, 5.031])
    mvr2 = Vector([-4.268, -1.861])
    print(mvr + mvr2)
