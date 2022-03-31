def countingSort(arr):
    arr.sort()
    print(arr)
    newArr = []
    lengthnewArr = len(arr[-1]) + 1

    for idx in range(lengthnewArr):
        if idx - 1 == idx:
            continue
        else:
            number = arr[idx]
            howManyTimes = arr.count(number)
            newArr.insert(number, howManyTimes)
        # unamaquina que detecte la diferencia entre arr[idx] y arr[idx + 1] para poder calcular la cantidad de nros que aparecen "0" veces
    return newArr

print(countingSort([1,2,3,4,5,6,1,12, 2,3, 3,3,12]))