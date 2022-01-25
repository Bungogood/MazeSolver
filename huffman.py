#!/usr/bin/env python

"""
"""

__author__ = "Jonathan Good"

from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq, self.char = freq, char
        self.left, self.right = left, right
    
    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:

    def gen_tree(text):
        heap = [Node(text.count(char), char) for char in text]
        heapify(heap)
        while len(heap) > 1:
            a, b = heappop(heap), heappop(heap)
            freq = a.freq + b.freq
            heappush(heap, Node(freq, left=a, right=b))
        return heap[0]
    
    def gen_key(text):
        root = Huffman.gen_tree(text)
        key = {}
        cur = root
        code = 0
        while cur.left != None:
            cur = cur.left
            if cur.char != None:
                pass

    def encoode(text, key):
        out = 1
        for char in text:
            print(key[char])
            out <<= 4
        return out

    def decode(data, root):
        out = []
        cur = root
        for bit in data:
            cur = cur.left if bit == '0' else cur.right
            if cur.char != None:
                out.append(cur.char)
                cur = root
        return "".join(out)
