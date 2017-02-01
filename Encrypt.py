"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def encrypt(AnyString):
    newString = ""
    for ch in AnyString:
        if ord(ch) is 65 or ord(ch) is 97:
            newString = newString + "%"

        elif ord(ch) is 69 or ord(ch) is 101:
            newString = newString + "*"

        elif ord(ch) is 73 or ord(ch) is 105:
            newString = newString + "&"

        elif ord(ch) is 79 or ord(ch) is 111:
            newString = newString + "@"

        elif ord(ch) is 85 or ord(ch) is 117:
            newString = newString + "$"


        else:
            newString = newString + ch
        #print (newString)
    return newString
String ='Computer Science Makes the World go round but it doesn\'t make the world round itself!'
NoVowels =  encrypt (String)
print (NoVowels)


"""Write an encryption code that you make up and run it for the variable NoVowels"""
