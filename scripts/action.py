#!/usr/bin/env python
import rospy 
import actionlib
from turtle_actionlib.msg import ShapeAction, ShapeGoal
import time 

# starting node
rospy.init_node('example_turtle_action')

# starting client action
service_action = actionlib.SimpleActionClient("turtle_action", ShapeAction)
service_action.wait_for_server()

# create a message defintion
msg = ShapeGoal()

print(msg)
msg.edges = 6
msg.radius = 3
print(msg)



service_action.send_goal(msg) #goal 