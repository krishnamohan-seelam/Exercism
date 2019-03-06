def raindrops(number):
    wordmap = { 3:'Pling', 5:'Plang',7:'Plong'}
    factors = [i for i in range(1, number + 1)  if number % i == 0 and i in[3,5,7]]
    if factors:
        result = "".join([wordmap[key] for key in factors])
        return result
    return str(number)

