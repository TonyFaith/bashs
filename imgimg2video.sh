# -*-coding:utf-8-*-
#!bin/bash
data_root="/media/tencent/Seagate/180817/180817_rotate_img"
data_save="/media/tencent/Seagate/180817/180817_out_video"
for file1 in $(ls $data_root);do
       file1_path=$data_root/$file1
       file1_save=$data_save/$file1
       mkdir $file1_save
       for file2 in $(ls $file1_path);do
		file2_path=$file1_path/$file2
		file2_save=$file1_save/$file2
		ffmpeg -f image2 -i $file2_path/%12d.png -r 50 $file2_save
	done
done

