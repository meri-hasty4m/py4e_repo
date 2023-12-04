'''

Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the
string after the colon character and then use the float function
to convert the extracted string into a floating point number.
'''

# str = 'X-DSPAM-Confidence:0.8475'
str = 'X-DSPAM-Confidence:jdlkjd'

while True :
    starting_point = str.find(":")
    target_text = str[starting_point + 1:]
    try:
        convert_str_to_float = float(target_text)
        print(convert_str_to_float)
        print(type(convert_str_to_float))
    except ValueError as v:
        print("Error: ", v)
    break
