# enumerate는 '열거하다'라는 의미다. list, tuple, string등의 자료형을 입력받으면, 인덱스 값을 포함하는 객체를 돌려준다.
# 어떤 데이터에 순서대로 id를 지정하고 싶은경우 유용하게 사용할수있으며, 딕셔너리와 다르다. 

a = ['hong','gil','dong']
b = list(enumerate(a))
c = dict(enumerate(a))
print(b)
print(c)

'''
[(0, 'hong'), (1, 'gil'), (2, 'dong')]
{0: 'hong', 1: 'gil', 2: 'dong'}
'''
