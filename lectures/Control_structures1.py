#Управляющие конструкции: while

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#print(inverted)

#Управляющие конструкции: while-else

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#else:
#    print('Пожалуй')
#    print('хватит )')
#print(inverted)
# Пожалуй
# хватит )
# 32

#Управляющие конструкции: for

#for i in range(1,10 ,2):
#    print(i**2)

#Немного о строках
#text = 'съешь ещё этих мягких французских булок'
#print(len(text)) # 39
#print('ещё' in text) # True
#print(text.isdigit()) # False
#print(text.islower()) # True
#print(text.replace('ещё','ЕЩЁ')) #
#for c in text:
# print(c)

#Срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...