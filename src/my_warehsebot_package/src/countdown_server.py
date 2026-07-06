#!/usr/bin/env python3

import rospy
import actionlib
import time
import my_warehsebot_package.msg

class CountdownServer():
	
	# Create Feedback and Result Messages
	def __init__(self):
		# Create server
		self._action_server = actionlib.SimpleActionServer('countdown', my_warehsebot_package.msg.CountdownAction, self.execute_callback, False)
	
		# Start server
		self._action_server.start()
		rospy.loginfo('Starting Action Server')
		
	# Callback function to RUN AFTER ACK A GOAL from server
	def execute_callback(self, goal_handle):
		rospy.loginfo('Starting Countdown')
		
		# Initiate the feedback message current num to the action request starting num
		feedback_num = my_warehsebot_package.msg.CountdownFeedback()
		feedback_msg.current_num = goal_handle.starting_num
		
		while feedback_msg.current_num > 0:
		
			# Publish feedback
			self._action_server.publish_feedback(feedback_msg)
		
			# Print log message
			rospy.loginfo('Feedback: {0}'.format(feedback_msg.current_num))
		
			# Decrement feedback message current_num
			feedback_msg.current_num = feedback_msg.current_num - 1
		
			# Wait a second before counting down next number
			time.sleep(1)
		
		self._action_server.publish.feedback(feedback_msg)
		rospy.loginfo('Feedback: {0}'.format(feedback_msg.current_num))
		rospy.loginfo('Done')
	
		result = my_warehsebot_package.msg.CountdownResult()
		result.is_finished = True
	
		# Indicate the goal is successful
		self._action_server.set_succeeded(result)

def main(arg=None):
	
	# Init ROS and give node a name
	rospy.init_node('countdown_server')
	countdown_server = CountdownServer()
	rospy.spin()
	
if __name__ == '__main__':
	main()
	
	
