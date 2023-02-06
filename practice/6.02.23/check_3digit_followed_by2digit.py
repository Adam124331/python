import re

str1 = '12345 123 89 908 99765'
match = re.search(r'\b\d{3}\s\d{2}\b', str1)
if match:
    print("3 digit followed by 2 digit:", match.group())
else:
    print("No match found.")
    
   output:

3 digit followed by 2 digit: 123 89


"""
summary

The code above uses the re (regular expression) module in Python to search for a pattern in the input string str1. The pattern is defined as follows:

\b - word boundary
\d{3} - three consecutive digits
\s - a whitespace character
\d{2} - two consecutive digits
\b - another word boundary
The re.search function is used to search str1 for the pattern defined above. If a match is found, the function returns a Match object, which is stored in the variable match. The matched string can then be accessed using match.group().

If no match is found, re.search returns None, and a message "No match found." is printed.

'''



