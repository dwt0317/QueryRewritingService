# -*- coding:utf-8 -*-
__author__ = 'dwt'


import jieba
import ConfigParser
import os
import config
from gensim.models import word2vec
import numpy as np


class RewritingServiceHandler:
    def __init__(self, cut_all=False):
        self._cut_all = cut_all
        self._model = None
        self.stopwords = set()
        self.load_segment_dict()
        self.load_stopwords()
        self.load_word2vec()

    def rewrite(self, q):
        q = q.decode('utf-8')
        q_list = self.segment(q)
        print q_list
        candi_list = self.embedding(q_list)
        rst = ''
        for pair in candi_list:
            rst += str(pair[0]) + ',' + str(pair[1]) + ' '
        return rst

    '''
        word embedding with gensim word2vec
    '''
    def embedding(self, q_list):
        candi_list = []
        try:
            if self._cut_all:
                for word in q_list:
                    items = self._model.most_similar(word, topn=8)
                    for item in items:
                        candi_list.append([item[0].encode('utf-8'), item[1]])
            else:
                query_vec = np.zeros(200)
                for word in q_list:
                    query_vec += self._model.wv[word]
                items = self._model.wv.similar_by_vector(query_vec, topn=20)
                for item in items:
                    candi_list.append([item[0].encode('utf-8'), item[1]])
        except Exception as e:
            print(repr(e))
        return candi_list

    # Load word2vec model
    def load_word2vec(self):
        print "Loading word2vec model."
        model_path = config.get_config('model', 'model_path')
        self._model = word2vec.Word2Vec.load(model_path)
        print 'Loading word2vec model completed!'

    '''
        Segment with jieba
    '''
    def segment(self, q):
        cut_rst = jieba.cut(q)
        # cut_rst = jieba.cut(q)
        strip_rst = list(set(cut_rst) - self.stopwords)
        return strip_rst

    def load_stopwords(self):
        print 'Loading stopwords...'
        stpwd_dir = config.get_config('corpus', 'stopwords_dir')
        list_file = os.listdir(stpwd_dir)
        for fileName in list_file:
            path = stpwd_dir+fileName
            file = open(path, 'r')
            for line in file:
                self.stopwords.add(line.strip('\n').decode('utf-8'))
        print 'Loading stopwords completed!'

    def load_segment_dict(self):
        print 'Loading user dict...'
        jieba.load_userdict(config.get_config('corpus', 'segment_dict_path'))
        print 'Loading user dict completed!'


if __name__ == '__main__':
    rs = RewritingServiceHandler()
    while True:
        try:
            word = raw_input("请输入：")
            print rs.rewrite(word)
        except Exception as e:
            print(repr(e))


