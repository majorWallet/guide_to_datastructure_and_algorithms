def print_only_num(array):
    for i in array:
        if str(type(i)) == "<class 'int'>":
            print(i)
        elif str(type(i)) == "<class 'list'>":
            print_only_num(i)
    return None

array = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8,
        [9, 10, 11,
            [12, 13, 14]
        ]
    ],
    [15, 16, 17, 18, 19,
        [20, 21, 22,
            [23, 24, 25,
                [26, 27, 29]
            ], 30, 31
        ], 32
    ], 33
]
print_only_num(array)