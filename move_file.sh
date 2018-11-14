#-*- coding:utf-8 -*-
#!bin/bash
video_all_path="/media/work/Seagate/videos_fixed_cut"
video_walk_path="/media/work/Seagate/videos_walk_only"
for person in $(ls $video_all_path);do
	person_path=$video_all_path/$person
	person_save_path=$video_walk_path/$person
	mkdir -p $person_save_path
	for video in $(ls $person_path); do
		video_path=$person_path/$video
		if [ "$video" = "out_5.walk.mp4" ];then
			mv   $video_path  $person_save_path 
		fi
	done
done
