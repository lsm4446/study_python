#!/user/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

print("Output #1: I'm excited to learn Python.")

# 두 수를 더한다.
x = 4
y = 5
z = x+y
print("Output #2: Four plus five equals {0:d}.".format(z))

# 두 리스트를 더한다.
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a+b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))

print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))

print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

print("Output #14: {0:s}".format('I\'m enjoying learning Python'))

print("Output #15: {0:s}".format("This is a long string. Without the backslash \
it would run off of the page on the right in the text editor and be very \
difficult to read and edit. By using the backslash you can split the long \
string into smaller strings on seperate lines so that the whole string is easy \
to view in the text editor."))

print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))

print("Output #17: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))

string1="This is a "
string2="short string."
sentence=string1+string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is","very "*4,"beautiful."))
m=len(sentence)
print("Output #20: {0:d}".format(m))

string1="My deliverable is due in May"
string1_list1=string1.split()
string1_list2=string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2="Your,deliverable,is,due,in,June"
string2_list=string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
string2_list[-1]))

print("Output #25: {0}".format(','.join(string2_list)))

string3=" Remove  unwanted characters   from this string.\t\t   \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip=string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip=string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip=string3.strip()
print("Output #29: stript: {0:s}".format(string3_strip))

string4="$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4="$$The unwanted characters have been removed.__---++"
string4_strip=string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

string5="Let's replace the spaces in this sentence with other characters."
string5_replace=string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace=string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))

string6="Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7="Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5="here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list=string5.split()
print("Output #37 (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))

# 문자열 내에 등장하는 패턴의 횟수를 세기
string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"The",re.I)
count=0
for word in string_list:
    if pattern.search(word):
        count+=1
print("Output #38: {0:d}".format(count))

# 문자열 내에서 발견된 패턴 출력하기
string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"(?P<match_word>The)",re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

# 문자열 내 "a"를 "the"로 대체하기
string="The quick brown fox jumps over the lazy dog."
string_to_find=r"The"
pattern=re.compile(string_to_find,re.I)
print("Output #40: {:s}".format(pattern.sub("a",string)))

# 오늘 날짜와 년, 월, 일 요소들을 출력하기
today=date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime=datetime.today()
print("Output #45: {0!s}".format(current_datetime))

# timedelta 함수를 이용하여 새로운 날짜 계산하기
one_day=timedelta(days=-1)
yesterday=today+one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours=timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# 두 날짜 사이의 날짜 차이를 계산하기
date_diff=today-yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

# date 객체를 특정 형식의 문자열로 만들기
print("Output #50: {:s}".format(today.strftime('%m\%d\%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

# 날짜 문자열로부터 특정 형식의 datetime 객체를 생성하기
date1=today.strftime('%m\%d\%Y')
date2=today.strftime('%b %d, %Y')
date3=today.strftime('%Y-%m-%d')
date4=today.strftime('%B %d, %Y')

# 다른 date 형식을 지닌 4가지 문자열에 기반한
# 각각 2종류의 datetime 객체들과 date 객체들
print("Output #54: {!s}".format(datetime.strptime(date1, '%m\%d\%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

# 날짜 부분만 출력하기
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))

# 리스트를 만들기 위해 대괄호를 사용한다.
# len() 함수를 통해 리스트 내 원소의 수를 센다.
# max() 함수와 min() 함수는 최대/최소 값을 찾는다.
# count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다.
a_list=[1,2,3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list=['printer',5,['star','circle',9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))

# 리스트 내 특정 원소에 접근하려면 인덱스 이용하기
# [0]은 첫 번째 원소이다. [-1]은 마지막 원소이다.
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

# 리스트 분할을 사용하여 리스트 원소들의 부분집합 만들기
# 맨 앞부터 분할하는 경우, 최초 인덱스를 생략한다.
# 맨 뒤까지 리스트를 분할하는 경우, 마지막 인덱스는 생략한다.
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

# [:]를 이용하여 리스트 복사하기
a_new_list=a_list[:]
print("Output #77: {}".format(a_new_list))

# + 연산자를 이용하여 2개 이상의 리스트를 병합하기
a_longer_list=a_list+another_list
print("Output #78: {}".format(a_longer_list))

# in과 not in을 이용하여 특정 원소의 리스트 내 포함 여부를 확인하기
a=2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}.".format(a_list))
b=6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}.".format(a_list))

# append() 함수를 이용하여 리스트의 마지막에 원소를 추가하기
# remove() 함수를 이용하여 리스트 내 특정 원소를 제거하기
# pop() 함수를 이용하여 리스트의 마지막 원소를 제거하기
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# reverse() 함수를 이용하여 리스트 반전하기
# 해당 리스트 내에서(인플레이스) 변경이 일어나므로
# 기존 리스트를 변경하지 않고 반전하려면 먼저 사본을 만들어둬야 한다.
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

# sort() 함수를 이용하여 리스트를 인플레이스로 정렬하기
# 이는 리스트가 변경된다는 것을 의미한다.
# 기존 리스트의 변경 없이 리스트를 정렬하려면, 우선 사본을 만든다.
unordered_list=[3,5,1,7,2,8,4,9,0,6]
print("Output #88 {}".format(unordered_list))
list_copy=unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

#s sorted() 함수를 이용하여 리스트들의 특정 위치에 따라 리스트 정렬하기
my_lists=[[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3=sorted(my_lists,key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
