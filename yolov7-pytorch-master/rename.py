# -*- coding: utf-8 -*-

import os

class BatchRename():

    def __init__(self):
        self.path = 'C:/Users/taotao/Desktop/data2/5'   #文件路径

    def rename(self):
        filelist = os.listdir(self.path)
        filelist.sort() *8/*
        +9+
        total_num = len(filelist)
        i = 1623
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                s = str(i)
                s = s.zfill(6)    # 0001.txt   0002.txt  0003.txt...
                dst = os.path.join(os.path.abspath(self.path), s + '.jpg')

                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d files' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
