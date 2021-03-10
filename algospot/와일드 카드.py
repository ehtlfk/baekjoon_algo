import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

def check(pos1, pos2):
    
    i = pos1
    j = pos2
    # 끝나거나, 끝이 *일 경우 종료 => 별찾기
    if j < len(word) and i < len(wild) and (wild[i] == word[j] or wild[i] == '?'):
        return check(i+1,j+1)
    # 별이 없어?
    if i == len(wild):
        if j == len(word):
            return 1
        else:
            return 0
    # 끝이 별일 경우, * 다음 단어와 일치하는 것을, Word에서 find 없으면, 끝,,
    # * 다음 * 이면 계속 넘어감.
    # 그래서 메모이제이션을 하는구나
    if wild[i]=='*':
        # 음, 넘어가는 거 s+k <len(word)를 넣으면, *로 끝날 때 0을 리턴한다, for문으로 * 뒤 일치하는 단어가 있는지 확인
        # 왜 check(i+1,j+1)을 하지 않을까? *과 j++ 값을 넘겨서 위에 있는 코드를 스킵하고 바로 wild == * 로 접근, 여기서 i+1, j+1을 볼 수 있게 된다.
        if check(i+1 ,j) or (j<len(word) and check(i,j+1)): # check(i,j+1)을 하는 이유는 , j가 거짓일 경우,
            return 1
    return 0
for _ in range(int(input())):
    wild = input()
    N = int(input())
    words = []
    wild_list = []
     

    for _ in range(N):
        word = input()
        if check(0,0):
            words.append(word)
        
    for w in sorted(words):
        print(w)
