def merg(a, b):
    result = ""
    if(len(a) == len(b)):
        for i in range(0, len(a)):
            result+=a[i]
            result+=b[i]
    elif(len(a) > len(b)):
        for i in range(0, len(b)):
            result+=a[i]
            result+=b[i]
        result+=a[len(b):]
    else:
        for i in range(0, len(a)):
            result+=a[i]
            result+=b[i]
        result+=b[len(a):]
    return result

if __name__ == "__main__":
    yo = merg('abcsre', 'def')
    print(yo)