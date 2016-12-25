import struct

def solve(a):
    b = open(a, 'rb')
    c = b.read()
    d = c
    listN = []
    for i in range(0, len(d), 5):
        number = d[i:i+5]
        if  (number[0] == ord("l")):
            intNumber = struct.unpack_from('i', number, 1)
            print(number," - ",intNumber)
        else:
            number = d[i+1:i+5]
            number = number[::-1]
            intNumber = struct.unpack_from('i', number)
            print(number," - ", intNumber)
        listN.append(intNumber[0])
    return listN
