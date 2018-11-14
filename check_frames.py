import os,sys
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

import numpy as np
def takeframenumber(videodir,movitontype):
    l = os.listdir(videodir)
    l.sort()
    aa = []
    nn = 0
    txtname=movitontype+'.txt'
    file = open(txtname, 'w')
    print(movitontype)
    for i in range(len(l)):
        address = videodir+'/' + l[i] + '/'+movitontype

        if os.path.exists(address):
            nn = nn + 1
            output = os.popen(
                'ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 ' + address)
            pp = output.read()
            output.close()
            list_data = l[i] + ' : ' + str(int(pp))
            aa.append(list_data)
            print(list_data)
            file.write(list_data+'\n')
        else:
            print(l[i])

    file.close()
    print(nn)

def txttopng(movtiontype):
    number=[]
    temp=[]
    txtname = movtiontype + '.txt'
    file=open(txtname,'r')
    while 1:
        line = file.readline()
        bb=line[16:-1]
        number.append(bb)
        if not line:
            break
    file.close()
    number=number[:-1]
    for i in number:
        ttt=int(i)
        temp.append(ttt)
    a=np.array(temp)
    plt.hist(a)
    plt.title('1.fingertapping_right video frame number')
    plt.savefig(txtname+' frame number.png')
    plt.show()

def main():
    videodir='output_segment_video'
    movitontype='1.fingertapping_right.mp4'
    #takeframenumber(videodir,movitontype)
    txttopng(movitontype)
main()