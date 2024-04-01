#String Function/Manipulation

String = "PytHon worlD"
print("Changes all to uppercase : ",String.upper())
print("Changes all to lowercase : ",String.lower())
print(String.swapcase())
print("Changes first letter of first word only change to uppercase : ",String.capitalize())
print("Changes first letter of Each word changes to uppercase : ",String.title())

print('------------------')

String1=" hello world"
print(String1.capitalize())
print(String1.count('o'))
print(String1.endswith('Ld'))
print(String1.startswith(' he'))

print('------------------')

String2="Python world"
print(String2.replace("world","Universe"))

print('------------------')

String3="Abcd"
print(String3.isalpha())

print('------------------')

String4="Abcd123ef"
print(String4.isalpha())

print('------------------')

String5="12345"
print(String5.isdigit())
print(String5.isnumeric())

print("------------------")

String6="五"
print(String6.isdigit())
print(String6.isnumeric())

print('------------------')

String7="abcd123"
print(String7.isalnum())

String8="shj"
print(String8.isalnum())

print('------------------')

String9="Bond007"
print(String9.find('7'))

print('------------------')

String10=" hello world "
print(String10)
print(String10.strip())
print(String10.lstrip())
print(String10.rstrip())
print(len(String10))
