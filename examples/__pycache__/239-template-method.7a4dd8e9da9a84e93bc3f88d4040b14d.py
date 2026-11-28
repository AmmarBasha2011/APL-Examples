
# apl-source:1
# مثال 239 — نمط القالب
# apl-source:2
# Template method pattern
# apl-source:3
# Demonstrates: هيكل ثابت وخطوات متغيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/239-template-method.apl
# apl-source:6

# apl-source:7
class مشروب:
    # apl-source:8
    def حضر(ذات):
        # apl-source:9
        ذات.اغل_الماء()
        # apl-source:10
        ذات.أضف_الأساس()
        # apl-source:11
        ذات.قدم()
# apl-source:12

    # apl-source:13
    def اغل_الماء(ذات):
        # apl-source:14
        print("غلي الماء")
# apl-source:15

    # apl-source:16
    def أضف_الأساس(ذات):
        # apl-source:17
        print("أساس عام")
# apl-source:18

    # apl-source:19
    def قدم(ذات):
        # apl-source:20
        print("يقدم في كوب")
# apl-source:21

# apl-source:22
class شاي(مشروب):
    # apl-source:23
    def أضف_الأساس(ذات):
        # apl-source:24
        print("نقع الشاي")
# apl-source:25

# apl-source:26
class قهوة(مشروب):
    # apl-source:27
    def أضف_الأساس(ذات):
        # apl-source:28
        print("تصفية القهوة")
# apl-source:29

# apl-source:30
print("--- شاي ---")
# apl-source:31
شاي().حضر()
# apl-source:32
print("--- قهوة ---")
# apl-source:33
قهوة().حضر()
# apl-source:34
