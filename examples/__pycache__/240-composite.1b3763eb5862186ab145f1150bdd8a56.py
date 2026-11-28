
# apl-source:1
# مثال 240 — نمط المركّب (نظام ملفات)
# apl-source:2
# Composite pattern (file system)
# apl-source:3
# Demonstrates: شجرة كائنات متجانسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/240-composite.apl
# apl-source:6

# apl-source:7
class ملف:
    # apl-source:8
    def __init__(ذات, اسم, مقاس):
        # apl-source:9
        ذات.اسم = اسم
        # apl-source:10
        ذات.مقاس_الملف = مقاس
# apl-source:11

    # apl-source:12
    def مقاس_كلي(ذات):
        # apl-source:13
        return ذات.مقاس_الملف
# apl-source:14

# apl-source:15
class مجلد:
    # apl-source:16
    def __init__(ذات, اسم):
        # apl-source:17
        ذات.اسم = اسم
        # apl-source:18
        ذات.محتويات = []
# apl-source:19

    # apl-source:20
    def أضف_عنصر(ذات, عنصر):
        # apl-source:21
        ذات.محتويات.append(عنصر)
        # apl-source:22
        return ذات
# apl-source:23

    # apl-source:24
    def مقاس_كلي(ذات):
        # apl-source:25
        مجموع = 0
        # apl-source:26
        for عنصر in ذات.محتويات:
            # apl-source:27
            مجموع = مجموع + عنصر.مقاس_كلي()
        # apl-source:28
        return مجموع
# apl-source:29

# apl-source:30
جذر = مجلد("الجذر")
# apl-source:31
جذر.أضف_عنصر(ملف("أ.txt", 100))
# apl-source:32
فرعي = مجلد("فرعي")
# apl-source:33
فرعي.أضف_عنصر(ملف("ب.txt", 200))
# apl-source:34
فرعي.أضف_عنصر(ملف("ج.txt", 300))
# apl-source:35
جذر.أضف_عنصر(فرعي)
# apl-source:36
print("المقاس الكلي:", جذر.مقاس_كلي())
# apl-source:37
