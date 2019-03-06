from re import sub

def input_chunks(input):
    all_chunks=[]
    prev=''
    for ch in input:
        if prev!=ch:
            prev=ch
            chunk=[]
            chunk.append(ch)
            all_chunks.append(chunk)
        else:
            chunk.append(ch)
    return all_chunks


def decode(string):
    decoded_value=[]
    all_nums =[]
    for ch in string:
         if ch.isdigit():
             all_nums.append(ch)
         else:
             num=int("".join(all_nums)) if all_nums else 1
             decoded_value.append(num * ch)
             all_nums=[]
    return "".join(decoded_value)


def encode(string):
    all_chunks = input_chunks(string)
    if len(all_chunks)== len(string):
        return string
    encoded_value  = "".join([ str(len(chunk))+ chunk[0] if len(chunk) > 1 else chunk[0] for chunk in all_chunks])
    return encoded_value


