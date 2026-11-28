
# apl-source:1
# مثال 212 — الطابور كصنف
# apl-source:2
# Queue as a class
# apl-source:3
# Demonstrates: صنف، إدخال وإخراج بالترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/212-queue-class.apl
# apl-source:6

# apl-source:7
class طابور:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.عناصر = []
# apl-source:10

    # apl-source:11
    def أدخل(ذات, عنصر):
        # apl-source:12
        ذات.عناصر.append(عنصر)
# apl-source:13

    # apl-source:14
    def أخرج_أول(ذات):
        # apl-source:15
        if ذات.فارغ():
            # apl-source:16
            return "طابور فارغ"
        # apl-source:17
        return ذات.عناصر.pop(0)
# apl-source:18

    # apl-source:19
    def فارغ(ذات):
        # apl-source:20
        return len(ذات.عناصر) == 0
# apl-source:21

# apl-source:22
ط = طابور()
# apl-source:23
ط.أدخل("أول")
# apl-source:24
ط.أدخل("ثاني")
# apl-source:25
ط.أدخل("ثالث")
# apl-source:26
print(ط.أخرج_أول())
# apl-source:27
print(ط.أخرج_أول())
# apl-source:28
ط.أدخل("رابع")
# apl-source:29
print(ط.أخرج_أول())
# apl-source:30
print(ط.أخرج_أول())
# apl-source:31
