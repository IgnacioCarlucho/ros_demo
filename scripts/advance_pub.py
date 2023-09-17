#!/usr/bin/env python

# Import libraries
import rospy
from geometry_msgs.msg import Twist



class Controller(object):
    def __init__(self, name, rate, verbose=True):

      # Initialize the node
      rospy.init_node(name)
      # Create a publisher in the node
      self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
      # Create a rate
      self.rate = rospy.Rate(rate)
      self.verbose = verbose
      
      # get form config
      self.vx = 2.
      self.wz = 1.

    def run(self):
      # Create the message that I will send: 
      msg = Twist()
      msg.linear.x = self.vx
      msg.angular.z = self.wz

      # Loop until we pres ctrl+c
      while not rospy.is_shutdown(): 
        # indent! 
        # publish
        self.pub.publish(msg)
        if self.verbose:
          print("Sending velocity: Vx", self.vx, " Wz", self.wz)
        # sleep for the selected rate 
        self.rate.sleep()

if __name__ == '__main__':

    controller_object = Controller('velocity_publisher', 10)
    controller_object.run()