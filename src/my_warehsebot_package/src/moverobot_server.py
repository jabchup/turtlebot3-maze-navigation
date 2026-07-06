#!/usr/bin/env python3

import rospy
import actionlib
import time
import my_warehsebot_package.msg

class MoveRobotServer():
	
	# Create Feedback and Result Messages
	def __init__(self):
		# Create server
		self._action_server = actionlib.SimpleActionServer('moverobot', my_warehsebot_package.msg.MoveRobotAction, self.execute_callback, False)
		# Use underscore because of library 
		
		
		# Start server
		self._action_server.start()
		rospy.loginfo('Starting Action Server')
		
	# Callback function to RUN AFTER ACK A GOAL from server
	def execute_callback(self, goal_handle):
		rospy.loginfo('Starting Move Robot')
		
		# Initiate the feedback message current num to the action request starting num
		feedback_pose = my_warehsebot_package.msg.MoveRobotFeedback()
		feedback_msg.current_pose = goal_handle.starting_pose
		
		feedback_velo = my_warehsebot_package.msg.MoveRobotFeedback()
		feedback_msg.current_velo = goal_handle.starting_velo
		
		while feedback_msg.current_pose <= 100:
		
			# Publish feedback
			self._action_server.publish_feedback(feedback_msg)
		
			# Print log message
			rospy.loginfo('Feedback: {0}'.format(feedback_msg.current_pose))
			rospy.loginfo('Feedback: {1}'.format(feedback_msg.current_velo))
		
			# Increment feedback message current_pose and current_velo
			feedback_msg.current_pose = feedback_msg.current_pose + 1
			feedback_msg.current_velo = feedback_msg.current_velo + 1
		
			# Wait a second before counting down next number
			time.sleep(1)
		
		self._action_server.publish.feedback(feedback_msg)
		rospy.loginfo('Feedback: {0}'.format(feedback_msg.current_pose))
		rospy.loginfo('Feedback: {1}'.format(feedback_msg.current_velo))		
		rospy.loginfo('Done')
	
		result = my_warehsebot_package.msg.MoveRobotResult()
		result.is_finished = True
	
		# Indicate the goal is successful
		self._action_server.set_succeeded(result)

def main(arg=None):
	
	# Init ROS and give node a name
	rospy.init_node('moverobot_server')
	moverobot_server = MoveRobotServer()
	rospy.spin() // Wait someone to send request
	
if __name__ == '__main__':
	main()
