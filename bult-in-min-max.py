# Script by Matthew Henry for 608

def custom_min(*args):
    #implementing a custom minimum function in response to the query of whether I could
    #only accepts tuples, so inputs must be unpacked
    #I would like to figure out a way to make this function accept lists as well as tuples
    #overloading the function with an alternative for lists didn't seem to work.
    min = args[0]
    for i in args:
        if i < min:
            min = i
    return min



def main():
    data1 = [12, 27, 36]
    data2 = [12.3, 45.6, 9.7]
    data3 = ['yellow', 'red', 'orange']
    data4 = [13.5, -3, 7]
    data5 = ['yellow', 'red', 'orange', 'blue', 'green']
    data6 = [15, 9, 27, 14]
    print(f'Max of {data1} is {max(data1)}')
    print(f'Max of {data2} is {max(data2)}')
    print(f'Max of {data3} is {max(data3)}')
    print(f'Max of {data4} is {max(data4)}')
    print(f'Max of {data5} is {max(data5)}')
    print(f'Max of {data6} is {max(data6)}')
    print(f'Min of {data1} is {min(data1)}')
    print(f'Min of {data2} is {min(data2)}')
    print(f'Min of {data3} is {min(data3)}')
    print(f'Min of {data4} is {min(data4)}')
    print(f'Min of {data5} is {min(data5)}')
    print(f'Min of {data6} is {min(data6)}')
    print(f'Testing custom min function.  Min of {data1} is {custom_min(*data1)}')

if __name__ == "__main__":
    main()