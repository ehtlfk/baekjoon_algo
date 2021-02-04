text = '100000\n1 2\n1 3\n'
for i in range(2, 99999):
    text+=f'{i} {i+2}\n'
text += '10000\n'
for i in range(9999):
    text+=f'{i+1} {i+3}\n'
text += f'5 6'
with open('test.txt','w') as f:
    f.write(text)