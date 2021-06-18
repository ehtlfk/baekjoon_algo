def solution(A):
    # write your code in Python 3.6
    num = [0]*100001

    for i in range(len(A)):
        if A[i]>0:
            num[A[i]] = 1
    for j in range(1,100001):
        if not num[j]:
            return j


# 양의 정수 중에서 A에 포함되지 않는 제일 작은 양의 정수를 찾는 문제, 
# A의 길이는 100,000
# 정수의 범위는 -1,000,000 ~ 1,000,000 이므로 백만까지 배열을 다 채울 수 없기 때문에 1000001 출력은 생각안해도 된다.

# 위 코드에서 개선점은 굳이 메모리를 1000001개 쓸 필요가 없다. max값을 구해서 max값 만큼 돌리면 된다.