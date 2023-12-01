'''

Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the
string after the colon character and then use the float function
to convert the extracted string into a floating point number.
'''



str = 'X-DSPAM-Confidence:0.8475'

for letter in str :
    target = str.find(":")
    extracted_text = str[target + 1:] #<-- colon is crucial after the 1 str[start: end]

    try:
        float(extracted_text)
        print(extracted_text)
    except ValueError as v:
        print('Developer says: You need to insert a number ')
        print("Python says: ", v)

    another_slice = str[:target]
    print(another_slice)
    break
