
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=[
        'ros_gsplines', 'gsplines', 'gsplinesopt'
    ],
    package_dir={'': 'src', 'gsplines': 'submodules/gsplines/gsplines',
                 'gsplinesopt':
                 'submodules/gspline_optimizer/gsplinesopt'},
)


setup(**setup_args)
