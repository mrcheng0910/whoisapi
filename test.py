#encoding:utf-8
def quicksort(array):
	
	less= []
	greater =[]
	if len(array)<=1:
		return array
	privot = array.pop()
	for x in array:
		if x<=privot:
			less.append(x)
		else:
			greater.append(x)
	return quicksort(less)+[privot]+quicksort(greater)
	


if __name__ == "__main__":
	array = [3,5,1,1,3,7,8,4,32,2]
	print quicksort(array)
	