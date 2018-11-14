video_input_path="/media/work/Seagate/videos_158_fixed"
img_output_path="/media/work/Seagate/images_158_2"
for person in $(ls $video_input_path); do
	person_path=$video_input_path/$person
	person_save_path=$img_output_path/$person
	mkdir -p $person_save_path
	for video in $(ls $person_path); do
		video_path=$person_path/$video
		video_save_path=$person_save_path/$video
		mkdir -p $video_save_path
		ffmpeg -i $video_path -qscale 0 -intra -r 50 $video_save_path/%5d.jpg
	done
done
