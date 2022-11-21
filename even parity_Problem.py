import math
def isPalindrome(word):
	if len(word) == 0:
		return False
	else: 
		size = len(word)
		for alphabets in range(math.floor(size/2)):
			if word[alphabets] != word[size-alphabets-1]:
				return False
		return True

handeler = open('input1.txt','r')
handeler=handeler.read()
text = handeler.split('\n')
line_count=0
even_Count=0
odd_Count=0
no_parity_Count=0
palindrome_Count=0
not_Palindrome_Count=0
output_file = open('output1.txt','w')
for line in text:
	msg = None
	msg2 = None
	line_count = line_count + 1
	sp =line.split(' ')
	if '.' not in sp[0]:
		if int(sp[0])%2 == 0:
			msg=sp[0]+' has even parity'
			even_Count = even_Count + 1
		else:
			msg=sp[0]+' has odd parity'
			odd_Count = odd_Count + 1
	else:
		no_parity_Count = no_parity_Count + 1
		msg =sp[0]+ ' cannot have parity' 
	palind = isPalindrome(sp[1])
	if palind:
		msg2 =sp[1]+' is a palindrome'
		palindrome_Count = palindrome_Count + 1
	else:
		msg2 =sp[1]+' not a palindrome'
		not_Palindrome_Count = not_Palindrome_Count + 1
	output = f'{msg} and {msg2}\n'
	output_file.write(output)
output_file.close()

record_file=open('record.txt','w')
even_percent = (even_Count/line_count)*100
odd_percent = (odd_Count/line_count)*100
palin_percent = (palindrome_Count/line_count)*100
not_palind_percent = (not_Palindrome_Count/line_count)*100
no_parity_percent = (no_parity_Count/line_count)*100
record_file.write(f'Percentage of odd parity:{odd_percent}%\n')
record_file.write(f'Percentage of even parity:{even_percent}%\n')
record_file.write(f'Percentage of no parity:{no_parity_percent}%\n')
record_file.write(f'Percentage of palindrome:{palin_percent}%\n')
record_file.write(f'Percentage of non-palindrome:{not_palind_percent}%\n')
record_file.close()