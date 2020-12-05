def main():
    f = open("agedetector_group_train.v1.0.txt", "r")
    file_label = open("label.txt", "w")
    hash = []
    for x in f:
        arr = x.strip('\n').split(' ')
        arr_first = arr[0]
        if arr_first not in hash:
            hash.append(arr_first)
            file_label.write(arr_first + '\n')
    file_label.close()
main()