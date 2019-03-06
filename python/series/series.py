def slices(series, length):
    slice=[]
    index=0
    if not series:
        raise ValueError("Series empty")
    if length <=0 or  length >len(series):
        raise ValueError("input length cannot be less than 1")

    while length <= len(series):
        slice.append(series[index:length])
        index +=1
        length +=1
    return slice
