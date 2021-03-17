mx = 200001

def bfs(c, b):
    queue = [(c,b)]
    v = [0]*mx

    while queue:
        c,b = queue.pop(0)
        if b == c:
            return v[b]

        c +=v[b]+1
        if 0<= 2*b <= mx:
            if v[2*b] == 0:
                queue.append((c,2*b))
                v[2*b] = v[b]+1
        if 0 <= b-1 <= mx:
            if v[b-1] == 0:
                queue.append((c,b-1))
                v[b-1] = v[b]+1
        if 0<= b+1 <= mx:
            if v[b+1] == 0:
                queue.append((c,b+1))
                v[1+b] = v[b]+1

    return False

print(bfs(11,1))