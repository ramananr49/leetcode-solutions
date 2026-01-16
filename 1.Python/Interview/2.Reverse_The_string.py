"""
#Write a program to reverse the string
"""

str = "Ramanan Ramasamy"
print(str[::-1])  #ymasamaR nanamaR

"""
write the program to reverse the string without using in built methods
"""

def reverse_string(text):
    temp = ""
    for i in range(len(text)-1, -1, -1):
        temp += text[i]
    return temp

print(reverse_string(str))

"""
write the program to reverse the word only not the complete sentence
"""
input = "Ramanan Ramasamy"
ouput = "nanamaR ymasamaR"

res = []
text_list = input.split(" ")
print(text_list)
for i in text_list:
    res.append(reverse_string(i))

print(" ".join(res))