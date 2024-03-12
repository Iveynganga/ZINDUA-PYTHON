import re

def extract_phone_numbers(string):
    pattern = r"(\(\d{3}\)\s\d{3}-\d{4})"
    return re.findall(pattern, string)

def extract_email_addresses(string):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(pattern, string)

def replace_email_addresses(string, replacement):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.sub(pattern, replacement, string)

phone_numbers = "(123) 456-7890, (111) 222-3333"
print(extract_phone_numbers(phone_numbers))

email_addresses = "Please contact info@example.com for assistance"
print(extract_email_addresses(email_addresses))

email_addresses_to_replace = "Please contact info@example.com for assistance"
replacement = "REPLACED"
print(replace_email_addresses(email_addresses_to_replace, replacement))




