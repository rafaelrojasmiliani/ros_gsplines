
import std_msgs.msg
from gsplines.services import piecewise2json
from .msg import JointGSplineTrajectory
import rospy


def gspline_to_joint_gspline_trajectory(_trj, _joint_names, _rate):

    result = JointGSplineTrajectory()
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    result.header = header

    result.joint_names = _joint_names
    result.json_representation = piecewise2json(_trj)
    result.rate = _rate
    return result
