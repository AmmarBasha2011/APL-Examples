
# apl-source:1
# مثال 356 — مساحات الأشكال
# apl-source:2
# Shapes and areas
# apl-source:3
# Demonstrates: تعدد أشكال بالوراثة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/356-shapes-area.apl
# apl-source:6

# apl-source:7
class شكل:
    # apl-source:8
    def مساحة(ذات):
        # apl-source:9
        return 0
# apl-source:10

    # apl-source:11
    def صف(ذات):
        # apl-source:12
        print("المساحة =", ذات.مساحة())
# apl-source:13

# apl-source:14
class مربع(شكل):
    # apl-source:15
    def __init__(ذات, ضلع):
        # apl-source:16
        ذات.ضلع = ضلع
# apl-source:17

    # apl-source:18
    def مساحة(ذات):
        # apl-source:19
        return ذات.ضلع * ذات.ضلع
# apl-source:20

# apl-source:21
class مستطيل(شكل):
    # apl-source:22
    def __init__(ذات, طول_ضلع, عرض_ضلع):
        # apl-source:23
        ذات.طول_ضلع = طول_ضلع
        # apl-source:24
        ذات.عرض_ضلع = عرض_ضلع
# apl-source:25

    # apl-source:26
    def مساحة(ذات):
        # apl-source:27
        return ذات.طول_ضلع * ذات.عرض_ضلع
# apl-source:28

# apl-source:29
class دائرة(شكل):
    # apl-source:30
    def __init__(ذات, نصف_قطر):
        # apl-source:31
        ذات.نصف_قطر = نصف_قطر
# apl-source:32

    # apl-source:33
    def مساحة(ذات):
        # apl-source:34
        return round(3.14159 * ذات.نصف_قطر * ذات.نصف_قطر, 2)
# apl-source:35

# apl-source:36
مربع(4).صف()
# apl-source:37
مستطيل(3, 5).صف()
# apl-source:38
دائرة(2).صف()
# apl-source:39
