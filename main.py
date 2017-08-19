#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher
from chiebukuro_analyzer import ChiebukuroAnalyzer
from collections import Counter

if __name__ == '__main__':
    # cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    # questions = cs.search_questions_by('\"飲める\" && \"場所\"', 1000000000000, ['title', 'body'])
    # questions = cs.search_questions_by('飲む場所', 100, ['title', 'body'])
    # questions = cs.search_questions_by_category('お酒、ドリンク', 230000)
    #
    # all_text = ''
    # i=0
    # with open('./questions_お酒、ドリンク.txt', 'w') as f:
    #     for question in questions:
    #         i +=1
    #         q = question['_source']['title'] + question['_source']['body'] + '\n'
    #         f.write(q)
    #         all_text += q
    # print(i)
    # print(len(questions))
    # all_text = '今日はいい天気だ．飲める？カウンター付きのバーでビールが飲める．ちょっと友達と飲める．楽しいきゅうじつだ。明日からりょこうでうす！￥'
    # print(all_text)
    # exit()
    # with open('./questions_飲食店.txt', 'r') as f:
    #     all_text += f.read()
    # #
    # with open('./questions_お酒、ドリンク.txt', 'r') as f:
    #     all_text += f.read()
    # #
    # exit()
    # all_text = '今日はいい天気だ．飲める？カウンター付きのバーでビールが飲める．ちょっと友達と飲める．\
    # # 楽しいきゅうじつだ。明日からりょこうでうす！大勢で飲む．ひとりで飲む．１人で飲む．ゆっくり飲みたい￥'

    # ca = ChiebukuroAnalyzer(all_text)
    # modifiers = ca.extract_modifiers('飲', './pattern')
    #
    # modifiers_frequences = ca.get_modifiers_frequences('飲', './pattern')
    # fw1 = open('../act-geo-matrix/actions/20170816/chiebukurお酒、ドリンク.txt', 'w')
    # fw2 = open('../act-geo-matrix/actions/20170816/chiebukuroお酒、ドリンク-freq.txt', 'w')
    #
    # for key, val in sorted(modifiers_frequences.items(), key=lambda x:x[1], reverse=True):
    #     fw1.write(key + '\n')
    #     fw2.write(key + ' ' + str(val) + '\n')
    #
    # fw1.close()
    # fw2.close()
    # print(22)
    # all_text = ''
    # # with open('./questions_飲食店.txt', 'r') as f:
    # #     all_text += f.read()
    # with open('./questions_お酒、ドリンク.txt', 'r') as f:
    #     all_text += f.read()
    # print(len(all_text))
    # ca = ChiebukuroAnalyzer(all_text.replace('\n', ''))
    # # modifiers = ca.extract_modifiers('飲', './pattern')
    #
    # modifiers_frequences = ca.get_modifiers_frequences('飲', './pattern')
    # fw1 = open('../act-geo-matrix/actions/20170816/chiebukuro.txt', 'w')
    # fw2 = open('../act-geo-matrix/actions/20170816/chiebukuro-freq.txt', 'w')
    #
    # for key, val in sorted(modifiers_frequences.items(), key=lambda x:x[1], reverse=True):
    #     fw1.write(key + '\n')
    #     fw2.write(key + ' ' + str(val) + '\n')
    #
    # fw1.close()
    # fw2.close()
    # exit()

    all_text = ''
    with open('./questions_飲食店.txt', 'r') as f:
        all_text += f.read()
    with open('./questions_お酒、ドリンク.txt', 'r') as f:
        all_text += f.read()

    print(len(all_text))
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[0:10000000])
    modifiers_frequences_1 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_1_counter = Counter(modifiers_frequences_1)

    print(1)
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[10000000:20000000])
    modifiers_frequences_2 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_2_counter = Counter(modifiers_frequences_2)

    print(1)
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[20000000:30000000])
    modifiers_frequences_3 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_3_counter = Counter(modifiers_frequences_3)

    print(1)
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[30000000:35000000])
    modifiers_frequences_41 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_41_counter = Counter(modifiers_frequences_41)

    print(1)
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[35000000:40000000])
    modifiers_frequences_42 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_42_counter = Counter(modifiers_frequences_42)

    print(1)
    ca = ChiebukuroAnalyzer(all_text.replace('\n', '')[40000000:50000000])
    modifiers_frequences_5 = ca.get_modifiers_frequences('飲', './pattern')
    modifiers_frequences_5_counter = Counter(modifiers_frequences_5)

    print(2)

    modifiers_frequences = dict(modifiers_frequences_1_counter + modifiers_frequences_2_counter + modifiers_frequences_3_counter + modifiers_frequences_41_counter + modifiers_frequences_42_counter + modifiers_frequences_5_counter)
    fw1 = open('../act-geo-matrix/actions/20170816/chiebukuro.txt', 'w')
    fw2 = open('../act-geo-matrix/actions/20170816/chiebukuro-freq.txt', 'w')

    for key, val in sorted(modifiers_frequences.items(), key=lambda x:x[1], reverse=True):
        fw1.write(key + '\n')
        fw2.write(key + ' ' + str(val) + '\n')

    fw1.close()
    fw2.close()
    exit()
