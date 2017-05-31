# -*- coding: utf-8 -*-

import logging
import os

import jieba

import config


def segment():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    resource_dir = config.get_config('corpus', 'resource_dir')
    jieba.set_dictionary(resource_dir+"/dict/dict.txt.big")

    # load stopwords set
    stop_word_set = set()
    stpwdPath = resource_dir+'/stopwords/'
    file_list = os.listdir(stpwdPath)
    for fileName in file_list:
        path = stpwdPath + fileName
        f = open(path, 'r')
        for line in f:
            stop_word_set.add(line.strip('\n').decode('utf-8'))

    texts_num = 0
    corpus_dir = "E:/Exchange/computing_ad/data/rewrite_corpus/"
    output = open(corpus_dir+'wiki_seg_test.txt', 'w')
    with open(corpus_dir+'wiki_zh_tw.txt', 'r') as content:
        for line in content:
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stop_word_set:
                    output.write(word.encode('utf-8') + ' ')
            output.write('\n')
            texts_num += 1
            if texts_num == 10:
                return
            if texts_num % 10000 == 0:
                logging.info("已完成前 %d 行的断词" % texts_num)
    output.close()

if __name__ == '__main__':
    segment()
