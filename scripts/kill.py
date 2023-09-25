#!/usr/bin/env python
import rospy 
from turtlesim.srv import Kill
import time 


rospy.init_node('example_turtle_sad')


service_turtle = rospy.ServiceProxy("/kill", Kill)

rospy.wait_for_service("/kill")

service_turtle("turtle1")
