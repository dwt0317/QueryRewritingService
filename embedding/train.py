# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import config

corpus_dir = "E:/Exchange/computing_ad/data/rewrite_corpus/"
project_dir = "D:/Workspaces/SAD/QueryRewritingService/"

# 训练word2vec模型
def train():
    corpus_path = config.get_config('corpus', 'word2vec_txt_path')
    model_path = config.get_config('model', 'model_path')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence(corpus_path)
    model = word2vec.Word2Vec(sentences, size=200)

    #保存模型，供日後使用
    model.save(model_path)

    #模型讀取方式
    # model = word2vec.Word2Vec.load(model_path)


if __name__ == "__main__":
    train()
