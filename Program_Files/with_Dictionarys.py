# Working with dictionaries
'''
Dictionaries contains key, value pairs.
Keys cannot be duplicated.
'''

# Student details with dictionary
Stu_DB = {
    'Name': 'Luna',
    'DOB': '14-Jul-2014',
    'Age':  12,
    'Class': 6,
    'School': 'Govt High School Kumbakonam',
    'Primary Subject': 'Astrophysics'
}

# Access values from a dictionary
print(Stu_DB['Name'], Stu_DB['Primary Subject'])
'''
Stu_DB['2ndry Subject'] - This will throw key error: '2ndry Subject'.
But when you use .get() method to access any key. It produces output if the key is present.
If not it simply returns None.
'''
print(Stu_DB['Name'], Stu_DB.get('2ndry Subject'))

# Supply an optional value to get method.
print(Stu_DB['Name'], Stu_DB.get('2ndry Subject', 'Aviation'))

# Get method doesn't add the new key to the dictionary.
print(Stu_DB)

# Add a new key to dictionary
Stu_DB['Surname'] = "Lovegood"
print(Stu_DB)

# Program to write down phone numbers in English
num_text = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}

phone_num = input("Enter your phone number: ")
op_str = ""

for value in phone_num:
    op_str += num_text.get(value, "XX") + " "

print(op_str)