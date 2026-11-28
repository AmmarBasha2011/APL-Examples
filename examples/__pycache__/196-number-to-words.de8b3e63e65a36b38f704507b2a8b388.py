
# apl-source:1
# مثال 196 — تحويل الأرقام إلى كلمات عربية
# apl-source:2
# Numbers to Arabic words
# apl-source:3
# Demonstrates: قواميس، بناء نصوص شرطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/196-number-to-words.apl
# apl-source:6

# apl-source:7
آحاد = {0: "صفر", 1: "واحد", 2: "اثنان", 3: "ثلاثة", 4: "أربعة", 5: "خمسة", 6: "ستة", 7: "سبعة", 8: "ثمانية", 9: "تسعة", 10: "عشرة", 11: "أحد عشر", 12: "اثنا عشر", 13: "ثلاثة عشر", 14: "أربعة عشر", 15: "خمسة عشر", 16: "ستة عشر", 17: "سبعة عشر", 18: "ثمانية عشر", 19: "تسعة عشر"}
# apl-source:8
عشرات = {2: "عشرون", 3: "ثلاثون", 4: "أربعون", 5: "خمسون", 6: "ستون", 7: "سبعون", 8: "ثمانون", 9: "تسعون"}
# apl-source:9

# apl-source:10
def بالكلمات(ن):
    # apl-source:11
    if ن < 20:
        # apl-source:12
        return آحاد[ن]
    # apl-source:13
    ع = ن // 10
    # apl-source:14
    أ = ن % 10
    # apl-source:15
    if أ == 0:
        # apl-source:16
        return عشرات[ع]
    # apl-source:17
    return آحاد[أ] + " و" + عشرات[ع]
# apl-source:18

# apl-source:19
for ن in [0, 5, 11, 20, 23, 57, 99]:
    # apl-source:20
    print(ن, "=", بالكلمات(ن))
# apl-source:21
