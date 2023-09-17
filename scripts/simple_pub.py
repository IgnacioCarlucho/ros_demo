#!/usr/bin/env python
# Import libraries
import rospy
from geometry_msgs.msg import Twist

# Initialize the node
rospy.init_node('velocity_publisher')
# Create a publisher in the node
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
# Create a rate
rate = rospy.Rate(10)

# Create the message that I will send: 
msg = Twist()
msg.linear.x = 1
msg.angular.z = 1

# Loop until we pres ctrl+c
while not rospy.is_shutdown(): 
  # indent! 
  # publish
  pub.publish(msg)
  # sleep for the selected rate 
  rate.sleep()