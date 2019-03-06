def square_of_sum(count):
    if not isinstance(count,int):
        raise TypeError("Invalid Type,only integers allowed")
    return sum(range(1,count+1)) **2

def sum_of_squares(count):
    if not isinstance(count,int):
        raise TypeError("Invalid Type,only integers allowed")
    return sum([number**2 for number in range(count+1)])

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
