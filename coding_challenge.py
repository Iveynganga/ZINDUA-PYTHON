import re

def extract_phone_numbers(string):
    phone_numbers = "(123) 456-7890 or (111) 222-3333"
    print(extract_phone_numbers(string))

def extract_email_addresses(string):
    email_addresses = "Please contact info@example.com for assistance"
    print(extract_email_addresses(string))

def replace_email_addresses(string, replacement):
    email_addresses = "Please contact info@example.com for assistance"
    replacement = "REPLACED"
    print(replace_email_addresses(string, "REPLACED"))



phone_numbers = "(123) 456-7890, (111) 222-3333"
pattern = r"(\(\d{3}\) \d{3}-\d{4}), (\(\d{3}\) \d{3}-\d{4})"
          
result = re.search(pattern, phone_numbers)

print(result)

email_addresses = "Please contact info@example.com for assistance"
pattern = r"\w{4}@\w{7}.com"
result = re.search(pattern, email_addresses)

print(result)


email_addresses = " 'Please contact info@example.com for assistance', 'replacement' "
pattern = r"\w{4}@\w{7}.com"
replacement = "REPLACED"
result = re.search(pattern, replacement)

print(result)

