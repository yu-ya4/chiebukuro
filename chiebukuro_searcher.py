#!/usr/local/bin/python3
# -*- coding: utf-8

import requests
import json
from elasticsearch import Elasticsearch

class ChiebukuroSearcher:
    '''
    Searcher of Yahoo Chiebukuro indexed by Elastic Search
    '''

    def __init__(self, host, index):
        '''
        get the host of elastic search and the index name

        Args:
            host: str
            index: str
        '''
        self.es = Elasticsearch(host, port=9200, timeout=10000)
        self.__index = index

    @property
    def index(self):
        return self.__index

    def search_questions_by(self, query, size, fields):
        '''
        search for questions and get json response

        Args:
            query: str
                検索クエリ
            size: int
                取得する検索結果数
            fields: list[str]
                検索対象にするフィールドの名称からなるリスト
        Returns:
            list[dict[str, str or int]]
            questionのlist
            json形式
        '''

        start = 0
        interval = 1000
        result = []
        while start < size:
            if size < interval:
                interval = size

            json = {"from": start, "size": interval,"query":{"query_string":{"query": query, "fields" : fields}}}
            res = self.es.search(index=self.index, doc_type='questions', body=json)
            questions = res['hits']['hits']
            # if there is no result, break the loop
            if not questions:
                break

            result.extend(questions)
            start += interval

        return result
