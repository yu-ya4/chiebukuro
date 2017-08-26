
```
cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
questions = cs.search_questions_by('飲む', 100, ['title', 'body'])
all_text = ''
for question in questions:
    all_text += question['_source']['title'] + question['_source']['body']
ca = ChiebukuroAnalyzer(all_text)
```
