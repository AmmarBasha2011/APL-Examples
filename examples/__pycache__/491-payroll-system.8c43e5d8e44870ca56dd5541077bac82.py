
# apl-source:1
# مثال 491 — نظام رواتب
# apl-source:2
# Payroll system
# apl-source:3
# Demonstrates: موظفون وصافي الراتب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/491-payroll-system.apl
# apl-source:6

# apl-source:7
class موظف:
    # apl-source:8
    def __init__(ذات, اسم, أساسي, بدلات):
        # apl-source:9
        ذات.اسم = اسم
        # apl-source:10
        ذات.أساسي = أساسي
        # apl-source:11
        ذات.بدلات = بدلات
# apl-source:12

    # apl-source:13
    def صافي(ذات):
        # apl-source:14
        إجمالي = ذات.أساسي + ذات.بدلات
        # apl-source:15
        ضريبة = إجمالي * 10 / 100
        # apl-source:16
        return إجمالي - ضريبة
# apl-source:17

    # apl-source:18
    def كشف(ذات):
        # apl-source:19
        print(ذات.اسم, "- أساسي:", ذات.أساسي, "- صافي:", ذات.صافي())
# apl-source:20

# apl-source:21
م1 = موظف("عمار", 8000, 1500)
# apl-source:22
م2 = موظف("سارة", 9500, 2000)
# apl-source:23
م1.كشف()
# apl-source:24
م2.كشف()
# apl-source:25
