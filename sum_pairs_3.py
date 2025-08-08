'''
close in from both ends
Assuming the list is sorted
'''



import random

SUM = 43

numbers = [random.randrange(35) for i in range(80)]
numbers.sort()
answer =[]
n = len(numbers)

print numbers
print
print 'n:', n
print

i = 0
j = n -1


while i < j:
	if (numbers[i] + numbers[j] < SUM):
		i += 1
	elif (numbers[i] + numbers[j] > SUM):
		j -= 1
	else:
		answer.append((numbers[i], numbers[j]))
		if (numbers[j - 1] == numbers[j]):
			j -= 1
		elif (numbers[i + 1] == numbers[i]):
			i += 1
			while(numbers[j] == numbers[j+1]):
				j += 1
		else:
			i += 1
			j -= 1


print answer
