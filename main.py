
# a = {"1","2","3","4","4"}
# a.add('5')
# a.remove('5')
# print(a)
# a = 'привет как дела'
# q = a.split(' ')
# print(q)
text = input('ведите текст ')
text = text.lower()
punction = ['.','"',"'",',','!','?']
for i in  punction:
    text = text.replace(i,"")
words = text.split()
word_feq = {}
for i in words:
    if i in word_feq:
        word_feq [i] += 1
    else:
        word_feq [i] = 1
print ('количевство разных слов:',len(set(words)))
print('чистота слов')
for word,count in word_feq.items():
    print(f'{word}: {count}')