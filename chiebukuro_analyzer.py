#!/usr/local/bin/python3
# -*- coding: utf-8

import sys
sys.path.append('../geosearch')
from cabocha_matcher import CaboChaMatcher

class ChiebukuroAnalyzer():
    def __init__(self, text):
        '''
        Args:
            text: str
                text to analyze
        '''

        self.matcher = CaboChaMatcher()
        self.text = text

    def extract_modifiers(self, target, pattern_file):
        '''
        extract modifiers to the target

        Args:
            target: str
        '''

        sentences = self.extract_sentences(target)
        results = []

        with open(pattern_file) as f:
            pat = f.read()
            pattern = self.matcher.parse_pat(pat)

            for sentence in sentences:
                sen = self.matcher.parse(sentence)
                matched = self.matcher.match(sen, pattern)
                if matched != None:
                    for m in matched:
                        if m != None:
                            for modifier in m:
                                results.append(modifier[0].dictform)


        return results

    def extract_sentences(self, target):
        '''
        記号で区切り， 対象を含む文章を抽出
        Returns:
            list[str]
        '''
        result = []
        syms = ['.', '。', ',', '，', '、', '?', '？', '!', '！']

        for sym in syms:
            text = self.text.replace(sym, " ")

        sentences = text.split()

        for sentence in sentences:
            if target in sentence:
                result.append(sentence)

        return result
