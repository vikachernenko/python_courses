import re

my_string = 'my first name is vika.'

res1 = re.search('v...\.$', my_string)  # $-обозначает конец строки
# <re.Match object; span=(17, 22), match='vika.'>
res2 = re.search('v...', my_string)
# <re.Match object; span=(11, 15), match='vika'>

res3 = re.search('^m.*name', my_string)  # ^-символ начала строки
# <re.Match object; span=(0, 7), match='my first name'>
print(str(res1) + '\n' + str(res2) + '\n' + str(res3))
