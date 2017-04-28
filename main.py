#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher
from chiebukuro_analyzer import ChiebukuroAnalyzer

if __name__ == '__main__':
    cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    # questions = cs.search_questions_by('\"飲める\" && \"場所\"', 1000000000000, ['title', 'body'])
    questions = cs.search_questions_by('\"飲む\"', 1000000000000, ['title', 'body'])
    all_text = ''
    for question in questions:
        all_text += question['_source']['title'] + question['_source']['body']
    print(len(questions))

    ca = ChiebukuroAnalyzer(all_text)
    modifiers = ca.extract_modifiers('飲む', './pattern/nomu.txt')
    print(modifiers)
