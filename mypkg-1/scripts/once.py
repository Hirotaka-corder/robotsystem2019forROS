#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

m = 0

def cb(message):
    global m
    m = message.data
    rospy.loginfo(m)

if __name__ == '__main__':
    rospy.init_node('once')
    sub = rospy.Subscriber('twice_up', Int32, cb)
    pub = rospy.Publisher('once_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        m = input()
        pub.publish(m)
        rate.sleep()
