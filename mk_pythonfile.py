import os, sys

def main(argv):
    directory = argv[1]
    N = argv[2]
    with open(f'{directory}/baekjoon_{N}.py', 'w') as f:
        f.write(
            '''import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline
            ''')
    with open(f'{directory}/baekjoon_{N}.txt', 'w') as f:
        f.write('?')
if __name__ == "__main__":
    main(sys.argv)