#!/usr/bin/env python 

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

watpoints = [[(5.60237, -1.8963, 0.0),(0.0, 0.0, 0.0, 1.0)]]

def goal_pose(pose):
	goal_pose = MoveBaseGoal()
	goal_pose.target_pose.header.frame_id = 'map'
	goal_pose.target_pose.pose.position.x = pose[0][0]
	goal_pose.target_pose.pose.position.y = pose[0][1]
	goal_pose.target_pose.pose.position.z = pose[0][2]
	goal_pose.target_pose.pose.orientation.x = pose[1][0]
	goal_pose.target_pose.pose.orientation.y = pose[1][1]
	goal_pose.target_pose.pose.orientation.z = pose[1][2]
	goal_pose.target_pose.pose.orientation.w = pose[1][3]

	return goal_pose

def callback():
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server()
	
	while True:
		for pose in watpoints:
			goal = goal_pose(pose)
			client.send_goal(goal)
			client.wait_for_result()

def listener():
	rospy.init_node('bedroom_goal_node')


if __name__ == '__main__':
	listener()
	