message = "hi"

# Turn these characters into integer / decimal

for character in message:
    print(ord(character))

binary_list = []
for character in message:
    # 0 = pad the left side of the binary string with 0's
    # 8 = The string needs to be 8 digits long
    # b = turn it into binary
    # 1 = 00000001
    binary_list.append(format(ord(character), '08b'))

print(binary_list)

output = ''
for binary_string in binary_list:
    # 2 = base 2 (1's, 0's)
    output += chr(int(binary_string, 2))

print(output)