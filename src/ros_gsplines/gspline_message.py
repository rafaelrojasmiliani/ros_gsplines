
import std_msgs.msg
from gsplines.services import piecewise2json
from gsplines.services import json2piecewise
from .msg import JointGSplineTrajectory
import rospy


def gspline_to_joint_gspline_trajectory(_trj, _joint_names, _rate):

    result = JointGSplineTrajectory()
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time()
    result.header = header

    result.joint_names = _joint_names
    result.json_representation = piecewise2json(_trj)
    result.rate = rospy.Duration.from_sec(_rate)
    return result


def joint_gspline_trajectory_to_gspline(_jgt):
    result = json2piecewise(_jgt.json_representation)
    return result
