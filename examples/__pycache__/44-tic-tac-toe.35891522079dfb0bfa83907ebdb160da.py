
# apl-source:1
# مثال 44 — لعبة tic-tac-toe
# apl-source:2
# Tic-Tac-Toe Game
# apl-source:3
# Demonstrates: 2D lists, game logic, win detection
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/44-tic-tac-toe.apl
# apl-source:6

# apl-source:7
def دالة_لوحة_فارغة():
    # apl-source:8
    صف = []
    # apl-source:9
    رقم = 0
    # apl-source:10
    while رقم < 3:
        # apl-source:11
        صف = صف + [["-", "-", "-"]]
        # apl-source:12
        رقم = رقم + 1
    # apl-source:13
    return صف
# apl-source:14

# apl-source:15
لوحة_فارغة = دالة_لوحة_فارغة
def دالة_عرض(لوحة):
    # apl-source:16
    for صف in لوحة:
        # apl-source:17
        print("  " + صف[0] + " | " + صف[1] + " | " + صف[2])
        # apl-source:18
        print("  ---|---|---|---")
# apl-source:19

# apl-source:20
عرض = دالة_عرض
def دالة_فاز(لوحة, رمز):
    # apl-source:21
    # صفوف
    # apl-source:22
    for صف in لوحة:
        # apl-source:23
        if صف[0] == رمز and صف[1] == رمز and صف[2] == رمز:
            # apl-source:24
            return True
    # apl-source:25
    # أعمدة
    # apl-source:26
    رقم = 0
    # apl-source:27
    while رقم < 3:
        # apl-source:28
        if لوحة[0][رقم] == رمز and لوحة[1][رقم] == رمز and لوحة[2][رقم] == رمز:
            # apl-source:29
            return True
        # apl-source:30
        رقم = رقم + 1
    # apl-source:31
    # أقطار
    # apl-source:32
    if لوحة[0][0] == رمز and لوحة[1][1] == رمز and لوحة[2][2] == رمز:
        # apl-source:33
        return True
    # apl-source:34
    if لوحة[0][2] == رمز and لوحة[1][1] == رمز and لوحة[2][0] == رمز:
        # apl-source:35
        return True
    # apl-source:36
    return False
# apl-source:37

# apl-source:38
فاز = دالة_فاز
اللوحة = لوحة_فارغة()
# apl-source:39
اللوحة[1][1] = "X"
# apl-source:40
اللوحة[0][0] = "O"
# apl-source:41
اللوحة[2][2] = "X"
# apl-source:42
اللوحة[0][2] = "O"
# apl-source:43
اللوحة[1][2] = "X"
# apl-source:44

# apl-source:45
print("=== tic-tac-toe ===")
# apl-source:46
print("")
# apl-source:47
عرض(اللوحة)
# apl-source:48
print("")
# apl-source:49
print("فاز X؟ " + str(فاز(اللوحة, "X")))
# apl-source:50
print("فاز O؟ " + str(فاز(اللوحة, "O")))
# apl-source:51
