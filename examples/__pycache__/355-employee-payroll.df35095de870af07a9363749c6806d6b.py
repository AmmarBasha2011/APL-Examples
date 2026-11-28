
# apl-source:1
# مثال 355 — رواتب الموظفين
# apl-source:2
# Employee payroll
# apl-source:3
# Demonstrates: وراثة وحساب صافي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/355-employee-payroll.apl
# apl-source:6

# apl-source:7
class موظف:
    # apl-source:8
    def __init__(ذات, اسم, أساسي):
        # apl-source:9
        ذات.اسم = اسم
        # apl-source:10
        ذات.أساسي = أساسي
# apl-source:11

    # apl-source:12
    def صافي(ذات):
        # apl-source:13
        return ذات.أساسي
# apl-source:14

    # apl-source:15
    def قسيمة(ذات):
        # apl-source:16
        print(ذات.اسم, ": الصافي =", ذات.صافي())
# apl-source:17

# apl-source:18
class مدير(موظف):
    # apl-source:19
    def __init__(ذات, اسم, أساسي, بدل):
        # apl-source:20
        ذات.اسم = اسم
        # apl-source:21
        ذات.أساسي = أساسي
        # apl-source:22
        ذات.بدل = بدل
# apl-source:23

    # apl-source:24
    def صافي(ذات):
        # apl-source:25
        return ذات.أساسي + ذات.بدل
# apl-source:26

# apl-source:27
class مندوب(موظف):
    # apl-source:28
    def __init__(ذات, اسم, أساسي, عمولة):
        # apl-source:29
        ذات.اسم = اسم
        # apl-source:30
        ذات.أساسي = أساسي
        # apl-source:31
        ذات.عمولة = عمولة
# apl-source:32

    # apl-source:33
    def صافي(ذات):
        # apl-source:34
        return ذات.أساسي + ذات.عمولة
# apl-source:35

# apl-source:36
موظف("أحمد", 5000).قسيمة()
# apl-source:37
مدير("سارة", 8000, 2000).قسيمة()
# apl-source:38
مندوب("خالد", 4000, 1500).قسيمة()
# apl-source:39
