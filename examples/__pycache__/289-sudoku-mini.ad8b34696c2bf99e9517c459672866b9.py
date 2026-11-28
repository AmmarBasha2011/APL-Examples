
# apl-source:1
# مثال 289 — سودوكو مصغر 4x4
# apl-source:2
# Mini sudoku 4x4
# apl-source:3
# Demonstrates: تراجع مع فحص الصف والعمود والمربع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/289-sudoku-mini.apl
# apl-source:6

# apl-source:7
def صالح(شبكة, س, ص, قيمة):
    # apl-source:8
    for ي in range(4):
        # apl-source:9
        if شبكة[س][ي] == قيمة or شبكة[ي][ص] == قيمة:
            # apl-source:10
            return False
    # apl-source:11
    س0 = (س // 2) * 2
    # apl-source:12
    ص0 = (ص // 2) * 2
    # apl-source:13
    for أ in range(س0, س0 + 2):
        # apl-source:14
        for ب in range(ص0, ص0 + 2):
            # apl-source:15
            if شبكة[أ][ب] == قيمة:
                # apl-source:16
                return False
    # apl-source:17
    return True
# apl-source:18

# apl-source:19
def حل(شبكة, موضع):
    # apl-source:20
    if موضع == 16:
        # apl-source:21
        return True
    # apl-source:22
    س = موضع // 4
    # apl-source:23
    ص = موضع % 4
    # apl-source:24
    if شبكة[س][ص] != 0:
        # apl-source:25
        return حل(شبكة, موضع + 1)
    # apl-source:26
    for قيمة in range(1, 5):
        # apl-source:27
        if صالح(شبكة, س, ص, قيمة):
            # apl-source:28
            شبكة[س][ص] = قيمة
            # apl-source:29
            if حل(شبكة, موضع + 1):
                # apl-source:30
                return True
            # apl-source:31
            شبكة[س][ص] = 0
    # apl-source:32
    return False
# apl-source:33

# apl-source:34
شبكة = [
    # apl-source:35
    [1, 0, 0, 4],
    # apl-source:36
    [0, 4, 1, 0],
    # apl-source:37
    [0, 1, 4, 0],
    # apl-source:38
    [4, 0, 0, 1]
# apl-source:39
]
# apl-source:40
if حل(شبكة, 0):
    # apl-source:41
    for صف in شبكة:
        # apl-source:42
        print(صف)
# apl-source:43
else:
    # apl-source:44
    print("لا حل")
# apl-source:45
