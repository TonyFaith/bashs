#-*- coding:utf-8 -*-
#!bin/bash
data_load="/media/tencent/INFERRR/walk"
data_save="/media/tencent/INFERRR/already"
pic_name="5.walk_picture"
save_video="5.walk.avi"
save_json="5.walk"
for file in $data_load;do
	echo "processing $data_load/$file ..."
	mkdir -p $data_save/$file
	for video in $data_load/$file;do
		cp $data_load/$file/$video $data_save/$file
		./build/examples/openpose/openpose.bin --video $data_save/$file/$video  --hand --write_video $data_save/$file/$save_video --write_json $data_save/$file/$save_json
		ffmpeg -i $data_save/$file/$save_video  -r 50 $data_save/$file/$pic_name/5.walk_%12d.png

