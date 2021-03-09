import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

def check(word1, word2):
    cnt = 0
    i = 0
    while i <len(word2):
        cnt = 0
        for j in range(len(word1)):
            if word1[j] == word2[i] or word1[j] =='?':
                cnt+=1
                i+=1
                continue
            else:
                break
        if cnt == len(word1):
            return i
        i+=1
    return -1
for _ in range(int(input())):
    wild = input()
    N = int(input())
    words = []

    s_wild = wild.split('*')

    for _ in range(N):
        word = input()
        i = 0
        for ch in s_wild:
            if not ch:
                continue
            
            temp = check(ch, word[i:])
            i = temp+1
            if temp != -1:
                continue
            else:
                break
        else:
            
            words.append(word)
    for w in sorted(words):
        print(w)
