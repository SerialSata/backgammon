fieldState = [" - "] * 24

def initField ():
    fieldState[23] = "15w"
    fieldState[11]="15b"

def printField ():
    for index in range (13, 25):
        print '{0:3d}'.format (index),
    print
    for index, element in enumerate(fieldState[12:]):
        print '{0:3s}'.format(element),
    print
    print
    print
    for index, element in enumerate(fieldState[11::-1]):
        print '{0:3s}'.format(element),
    print
    for index in range (12, 0, -1):
        print '{0:3d}'.format(index),


initField ()
printField ()