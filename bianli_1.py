import os
import json
def load(data_dir, random_shuffle=False):
    wrong_person = []
    wrong_open = []
    for game in os.listdir(data_dir):
        print("peocessing file:",game)
        for live in os.listdir(os.path.join(data_dir, game)):
		json_ = os.path.join(data_dir,game,live)
#		print(json_)
		with open(json_,'r') as f1:
			try:
				data = json.load(f1)
			except:
				print(json_)


load("/home/tencent/openpose-1.3.0/a")
