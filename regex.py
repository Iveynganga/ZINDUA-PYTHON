import re

text = "+254-234-098-134"
pattern = r"\+\d{3}-\d{3}-\d{3}-\d{3}"

result = re.search(pattern,text)

print(result)