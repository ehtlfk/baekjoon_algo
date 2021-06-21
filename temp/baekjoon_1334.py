import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input())
N+=1
SN = str(N)
l = len(SN)//2
f_m = SN[:l+len(SN)%2]
# 숫자 문자열 비교 숫자랑 같은 방식으로 진행되지 않고 맨 처음 문자열부터 비교, 하지만 이 경우는 숫자의 길이가 같기 때문에 문자열 비교를 해도 됨
first = ''.join(reversed(SN[:l]))
last = SN[l+len(SN)%2:]

if  first >= last:
    print(''.join([f_m,first]))
# fisrt의 맨 뒤
else:
    num = int(f_m)
    num+=1
    first = str(num)
    last = ''.join(reversed(first[:l]))
    print(''.join([first,last]))