#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher
from chiebukuro_analyzer import ChiebukuroAnalyzer

if __name__ == '__main__':
    cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    # questions = cs.search_questions_by('\"飲める\" && \"場所\"', 1000000000000, ['title', 'body'])
    questions = cs.search_questions_by('\"飲める\"', 1000000000000, ['title', 'body'])
    all_text = ''
    for question in questions:
        all_text += question['_source']['title'] + question['_source']['body']
    # print(len(questions))
    # all_text = '今日はいい天気だ．飲める？カウンター付きのバーでビールが飲める．ちょっと友達と飲める．楽しいきゅうじつだ。明日からりょこうでうす！￥'
    ca = ChiebukuroAnalyzer(all_text)
    # ca.extract_modifiers('飲める', './pattern')
    # modifiers = ca.extract_modifiers('飲める', './pattern')
    # print(modifiers)

    modifiers_frequences = ca.get_modifiers_frequences('飲める', './pattern')
    print(modifiers_frequences)
