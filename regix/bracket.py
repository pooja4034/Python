import re
text='The rain in spain'

x=re.findall('[arn]',text)
print(x)