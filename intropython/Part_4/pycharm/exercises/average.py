# This module calculates the average of
# a list

def average():
    my_list=input("Input a series of numbers seperated with spaces:")
    numeric_list=[float(i) for i in my_list.split(" ")]
    print("The average of the given list is:", sum(numeric_list)/len(numeric_list))
    #    help(sum)

if __name__ == "__main__" :
    print("__name__ is set to ", __name__)
    average()

