#-*- coding:utf-8 -*- 
import json
#import matplotlib.pyplot as plt
import cv2

pic_path = "/media/tencent/INFERRR/already/HS20170105001/5.walk_picture/5.walk_000000000000_rendered.png"
json_path = "/media/tencent/INFERRR/already/HS20170105001/5.walk/5.walk_000000000000_keypoints.json"
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread(pic_path)

def int_list(list_str):
	list_int = []
	for digit in list_str:
		list_int.append(int(digit))
	return list_int


with open(json_path) as f_json:
	data = json.load(f_json)
	for people_count in range(len(data['people'])):
 		print("第%d个人的身体节坐标信息:%s"%(people_count,data['people'][people_count]['pose_keypoints_2d']))
	cv2.circle(img,tuple(int_list(data['people'][0]['pose_keypoints_2d'][:2])),6,[255,255,255] ,thickness=-1)
	cv2.putText(img,str(people_count),tuple(int_list(data['people'][0]['pose_keypoints_2d'][:2])),font,1,[255,255,255],1)
	cv2.imwrite("plot_test.png",img)





