
# apl-source:1
# مثال 438 — التفاف النص
# apl-source:2
# Text wrapping
# apl-source:3
# Demonstrates: قص الأسطر بعرض ثابت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/438-text-wrap.apl
# apl-source:6

# apl-source:7
def التف(نص_الدخل, عرض_مطلوب):
    # apl-source:8
    كلمات = نص_الدخل.split(" ")
    # apl-source:9
    سطر = ""
    # apl-source:10
    for كلمة in كلمات:
        # apl-source:11
        if len(سطر) + len(كلمة) + 1 > عرض_مطلوب:
            # apl-source:12
            print(سطر)
            # apl-source:13
            سطر = كلمة
        # apl-source:14
        elif سطر == "":
            # apl-source:15
            سطر = كلمة
        # apl-source:16
        else:
            # apl-source:17
            سطر = سطر + " " + كلمة
    # apl-source:18
    if سطر != "":
        # apl-source:19
        print(سطر)
# apl-source:20

# apl-source:21
التف("البرمجة بلغة APL سهلة وممتعة وتدعم العربية بالكامل في كل شيء", 30)
# apl-source:22
