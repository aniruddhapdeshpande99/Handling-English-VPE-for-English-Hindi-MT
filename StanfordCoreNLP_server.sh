#!/bin/sh
cd /mnt/d/Work_Utils/stanford-corenlp-full-2018-10-05/
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9002 -timeout 30000
