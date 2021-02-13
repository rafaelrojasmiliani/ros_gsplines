from . import gsplines
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
from control_msgs.msg import JointTolerance
from control_msgs.msg import FollowJointTrajectoryActionGoal
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryGoal
from actionlib_msgs.msg import GoalID

import numpy as np
import rospy
import std_msgs.msg


def gspline_to_joint_trajectory_message(_trj, _joint_names, _sample_rate):
    """ Convert a piecewise curve into a trajectory message"""
    msg = JointTrajectory()
    trj_d = _trj.deriv()
    trj_2d = _trj.deriv(2)
    msg.joint_names = _joint_names
    time_span = np.arange(0, _trj.T_, 1.0 / _sample_rate)

    for time_i in time_span:
        trjpoint = JointTrajectoryPoint()
        trjpoint.positions = list(_trj(time_i).ravel())
        trjpoint.velocities = list(trj_d(time_i).ravel())
        trjpoint.accelerations = list(trj_2d(time_i).ravel())
        trjpoint.effort = [0] * _trj.dim_
        trjpoint.time_from_start = rospy.Duration.from_sec(time_i)
        msg.points.append(trjpoint)
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    msg.header = header
    return msg


def gspline_to_follow_joint_trajectory_goal(_trj, _joint_names, _sample_rate):
    trj_msg = gspline_to_joint_trajectory_message(
        _trj, _joint_names, _sample_rate)
    msg = FollowJointTrajectoryGoal()
    msg.trajectory = trj_msg
    return msg
