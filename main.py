#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher

if __name__ == '__main__':
    cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    questions = cs.search_questions_by('\"場所知りませんか\"', 3, ['body'])
    print(questions)
