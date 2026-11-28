
# apl-source:1
# مثال 482 — نظام مكتبة
# apl-source:2
# Library system
# apl-source:3
# Demonstrates: إعارة وإرجاع كتب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/482-library-system.apl
# apl-source:6

# apl-source:7
class كتاب:
    # apl-source:8
    def __init__(ذات, عنوان):
        # apl-source:9
        ذات.عنوان = عنوان
        # apl-source:10
        ذات.معار = False
# apl-source:11

    # apl-source:12
    def أعر(ذات):
        # apl-source:13
        if ذات.معار:
            # apl-source:14
            print("غير متاح:", ذات.عنوان)
            # apl-source:15
            return
        # apl-source:16
        ذات.معار = True
        # apl-source:17
        print("تمت الإعارة:", ذات.عنوان)
# apl-source:18

    # apl-source:19
    def أرجع_الكتاب(ذات):
        # apl-source:20
        ذات.معار = False
        # apl-source:21
        print("تم الإرجاع:", ذات.عنوان)
# apl-source:22

# apl-source:23
ك1 = كتاب("مقدمة في البرمجة")
# apl-source:24
ك2 = كتاب("أسرار الخوارزميات")
# apl-source:25
ك1.أعر()
# apl-source:26
ك1.أعر()
# apl-source:27
ك1.أرجع_الكتاب()
# apl-source:28
ك2.أعر()
# apl-source:29
