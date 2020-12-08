def main():
    f = open("agedetector_group_test_unlabel.v1.0.txt", "r")
    groups = open("group.txt", "r")
    file_data = open("data_test.txt", "w")
    group_arr = []
    for x in groups:
        group_arr.append(x.strip('\n'))
    print(len(group_arr))
    for x in f:
        arr = x.strip('\n').split(' ')
        arr_data = []
        #print(group_arr)
        for group in group_arr:
            #print(group)
            if group in arr:
                arr_data.append('1')
            else:
                arr_data.append('0')
        i = 1
        for data in arr_data:
            if i < len(arr_data):
                file_data.write(data + ',')
            else:
                file_data.write(data)
            i += 1
        file_data.write('\n')
    file_data.close()
main()