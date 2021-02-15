# 매우 큰 숫자의 곱셈 반복 연산 테스트
# 검색결과 모듈러 연산이 튀어나왔다.
# 1000000007은 소수이다. 이거 or 1e9+9도 사용한다고 함
# 페르마 소정리, ax = 1 (mod M) x를 구할때, 이는 a^(M-1) = 1 ( mod M ) M = prime number
# a^(M-2) = a^(-1) = x(mod M)인 것을 구할 수 있다고 한다.
from tqdm import tqdm
an = 2
a1 = 21000
k = 1000
for i in tqdm(range(3,k+1))  :
    an= (an*(pow(2,i-2,1000000007)))%1000000007 + (2*an)%1000000007
print(an)