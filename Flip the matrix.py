def who_is_bigger(value1, value2, value3, value4):
    if value1 > value2:
        win1 = value1
    else:
        win1 = value2

    if value3 > value4:
        win2 = value3
    else:
        win2 = value4

    if win1 > win2:
        return win1
    else:
        return win2


def flippingMatrix(matrix):
    # Write your code here
    num1 = who_is_bigger(matrix[0][0], matrix[0][3], matrix[3][0], matrix[3][3])
    num2 = who_is_bigger(matrix[1][1], matrix[1][2], matrix[2][1], matrix[2][2])
    num3 = who_is_bigger(matrix[0][1], matrix[0][2], matrix[3][1], matrix[3][2])
    num4 = who_is_bigger(matrix[1][0], matrix[1][3], matrix[2][3], matrix[2][0])
    return num1 + num2 + num3 + num4
