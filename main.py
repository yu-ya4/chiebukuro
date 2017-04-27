#!/usr/local/bin/python3
# -*- coding: utf-8

from chiebukuro_searcher import ChiebukuroSearcher

if __name__ == '__main__':
    cs = ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    print(cs.index)
