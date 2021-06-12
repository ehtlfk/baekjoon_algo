n = int(input())
for _ in range(n):
    word = input()
    ret = ''
    if len(word) > 10:
        ret += word[0]
        ret += str(len(word)-2)
        ret += word[-1]
    else:
        ret = word
    print(ret)
    
# 메모리를 더 효율적으로 활용할 수 없을까?
# +=은 매우 느린 연산임, ret를 복사하고 다시 합치기 때문
# python 내부에서 어떻게 처리하는지는 모르겠음                                        
# ret 변수를 선언한 이유는 word 가 string으로 immutable이기 때문

