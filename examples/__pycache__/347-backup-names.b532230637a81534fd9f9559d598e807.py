
# apl-source:1
# مثال 347 — مولد أسماء نسخ احتياطية
# apl-source:2
# Backup name generator
# apl-source:3
# Demonstrates: ترقيم النسخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/347-backup-names.apl
# apl-source:6

# apl-source:7
def اسم_نسخة(جذر_الاسم, رقم):
    # apl-source:8
    return جذر_الاسم + ".bak" + str(رقم)
# apl-source:9

# apl-source:10
def أحدث_رقم(أسماء, جذر_الاسم):
    # apl-source:11
    أعلى = 0
    # apl-source:12
    for اسم in أسماء:
        # apl-source:13
        if اسم.startswith(جذر_الاسم + ".bak"):
            # apl-source:14
            رقم = int(اسم[len(جذر_الاسم) + 4:])
            # apl-source:15
            if رقم > أعلى:
                # apl-source:16
                أعلى = رقم
    # apl-source:17
    return أعلى
# apl-source:18

# apl-source:19
موجودة = ["data.bak1", "data.bak2", "data.bak3", "other.bak1"]
# apl-source:20
تالي = أحدث_رقم(موجودة, "data") + 1
# apl-source:21
print("النسخة التالية:", اسم_نسخة("data", تالي))
# apl-source:22
