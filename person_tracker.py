# -*-coding:utf-8-*-
# author: Yifei Chen (dolphinchen@tencent.com)
# date:   2018/04/12
# brief:  track the correct person during video
import os
import sys
import json
import numpy
import scipy
import pylab


'''
given a folder of openpose json frames of sitting pose,
return which purson to track for each frame
'''
def traker_for_hand_gesture(json_file, num_frames, vid_width):
    track_rslt = [-1] * num_frames

    # collect one-person frame cases
    one_person_list = numpy.zeros((0, 2))  # bug detected: array
    for idx in range(num_frames):
        f_idx = '{:012d}'.format(idx)
        f_name = json_file % f_idx
        with open(f_name) as f_json:
            people_list = json.loads(f_json.readline())['people']
            #print(len(people_list))
            if len(people_list) == 1:
                one_person_list = numpy.vstack((one_person_list, people_list[0]['pose_keypoints_2d'][3 : 5]))

    # decide which person to focus for each frame
    if one_person_list.shape[0] > 0:
        target_ave = one_person_list.mean(axis = 0)

    #print("===============================================")
    #print(one_person_list)
    #print(target_ave)
    #print("===============================================")


    for idx in range(num_frames):
        f_idx = '{:012d}'.format(idx)
        f_name = json_file % f_idx
        with open(f_name) as f_json:
            people_list = json.loads(f_json.readline())['people']
            j_closest = 100000
            dist_closest = 100000000000000.

            for j in range(0, len(people_list)):
                neck_coord = numpy.array(people_list[j]['pose_keypoints_2d'][3 : 5])
                if one_person_list.shape[0] == 0:   # always more than one person (or no person)
                    dist = numpy.abs(neck_coord[0] - vid_width / 2.)
                else:                               # there are some frames with only one person
                    dist = numpy.sqrt(numpy.sum((neck_coord - target_ave) ** 2))
                # print('haha', one_person_list,  dist)
                if dist < dist_closest:
                    j_closest = j
                    dist_closest = dist
        track_rslt[idx] = j_closest

    # print out log
    for idx in range(num_frames):
        f_idx = '{:012d}'.format(idx)
        f_name = json_file % f_idx
        log = "@person_tracker::traker_for_hand_gesture. {:04d}: ".format(idx) + str(track_rslt[idx]) + '; '
        with open(f_name) as f_json:
            people_list = json.loads(f_json.readline())['people']
            for j in range(len(people_list)):
                key_point = ', '.join(map(str, people_list[j]['pose_keypoints_2d'][3 : 5])) + '; '
                log += key_point
    #print(log)
            
    return track_rslt
