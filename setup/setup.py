import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="numerical-analysis-aman",
    version="1.0.1",
    description="This Module is Numerical analysis, area of mathematics and computer science that creates, analyzes, and implements algorithms for obtaining numerical solutions to problems involving continuous variables. Such problems arise throughout the natural sciences, social sciences, engineering, medicine, and business. This module contain some basic Functions so that it makes easyer to reuse them",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AMANKANOJIYA/Numerical_Analysis",
    author="Aman Kanojiya",
    author_email="aman.kanojiya4203@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Numerical_Analysis_Aman"],
    include_package_data=True,
    install_requires=["numpy"],
    # entry_points={
    #     "console_scripts": [
    #         "Numerical_Analysis=Numerical_Analysis.__main__",
    #     ]
    # },
)
