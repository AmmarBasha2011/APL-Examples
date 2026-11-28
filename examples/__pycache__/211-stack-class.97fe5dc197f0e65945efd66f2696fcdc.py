
# apl-source:1
# مثال 211 — المكدس كصنف
# apl-source:2
# Stack as a class
# apl-source:3
# Demonstrates: صنف، أضف، pop، peek
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/211-stack-class.apl
# apl-source:6

# apl-source:7
class مكدس:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.عناصر = []
# apl-source:10

    # apl-source:11
    def ادفع(ذات, عنصر):
        # apl-source:12
        ذات.عناصر.append(عنصر)
# apl-source:13

    # apl-source:14
    def اسحب(ذات):
        # apl-source:15
        if ذات.فارغ():
            # apl-source:16
            return "مكدس فارغ"
        # apl-source:17
        return ذات.عناصر.pop()
# apl-source:18

    # apl-source:19
    def قمة(ذات):
        # apl-source:20
        if ذات.فارغ():
            # apl-source:21
            return "مكدس فارغ"
        # apl-source:22
        return ذات.عناصر[-1]
# apl-source:23

    # apl-source:24
    def فارغ(ذات):
        # apl-source:25
        return len(ذات.عناصر) == 0
# apl-source:26

    # apl-source:27
    def حجم_المكدس(ذات):
        # apl-source:28
        return len(ذات.عناصر)
# apl-source:29

# apl-source:30
م = مكدس()
# apl-source:31
م.ادفع(10)
# apl-source:32
م.ادفع(20)
# apl-source:33
م.ادفع(30)
# apl-source:34
print("القمة:", م.قمة())
# apl-source:35
print("اسحب:", م.اسحب())
# apl-source:36
print("الحجم:", م.حجم_المكدس())
# apl-source:37
