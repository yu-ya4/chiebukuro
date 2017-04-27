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
