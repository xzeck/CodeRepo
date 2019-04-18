def DisplayRepeated(InputElements):
    _size = len(InputElements)
    Repeated = []
    for i in range(_size): 
        k = i + 1  
        for j in range(k, _size): 
            if InputElements[i] == InputElements[j] and InputElements[i] not in Repeated: 
                Repeated.append(InputElements[i])

    return Repeated



def CallFunction():
    InputElements = ["Something", "Something2", "Something3", "Something4", "Repeating", "Repeating"]
    Res = DisplayRepeated(InputElements)    
    print(Res)

CallFunction()
