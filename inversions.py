import sys

testArray1 = [1,2,4,3,5,6]
testArray2 = [6,5,4,3,2,1]
testArray3 = [1,2,4,3,5]
testArray4 = [2,1,3,4,5]
testArray5 = [6,1,3,3,5,2]
testArray6 = [2,1,3,4]



def sort(inputList, inversionCount):
	if len(inputList) <= 1:
		return inputList, inversionCount
	(left, inversionCount) = sort(inputList[:len(inputList)/2], inversionCount)
	(right, inversionCount) = sort(inputList[len(inputList)/2:], inversionCount)

	#print(left)
	#print(right)

	(mergedList, inversionCount) = merge(left, right, inversionCount)

	return mergedList, inversionCount

	
def merge(left, right, inversionCount):
	outputList = []
	#reverse the lists so that when we pop(), it pops from the correct side (the beginnning of the list in its un-reverse order) 
	left.reverse()
	right.reverse()

	#reverse again so we are starting at the beginning of each list
	for leftItem in left[::-1]:
		for rightItem in right[::-1]:
			#print "left item is " + str(leftItem)
			#print "right item is " + str(rightItem)
			if leftItem <= rightItem:
				outputList.append(left.pop())
				#print "outputList " + str(outputList)
				#print "left is "
				#print left
				break
			else:
				inversionCount += len(left)
				outputList.append(right.pop())
				#print "outputList " + str(outputList)
				#print "inversionCount " + str(inversionCount)


	#picking pp residual items left in either list (the highest value will be left behind otherwise)
	if len(left) > 0:
		#inversionCount += len(left)
		#print "inversionCount " + str(inversionCount)
		for item in left[::-1]: outputList.append(item)
	if len(right) > 0:
		for item in right[::-1]: outputList.append(item)

	return outputList, inversionCount




f = open('inversionSet.txt', 'r')
numbers = []
for line in f:
	numbers.append(int(line))

(sortedList, count) = sort(numbers,0)
print count
#print(sort(numbers, 0))

def testSort():
	print("testArray5")
	print(sort(testArray5, 0))
	print("testArray3")
	print(sort(testArray3, 0))
	print("testArray6")
	print(sort(testArray6, 0))

def testMerge():
	print "2,4 and 1,3"
	print(merge([2,4],[1,3]))
	print "1,3,5 and 2,4"
	print(merge([1,3,5],[2,4]))
	print "4,5,6 and 1,2,3"
	print(merge([4,5,6],[1,2,3]))
	print("4,5,7 and 1,2,6")
	print(merge([4,5,7],[1,2,6]))

#testSort()



