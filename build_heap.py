# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n= len(data)

    for i in range(n//2-1, -1, -1): #largest integear
        j = i #current node
        while j * 2 + 1 < n: # looking for smallest child
            child = j * 2 + 1
            if child + 1 < n and data[child+1]< data[child]:
                child = child + 1
            if data[child] < data[j]:
                data[j], data[child] = data[child],data[j]
                swaps.append((j, child))
                j = child
            else:
                break





    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_type = input()
    if 'I' in input_type:  
        n = int(input()) 
        data = list(map(int, input().split()))
    elif 'F' in input_type:
        fileName = input()
        path ="./test/" + fileName
        try:
            with open(path,'r', encoding='utf-8') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("error")
            return
        
    else:
        print("error")                                         
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    
    assert len(swaps) <= 4 * n

    ##print(len(swaps))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
