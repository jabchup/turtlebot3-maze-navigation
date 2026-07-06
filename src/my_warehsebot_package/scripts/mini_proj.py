#!/usr/bin/env python3

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

def check_if_waypoint_blocked(waypoint):
    	# Your logic to determine if the waypoint is blocked
    	# This could involve checking sensor data, obstacle detection, etc.
    	# Return True if blocked, False if not blocked
    	
    		blocked_threshold_y = 0.5
    
    	# For demonstration purposes, let's assume the waypoint is blocked if its y-coordinate is below a threshold
    		if waypoint < blocked_threshold_y:
        		return True
    		else:
        		return False
        		

if __name__== '__main__':
	# CREATE NODE
	rospy.init_node('maze_nav')
	
	# CREATE A CLIENT
	client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
	
	# CLIENT WAIT FOR THE ACTION SERVER TO ON
	client.wait_for_server()
	
	goals = [[4.454,4.069,0.003,-0.003,-0.716,-0.698],
		[-4.592,0.8,0.003,-0.003,-0.717,-0.697],
		[4.430,-4.414,-0.000,-0.000,0.070,-0.998],
		[-4.293,4.453,-0.000,-0.004,0.048,-0.999],
		[-4.40,-4.32,-0.000,-0.004,0.066,-0.998],
		[0.945,-0.724,0.000,-0.004,-0.074,-0.997]
		]
		       
		
	for goal in goals:
	
		# CREATE A WAYPOINT	
		waypoint = MoveBaseGoal()
		
		waypoint.target_pose.header.frame_id = 'map'  # INDICATES THE GOAL IS IN THE MAP COORDINATE FRAME
		
		waypoint.target_pose.pose.position.x = goal[0] # SEND TO move_base SERVER
		waypoint.target_pose.pose.position.y = goal[1]
		#waypoint.target_pose.pose.position.z = goal[2]
		waypoint.target_pose.pose.orientation.x = goal[2]
		waypoint.target_pose.pose.orientation.y = goal[3]
		waypoint.target_pose.pose.orientation.z = goal[4]
		waypoint.target_pose.pose.orientation.w = goal[5]
			
		
		current_waypoint = goal[0]
		is_blocked = check_if_waypoint_blocked(current_waypoint)
	
		if is_blocked:
			offset_x = 0.1   # Example offset values
			offset_y = 0.1
    			
			new_waypoint = [current_waypoint + offset_x, current_waypoint + offset_y]
			waypoint.target_pose.pose.position.x = new_waypoint[0]
			waypoint.target_pose.pose.position.y = new_waypoint[1]
			
			
			
				
	
		client.send_goal(waypoint)
		client.wait_for_result()
