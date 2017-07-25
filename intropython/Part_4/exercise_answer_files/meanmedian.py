from statistics import mean, median

def meanmedian(mydata):
	return mean(mydata), median(mydata)    # this makes a tuple, even without wrapping in ()

if __name__ == "__main__" :
	my_list=input("Input a series of numbers seperated with spaces:")
	numeric_list=[float(i) for i in my_list.strip().split(" ")] # .strip in case there's a space at the end
	print("The average is: {}\nThe median is: {}".format(*meanmedian(numeric_list)))
    # The * in front of meanmedian in the line above says to unpack the tuple into multiple values
    