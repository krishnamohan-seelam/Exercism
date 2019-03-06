def is_armstrong(number):
    if not isinstance(number,int):
        raise TypeError("Only integers are allowed")
    numberx =str(number)
    armstrong_sum = sum([int(x)**len(numberx) for x in numberx])
    return  armstrong_sum == number
