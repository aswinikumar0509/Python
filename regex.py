import re

s = "AswiniKumar :  A Computer science Engineer"

match = re.search(r'Engineer',s)

print('Start index : ', match.start())
print('End index : ' , match.end())