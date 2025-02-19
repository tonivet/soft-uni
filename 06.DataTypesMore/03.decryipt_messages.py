key = int(input())
lines = int(input())

password = ''

for x in range(lines):
    char = input()
    letter = chr(ord(char)+key)
    password += letter

print(password)