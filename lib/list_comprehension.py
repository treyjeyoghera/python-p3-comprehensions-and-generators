#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n%2 == 0]

def make_exclamation(sentence_list):
    return [sentence_list + '!'for sentence_list in sentence_list]