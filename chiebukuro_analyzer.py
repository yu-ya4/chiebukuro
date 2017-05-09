#!/usr/local/bin/python3
# -*- coding: utf-8

import sys
import glob
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

    def extract_modifiers(self, target, pattern_dir):
        '''
        extract modifiers to the target

        Args:
            target: str
                extract modifiers to this target
            pattern_dir: str
                read pattern files from this directory
        Returns:
            list[list[str]]
                modifiers
        '''

        text = self.extract_sentences(target)
        results = []
        pattern_files = glob.glob(pattern_dir + '/*.txt')
        patterns = []

        # read patterns
        for pattern_file in pattern_files:
            with open(pattern_file) as f:
                pat = f.read()
                patterns.append(self.matcher.parse_pat(pat))

        sentences = self.matcher.parse(text)
        for pattern in patterns:
            # matched: list[list[list[Token]]]
            matcheds = self.matcher.match(sentences, pattern)
            if matcheds != None:
                for matched in matcheds:
                    if matched != None:
                        modifier = []
                        # return results as [['ちょっと'], ['カウンター', 'で']]
                        for m in matched:
                            modifier.append(m[0].dictform)
                        results.append(modifier)

        return results

    def get_modifiers_frequences(self, target, pattern_dir):
        '''
        get modifiers frequences got by extract_modifiers()

        Args:
            target: str
                extract modifiers to this target
            pattern_dir: str
                read pattern files from this directory
        Returns:
            dict{str: int}
                ex. {'カウンターで': 1, 'ちょこっと': 2, 'ゆっくり': 18}
        '''

        modifiers = self.extract_modifiers(target, pattern_dir)
        modifiers_frequences = {}

        for modifier_list in modifiers:
            modifier = ''
            for m in modifier_list:
                modifier += m

            if modifier not in modifiers_frequences:
                modifiers_frequences[modifier] = 1
            else:
                modifiers_frequences[modifier] += 1

        return modifiers_frequences

    def extract_sentences(self, target):
        '''
        記号で区切り， 対象を含む文章を抽出
        抽出した文章を"．"でつなげた文字列を返す．
        Returns:
            str
        '''
        result = ''
        syms = ['.', '。', ',', '，', '、', '?', '？', '!', '！', '．', '，']
        text = self.text
        for sym in syms:
            text = text.replace(sym, " ")

        sentences = text.split()

        for sentence in sentences:
            if target in sentence:
                result += sentence + '．'

        return result
