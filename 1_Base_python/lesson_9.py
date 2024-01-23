import re


regex = re.compile('\s+')

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

result = re.match(r'First', 'First Second Third')
print(result)
print(result.group(0))
result = re.match(r'Second', 'Fisrt Second Third')
print(result)

result = re.search(r'Second', 'Fisrt Second Third')
print(result.group(0))

result = re.findall(r'Second', 'Fisrt Second Third Fisrt Second Third Fisrt Second Third Fisrt Second Third Fisrt Second Third')
print(result)

result = re.split(r'i', 'Fisrt Second Third Fisrt Second Third Fisrt Second Third Fisrt Second Third Fisrt Second Third')
print(result)

result = re.sub(r'First', 'ABC', 'First Second Third First Second Third First Second Third First Second Third Fisrt Second Third')
print(result)