text = '100000\n1 2\n1 3\n'
for i in range(2, 99999):
    text+=f'{i} {i+2}\n'
text += '10000\n'
for i in range(1,99999):
    text+=f'{i} {i+1}\n'
text+= '3 4\n2 3'
with open('test.txt','w') as f:
    f.write(text)