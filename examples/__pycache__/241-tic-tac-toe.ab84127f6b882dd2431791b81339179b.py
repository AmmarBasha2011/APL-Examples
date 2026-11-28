
# apl-source:1
# مثال 241 — لعبة إكس أو (منطق)
# apl-source:2
# Tic-tac-toe logic
# apl-source:3
# Demonstrates: لوحة 3x3، فحص الفائز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/241-tic-tac-toe.apl
# apl-source:6

# apl-source:7
def فائز(لوحة):
    # apl-source:8
    خطوط = [
        # apl-source:9
        [لوحة[0], لوحة[1], لوحة[2]],
        # apl-source:10
        [لوحة[3], لوحة[4], لوحة[5]],
        # apl-source:11
        [لوحة[6], لوحة[7], لوحة[8]],
        # apl-source:12
        [لوحة[0], لوحة[3], لوحة[6]],
        # apl-source:13
        [لوحة[1], لوحة[4], لوحة[7]],
        # apl-source:14
        [لوحة[2], لوحة[5], لوحة[8]],
        # apl-source:15
        [لوحة[0], لوحة[4], لوحة[8]],
        # apl-source:16
        [لوحة[2], لوحة[4], لوحة[6]]
    # apl-source:17
    ]
    # apl-source:18
    for خط in خطوط:
        # apl-source:19
        if خط[0] == خط[1] and خط[1] == خط[2] and خط[0] != " ":
            # apl-source:20
            return خط[0]
    # apl-source:21
    return None
# apl-source:22

# apl-source:23
def اطبع_لوحة(لوحة):
    # apl-source:24
    print(لوحة[0] + "|" + لوحة[1] + "|" + لوحة[2])
    # apl-source:25
    print("-+-+-")
    # apl-source:26
    print(لوحة[3] + "|" + لوحة[4] + "|" + لوحة[5])
    # apl-source:27
    print("-+-+-")
    # apl-source:28
    print(لوحة[6] + "|" + لوحة[7] + "|" + لوحة[8])
# apl-source:29

# apl-source:30
لوحة = ["X", "O", "X", "O", "X", "O", "X", " ", " "]
# apl-source:31
اطبع_لوحة(لوحة)
# apl-source:32
print("الفائز:", فائز(لوحة))
# apl-source:33
