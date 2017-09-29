import datetime

def print_time(my_path):
    "Receives my path and combines with time"
    a=datetime.datetime.now()
    print('Execution time: {0}'.format(a))
    print(my_path)
    return