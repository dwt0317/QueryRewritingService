# -*- coding:utf-8 -*-
import multiprocessing
import os

import jieba

import config


def load_user_dict():
    print 'Loading user dict...'
    jieba.load_userdict(config.get_config('corpus', 'dict_path'))
    print 'Loading user dict completed!'


def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]


def splitFile(thisList):
    srcPath = "G:\\Exchange\\searchAD\\grad_project\\corpus\\SougouCA_txt"
    desPath = "G:\\Exchange\\searchAD\\grad_project\\corpus\\SougouCA_seg"
    for fileName in thisList:
        path = srcPath + "//" + fileName
        toPath = desPath + "//" + fileName
        print fileName
        if os.path.exists(toPath):
            print 'JDSJFSD'
            continue
        srcfile = open(path, 'r')
        desfile = open(toPath,'w')
        strBuffer = []
        try:
            i=0
            for line in srcfile.readlines():
                i=i+1
                if i%10000 == 0:
                    print i
                seg_line = jieba.cut(line.strip('\n'))
                # print list(seg_line)
                if(len(strBuffer)==5000):
                    desfile.writelines(strBuffer)
                    strBuffer=[]
                else:
                    strBuffer.append(" ".join(list(seg_line)).encode('utf-8')+'\n')
        except Exception, e:
            print e
        finally:
            srcfile.close()
            desfile.flush()
            desfile.close()

if __name__ == '__main__':
    srcPath = "G:\\Exchange\\searchAD\\grad_project\\corpus\\SougouCA_txt"
    listfile = os.listdir(srcPath)
    filelist1, filelist2 = split_list(listfile)
    jieba.load_userdict(config.get_config('corpus', 'dict_path'))
    paras = [filelist1,filelist2]
    processNum = 2
    pool = multiprocessing.Pool(processes=processNum)
    for i in xrange(processNum):
        pool.apply_async(splitFile, (paras[i], ))
    pool.close()
    pool.join()

