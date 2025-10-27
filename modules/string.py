import string

# string 
# without importing ypu can use it 

# lowercase
# Uppercase 
# sentence -> every word -> capitalized
# sentence -> beginning word -> capitalized

# within a given sentence,
# lowercase -> upper case , upper case -> lower case

content = "hello world"
print(content.capitalize())

left = "level"
right = "LEVEL"
#upper case full conversion
print(right.casefold())

city = "JohanNESburg"
# lowercase -> upper case
# uppercase -> lower case
print(city.swapcase())

proverb = "practice makes man perfect"
print(proverb.upper())
print(proverb.capitalize())
print(proverb.title())



