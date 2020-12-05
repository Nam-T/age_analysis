def getList(dict):
    file_group = open("group.txt", "w")
    list = []
    for key in dict.keys():
        if dict[key] < 50: continue
        list.append(key)
        file_group.write(key + '\n')
    file_group.close()

    return list

def main():
    f = open("agedetector_group_train.v1.0.txt", "r")
    hash = {}
    for x in f:
        arr = x.strip('\n').split(' ')
        arr.pop(0)
        for group in arr:
            if group not in hash:
                hash[group] = 1
            else:
                hash[group] = hash[group] + 1
    print(getList(hash))

main()