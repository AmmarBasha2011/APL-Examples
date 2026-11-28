
# apl-source:1
# مثال 287 — البحث عن كلمة في شبكة
# apl-source:2
# Word search in a grid
# apl-source:3
# Demonstrates: تراجع رباعي الاتجاهات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/287-word-search.apl
# apl-source:6

# apl-source:7
def ابحث_من(شبكة, كلمة, س, ص, مؤشر, مزارة):
    # apl-source:8
    if مؤشر == len(كلمة):
        # apl-source:9
        return True
    # apl-source:10
    if س < 0 or ص < 0 or س >= len(شبكة) or ص >= len(شبكة[0]):
        # apl-source:11
        return False
    # apl-source:12
    if شبكة[س][ص] != كلمة[مؤشر]:
        # apl-source:13
        return False
    # apl-source:14
    مفتاح = str(س) + "," + str(ص)
    # apl-source:15
    if مفتاح in مزارة:
        # apl-source:16
        return False
    # apl-source:17
    مزارة[مفتاح] = True
    # apl-source:18
    تم_العثور = ابحث_من(شبكة, كلمة, س + 1, ص, مؤشر + 1, مزارة) or ابحث_من(شبكة, كلمة, س - 1, ص, مؤشر + 1, مزارة) or ابحث_من(شبكة, كلمة, س, ص + 1, مؤشر + 1, مزارة) or ابحث_من(شبكة, كلمة, س, ص - 1, مؤشر + 1, مزارة)
    # apl-source:19
    if not تم_العثور:
        # apl-source:20
        مزارة.pop(مفتاح)
    # apl-source:21
    return تم_العثور
# apl-source:22

# apl-source:23
def موجودة(شبكة, كلمة):
    # apl-source:24
    for س in range(len(شبكة)):
        # apl-source:25
        for ص in range(len(شبكة[0])):
            # apl-source:26
            if ابحث_من(شبكة, كلمة, س, ص, 0, {}):
                # apl-source:27
                return True
    # apl-source:28
    return False
# apl-source:29

# apl-source:30
شبكة = [
    # apl-source:31
    ["A", "B", "C", "E"],
    # apl-source:32
    ["S", "F", "C", "S"],
    # apl-source:33
    ["A", "D", "E", "E"]
# apl-source:34
]
# apl-source:35
print("ABCCED:", موجودة(شبكة, "ABCCED"))
# apl-source:36
print("SEE:", موجودة(شبكة, "SEE"))
# apl-source:37
print("ABCB:", موجودة(شبكة, "ABCB"))
# apl-source:38
