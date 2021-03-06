#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (C) 2021 Fumiya Ogura, Ryuichi ueda. All rights reserved.

import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('count_up',String, queue_size=1)
rate = rospy.Rate(0.5)  #表示間隔
n = 0


while not rospy.is_shutdown():
    count = 0
    with open('scripture.txt') as f:
        for line in f:
            count += 1
    with open('scripture.txt') as f:
        str = f.readlines()[n-1]
    if n >= count:
        n = 0
    n += 1
    pub.publish(str.rstrip('\n'))
    rate.sleep()

