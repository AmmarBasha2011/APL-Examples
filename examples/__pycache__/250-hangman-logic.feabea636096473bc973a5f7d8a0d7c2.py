
# apl-source:1
# مثال 250 — منطق لعبة الرجل المشنوق
# apl-source:2
# Hangman logic
# apl-source:3
# Demonstrates: كشف الحروف تدريجيا، عداد أخطاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/250-hangman-logic.apl
# apl-source:6

# apl-source:7
كلمة = "برمجة"
# apl-source:8
تخمينات = ["ب", "م", "ر", "ج", "ة", "x"]
# apl-source:9
مكشوف = []
# apl-source:10
for _ in كلمة:
    # apl-source:11
    مكشوف.append("_")
# apl-source:12

# apl-source:13
أخطاء = 0
# apl-source:14
for حرف in تخمينات:
    # apl-source:15
    if حرف in كلمة:
        # apl-source:16
        for ي in range(len(كلمة)):
            # apl-source:17
            if كلمة[ي] == حرف:
                # apl-source:18
                مكشوف[ي] = حرف
    # apl-source:19
    else:
        # apl-source:20
        أخطاء = أخطاء + 1
    # apl-source:21
    print(" ".join(مكشوف), "(أخطاء:", أخطاء, ")")
# apl-source:22

# apl-source:23
if "_" not in مكشوف:
    # apl-source:24
    print("فزت!")
# apl-source:25
