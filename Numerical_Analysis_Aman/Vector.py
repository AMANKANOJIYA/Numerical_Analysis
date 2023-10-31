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
    """
    Vector Class

    This Class is used to create a Vector Object which can be used to perform
    various operations on it. It is a very useful class for Linear Algebra
    and can be used to solve various problems related to it.
    """

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

    def __str__(self) -> str:
        """
        String Representation of the Vector

        Args:
            None

        Returns:
            str: String representation of the Vector

        Attributes:
            None
        """
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v: Vector) -> bool:
        """
        Check if two vectors are equal

        Args:
            v (Vector): Vector to be added

        Returns:
            bool: True if the two vectors are equal else False

        """
        return self.coordinates == v.coordinates

    def __add__(self, v: Vector) -> Vector:
        """
        Add two vectors

        Args:
            v (Vector): Vector to be added

        Returns:
            Vector: Vector after addition

        """

        new_coordinates = [x+y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v: Vector) -> Vector:
        """
        Subtract two vectors

        Args:
            v (Vector): Vector to be subtracted

        Returns:
            Vector: Vector after subtraction

        """
        new_coordinates = [x-y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, n: Vector) -> Vector:
        """
        Multiply two vectors

        Args:
            n (Vector): Vector to be subtracted

        Returns:
            Vector: Vector after Multiplication

        """
        new_coordinates = [x*n for x,
                           n in zip(self.coordinates, n.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c: float) -> Vector:
        """
        Scalar Multiplication of two vectors

        Args:
            c (float): Scalar to be multiplied

        Returns:
            Vector: Vector after Multiplication with c (Scaler Product)

        """
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self) -> float:
        """
        Magnitude of a Vector

        Returns:
            float: Magnitude of the Vector
        """
        return sum([i**2 for i in self.coordinates])**(1/2)

    def normalized(self) -> Vector:
        """
        Nomalized Vector

        Returns:
            Vector: Normalized Vector
        """
        try:
            mag = self.magnitude()
            return Vector([i/mag for i in self.coordinates])
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, n: Vector) -> float:
        """
        Dot Product of two vectors

        Args:
            n (Vector) : Vector to be multiplied

        Returns:
            float: Dot Product of the two vectors

        """
        list_zip = zip(self.coordinates, n.coordinates)
        return sum([x*y for x, y in list_zip])

    def angle(self, n: Vector, deg: bool = False) -> float:
        """
        Angle between two vectors

        Args:
            n (Vector) : Vector to check angle with
            deg (bool) : If True return angle in degree else in radians

        Returns:
            float: Angle between the two vectors
        """
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

    def is_parallel(self, n: Vector) -> bool:
        """
        Check if two vectors are parallel

        Args:
            n (Vector) : Vector to check parallel with

        Returns:
            bool: True if the two vectors are parallel else False
        """
        return (self.is_zero() or n.is_zero() or self.angle(n) == 0 or self.angle(n) == math.pi)

    def is_zero(self, tolerance: float = 1e-10) -> bool:
        """
        Check if a vector is zero vector

        Args:
            tolerance (float) : Tolerance value for the magnitude

        Returns:
            bool: True if the vector is zero vector else False
        """
        return self.magnitude() < tolerance

    def is_orthogonal(self, n: Vector, tolerance: float = 1e-10) -> bool:
        """
        Check if two vectors are orthogonal

        Args:
            n (Vector) : Vector to check orthogonal with
            tolerance (float) : Tolerance value for the magnitude

        Returns:
            bool: True if the two vectors are orthogonal else False
        """
        return self.dot(n) < tolerance

    def com_orthogonal_to(self, n: Vector) -> Vector:
        """
        Orthogonal Component of Vector over other Vector

        Args:
            n (Vector) : Vector to check orthogonal with

        Returns:
            bool : True if the two vectors are orthogonal else False
        """
        try:
            return self - self.com_parallel_to(n)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def com_parallel_to(self, n: Vector) -> Vector:
        """
        Parallel Component of Vector over other Vector

        Args:
            n (Vector) : Vector to check parallel with

        Returns:
        bool : True if the two vectors are parallel else False
        """
        try:
            u = n.normalized()
            return u.times_scalar(self.dot(u))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, n: Vector) -> Vector:
        """
        Cross Product of two vectors

        Args:
            n (Vector) : Vector to check cross with

        Returns:
            Vector : Cross Product of the two vectors (Vector Product)
        """
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

    def area_of_triangle(self, n: Vector) -> float:
        """
        Area of triangle corresponding to the two givern Vector

        Args:
            n (Vector) : Vector to get area with

        Returns:
            float : Area of the triangle
        """
        return self.area_of_parallelogram(n) / 2.0

    def area_of_parallelogram(self, n: Vector) -> float:
        """
        Area of parallelogram corresponding to the two givern Vector

        Args:
            n (Vector) : Vector to get area with

        Returns:
            float : Area of the parallelogram
        """
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
    # Vector: (0.3404012959433014, 0.5300437012984873, -0.7766470449528028)
    # print(mvr.normalized())

    mvr = Vector([-8.987, -9.838, 5.031])
    mvr2 = Vector([-4.268, -1.861])
    print(mvr + mvr2)
