from meanmedian import meanmedian

my_list=input("Input a series of numbers seperated with spaces:")
numeric_list=[float(i) for i in my_list.strip().split(" ")]
print("The average is: {}\nThe median is: {}".format(*meanmedian(numeric_list)))