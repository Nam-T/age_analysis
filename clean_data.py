def main():
    f = open("agedetector_group_train.v1.0.txt", "r")
    groups = open("group.txt", "r")
    file_data = open("data.txt", "w")
    group_arr = []
    for x in groups:
        group_arr.append(x.strip('\n'))
    print(len(group_arr))
    for x in f:
        arr = x.strip('\n').split(' ')
        arr_data = []
        label = arr[0]
        LABEL_HASH = {
            '__label__18-24' : '0',
            '__label__55+' : '1',
            '__label__45-54' : '2',
            '__label__25-34' : '3',
            '__label__35-44' : '4'
        }
        arr_data.append(LABEL_HASH[label])
        arr.pop(0)
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