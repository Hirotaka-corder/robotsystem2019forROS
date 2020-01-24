#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data
    rospy.loginfo(n)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('once_up', Int32, cb)
    pub = rospy.Publisher('twice_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        n = input()
        pub.publish(n)
        rate.sleep()
