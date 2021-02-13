
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=[
        'ros_gsplines', 'gsplines', 'gsplinesopt'
    ],
    package_dir={'': 'src', 'gsplines': 'src/ros_gsplines/gsplines/gsplines',
                 'gsplinesopt':
                 'src/ros_gsplines/gspline_optimizer/gsplinesopt'},
)


setup(**setup_args)
