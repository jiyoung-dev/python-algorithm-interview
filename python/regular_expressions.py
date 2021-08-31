import re

# 정규표현식을 지원하는 re 모듈
# re는 regular expression의 약어이다. re.compile을 사용하여 정규표현식을 컴파일할 수 있다.

# 메타문자
# . ^ $ * + ? { } [ ] \ | ( )

# 1. 문자클래스 []
# 정규 표현식이 [abc]인 경우, a, b, c 중 한개의 문자와 매치를 의미한다.
p1 = re.compile('[abc]')
result1 = p1.findall('ababddeec')
print(result1)  # ['a', 'b', 'a', 'b', 'c']

# \d: 숫자와 매치. [0-9]와 동일한 표현식이다.
# \D: 숫자가 아닌것과 매치. [^0-9]와 동일. (^는 not을 의미함)
expression = "study python 2021-08-31"

result_d = re.findall('(\d)', expression)
print(result_d)  # ['2', '0', '2', '1', '0', '8', '3', '1']

result_D = re.findall('(\D)', expression)
print(result_D)  # ['s', 't', 'u', 'd', 'y', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', '-', '-']

# \s: whitespace 문자와 매치. [ \t\n\r\f\v]와 동일한 표현식.
# \S: whitespace 문자가 아닌것과 매치. [^ \t\n\r\f\v]와 동일한 표현식.
result_s = re.split('(\s)', expression)
print(result_s)  # ['study', ' ', 'python', ' ', '2021-08-31']

result_S = re.split('(\S)', expression)
print(result_d)  # ['2', '0', '2', '1', '0', '8', '3', '1']

# \w: 문자+숫자와 매치. [a-zA-Z0-9_]와 동일.
# \W: 문자+숫자가 아닌 문자와 매치. [^a-zA-Z0-9_]와 동일.
result_w = re.findall('(\w)', expression)
print(result_w)  # ['s', 't', 'u', 'd', 'y', 'p', 'y', 't', 'h', 'o', 'n', '2', '0', '2', '1', '0', '8', '3', '1']
result_W = re.findall('(\W)', expression)
print(result_W)  # [' ', ' ', '-', '-']

# 2. Dot(.)
# a.b의 의미는 a + 모든문자 + b 라는 의미이다. \n을 제외한 모든 하나의 문자가 들어올 수 있다.
p2 = re.compile('a.b')
print(p2.findall('aab ab awerb'))  # ['aab']

p2_2 = re.compile('a...b')
print(p2_2.findall('apppb aggggb'))  # ['apppb']

# 3. 반복(*)
# * 앞에 작성된 문자가 무한대로 반복될 수 있다는 의미
p3 = re.compile('ca*t')
print(p3.findall('caaaat cbt ct'))  # ['caaaat', 'ct']

# 4. 반복(+)
# + 앞에 작성된 문자가 1회 이상 반복될때 사용
p4 = re.compile('ca+t')
print(p4.findall('ct cat caaat'))  # ['cat', 'caaat']

# 5. 반복({m,n}, ?)
# 반복횟수를 제한하는 경우 사용
p5 = re.compile('ca{2}t')  # a가 2번만 반복되야한다는 의미
print(p5.findall('cat caat'))  # ['caat']

p5_2 = re.compile('ca{2,5}t')  # a가 2~5회 반복
print(p5_2.findall('cat caat caaaaat'))  # ['caat', 'caaaaat']


# 정규식을 이용한 문자열 검색

# 1. match
# 문자열의 처음부터 정규식과 매치되는지 조사한다.
p = re.compile('[a-z]+')
print(p.match('3 python'))  # None (정규식에 부합되지 않음)

# 2. search
# 문자열의 전체를 검색해 정규식과 매치되는지 조사.
print(p.search('3 python'))  # <_sre.SRE_Match object; span=(2, 8), match='python'>

# 3. findall
# 정규식과 매치되는 요소들을 리스트로 반환
print(p.findall('life is too short'))  # ['life', 'is', 'too', 'short']

# 4. finditer
# findall과 동일하지만, finditer는 반복가능한 객체를 돌려준다.
print(p.finditer('hello python'))  # <callable_iterator object at 0x00000164DF1C6F28>

# 문자열 바꾸기
# sub 메서드를 사용해 문자열의 일부분을 다른 문자로 쉽게 바꿀수있다. sub(바꿀 문자열, 대상 문자열)
# sub(self, repl: AnyStr, string: AnyStr, count: int = ...) -> AnyStr: ...
P = re.compile('(blue|white|pink)')
print(P.sub('color', 'blue shirt and pink shirt'))  # color shirt and color shirt

# 문자열 바꾸기 예제
# 주민등록번호의 뒷자리를 * 문자로 변경하시오.
data = "kim 990101-1234567"
pat = re.compile('(\d{6})[-]\d{7}')
print(pat.sub("\g<1>-*******", data))  # kim 990101-*******
