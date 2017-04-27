#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher

if __name__ == '__main__':
    cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    questions = cs.search_questions_by('飲む', 100000000000000000, ['body'])
    for question in questions:
        print(question['_source']['title'] + question['_source']['body'])
    print(len(questions))
