import re
p = re.compile('ab*')
phone = re.compile('[0-9]{4}-[0-9]{4}-[0-9]{4}')

test = re.compile(r'([a-z]+)\s\w+')
m=test.match('eafa sdfs')
print(m.group())
print(m[1])
s = test.search('asdfasd 23 dfasdf')
f = test.findall('asdf 343lkadf.dfs 23232 dsd')

k = phone.match('1232-1231-2312-1233')
print(k.group())


p = re.compile(r'(\b\w+)\s+\1') # r은 raw string을 의미, \b 단어구분자임을 알려주기 위해서 써야됨
t = p.search('Paris in the the spring').group()
print(t)