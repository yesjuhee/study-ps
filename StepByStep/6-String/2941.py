# 크로아티아 알파벳

ca_length2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
ca_length3 = 'dz='

str = input()
length2 = 0
for word in ca_length2:
    length2 += str.count(word)
length3 = str.count(ca_length3)
print(len(str)-length2-length3)

'''
str(len) - 2개 글자 개수 - 3개 글자 개수
ljes=njak
ddz=z=
6 - 2 - 1
'''
