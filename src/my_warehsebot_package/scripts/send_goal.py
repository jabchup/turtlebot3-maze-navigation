#!/usr/bin/env python3 

import rospy 
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

if __name__ == '__main__':

	# Create a ROS node
	rospy.init_node('send_goals')
	
	# Create a ROS move_base action client
	client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
	
	# Client to wait till action server is on 
	client.wait_for_server()
	
	# Create a goal post
	goal_1 = MoveBaseGoal()
	goal_1.target_pose.headerframe_id = 'map'
	goal_1.target_pose.pose.position.x = 0
	goal_1.target_pose.pose.position.y = 0
	#goal_1.target_pose.pose.position.z = 
	#goal_1.target_pose.pose.orientation.x = 
	#goal_1.target_pose.pose.orientation.y = 
	goal_1.target_pose.pose.orientation.z = 0
	#goal_1.target_pose.pose.orientation.w = 
	
	# Client to send goal post to move_base action server
	client.send_goal(goal_1)
	
	client.wait_for_result()
	#rospy.loginfo('Goal reached')
	print('Goal reached')
