# given a list of integers ([1,3,5,2,8,6])
# find the integers are missing betwen the lowest and highest values ([4,7])

def main():
    my_list = [1, 3, 5, 2, 8, 6]
    my_list.sort()
    print(my_list)
    low = my_list[0]
    high = my_list[-1]
    counter = low + 1

    while counter < high:
        # print(counter)
        counter += 1
        if counter not in my_list:
            print('missing ' + str(counter))


main()
