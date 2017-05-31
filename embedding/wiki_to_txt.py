# -*- coding: utf-8 -*-
import logging
import sys
from gensim.corpora import WikiCorpus
import opencc

dir_path = "E:/Exchange/computing_ad/data/rewrite_corpus/"


def read_sample():
    i = 0
    with open(dir_path + "wiki_seg.txt", 'r') as f:
        for line in f:
            print line + '\n'
            if i == 0:
                return
            i += 1


# xml to txt
def wiki_to_txt():
    # if len(sys.argv) != 2:
    #     print("Usage: python3 " + sys.argv[0] + " wiki_data_path")
    #     exit()
    corpus_path = dir_path + "zhwiki-20170501-pages-articles1.xml.bz2"
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    texts_num = 0

    output = open(dir_path + "wiki_texts1.txt", 'w')
    wiki = WikiCorpus(corpus_path, lemmatize=False, processes=15, dictionary={})
    i = 0
    for text in wiki.get_texts():
        output.write(" ".join(text) + "\n")
        i += 1
        if i % 10000 == 0:
            logging.info("Saved " + str(i) + " articles")
    output.close()
    logging.info("Finished Saved " + str(i) + " articles")


def convert2simple():
    cc = opencc.OpenCC('t2s')
    for i in range(1, 5):
        src_file = dir_path + "wiki_texts" + str(i) + ".txt"
        des_file = dir_path + "wiki_simple" + str(i) + ".txt"
        des_f = open(des_file, 'w')
        with open(src_file, 'r') as f:
            for line in f:
                # print line.decode('utf-8')
                content = cc.convert(line.decode('utf-8'))
                print content
                des_f.write(content.encode('utf-8') + '\n')
        des_f.close()
        print str(i) + " finished."

if __name__ == "__main__":
    # wiki_to_txt()
    read_sample()
    # convert2simple()