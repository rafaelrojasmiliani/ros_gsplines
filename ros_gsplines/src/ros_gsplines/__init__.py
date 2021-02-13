"""
This file makes available the submodules
"""
import pathlib
import sys

MOD_PATH = pathlib.Path(__file__).parent.absolute()
GSPLINES_PATH = pathlib.Path(MOD_PATH, 'gsplines')
GSPLINES_OPT_PATH = pathlib.Path(MOD_PATH, 'gspline_optimizer')
sys.path.append(str(GSPLINES_PATH))
sys.path.append(str(GSPLINES_OPT_PATH))

import gsplines
import gsplinesopt

from .trajectory_message import gspline_to_joint_trajectory_message
from .trajectory_message import gspline_to_follow_joint_trajectory_goal
