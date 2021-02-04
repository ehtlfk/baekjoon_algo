text = '100000\n1 2\n1 3\n'
for i in range(2, 99999):
    text+=f'{i} {i+2}\n'
text += '10000\n'
for i in range(1,100000):
    text+=f'{i} {i+1}\n'

with open('test.txt','w') as f:
    f.write(text)