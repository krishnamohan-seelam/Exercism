def verify(isbn):
    isbn = isbn.replace('-','') 
    if len(isbn) ==10:
        isbn,check_digit = isbn[:9],isbn[9:]
        if ((check_digit.isalpha() and check_digit !='X') or
            (not isbn.isdigit()) ):
            return False
        check_digit =10 if check_digit =='X' else int(check_digit)
        isbn_sum = sum([ int(x)* y  for x,y in list(zip(isbn,range(10,1,-1)))]) +  check_digit
        return isbn_sum % 11 ==0 
    return False
