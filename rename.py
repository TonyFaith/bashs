import os,sys
import shutil
import pandas as pd

def rename():
    l = os.listdir('tmp')
    l.sort()
    for i in range(len(l)):
        address = 'tmp/' + l[i] + '/tmp_5.walk.mp4'
        newname = 'tmp/' + l[i] + '/5.walk.mp4'
        if os.path.exists(address):
            os.rename(address, newname)
def copytree():
    l = os.listdir('tmp')
    l.sort()
    data = pd.DataFrame(l)
    writer = pd.ExcelWriter('walk.xlsx')
    data.to_excel(writer, 'page1', float_format='%.5f', index=False)
    #for i in range(len(l)):
        #os.makedirs('walk/'+l[i])

def copyvideo():
    l = os.listdir('walk')
    l.sort()
    for i in range(len(l)):
        walkvideo='turn_out/' + l[i] + '/out_1.fingertapping_right.mp4'
        check='fr/'+l[i]+'_fingertapping_right.mp4'
        if os.path.exists(walkvideo):
            shutil.copy(walkvideo,check)
            print(check)
copyvideo()