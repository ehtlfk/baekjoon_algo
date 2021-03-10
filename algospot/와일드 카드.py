import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

def check(pos1, pos2):
    
    i = pos1
    j = pos2
    while j < len(word) and i < len(wild) and (wild[i] == word[j] or wild[i] == '?'):
        i+=1
        j+=1
    if i == len(wild):
        if j == len(word):
            return 1
        else:
            return 0

    if wild[i]=='*':
        for k in range(len(word)):
            # 음, 넘어가는 거 s+k <len(word)를 넣으면, *로 끝날 때 0을 리턴한다
            if check(i+1 ,j+k):
                return 1
    return 0
for _ in range(int(input())):
    wild = input()
    N = int(input())
    words = []
    wild_list = []

    # pos = 0
    # for i in range(len(wild)):
    #     if wild[i] == '*':
    #         wild_list.append(wild[pos:i+1])
    #         pos = i+1

    # if not wild_list:
    #     wild_list = [wild]         

    for _ in range(N):
        word = input()
        if check(0,0):
            words.append(word)
        
    for w in sorted(words):
        print(w)
