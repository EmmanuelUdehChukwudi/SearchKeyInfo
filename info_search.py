import re

text = """John Doe was born on January 15, 1990, in New York City. 
His email address is john.doe90@example.com, and his phone number is (123) 456-7890. He works at ExampleCorp, 
and his employee ID is EMP12345. He started working there on March 1, 2015.
The company's website is https://www.examplecorp.com, 
and its main office is located at 123 Example Street, NY 10001"""

name = re.search(r'[A-Z][a-z]+\s[A-Z][a-z]+', text)
print(name.group())  
birthdate = re.search(r'[A-Za-z]+\s\d{1,2},\s\d{4}', text)
print(birthdate.group())
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(email.group())
phone = re.search(r'\(\d{3}\)\s\d{3}-\d{4}', text)
print(phone.group()) 
employee_id = re.search(r'EMP\d+', text)
print(employee_id.group())
website = re.search(r'https?://[A-Za-z0-9./]+', text)
print(website.group())