# 배열의 최대값의 인덱스는?

> find함수를 사용하면 됨, 하지만 예전에 find 함수 남용하다가 시간초과 걸린 트라우마로...

```python

def dfs(study):
    if study == 'death':
        return
    for l in range(len(learnings)):
        if visited[l] == 0:
            dfs(l)
```
