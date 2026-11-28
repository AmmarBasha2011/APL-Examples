
# apl-source:1
# مثال 235 — نمط البنّاء
# apl-source:2
# Builder pattern
# apl-source:3
# Demonstrates: بناء كائن خطوة بخطوة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/235-builder.apl
# apl-source:6

# apl-source:7
class بناي_بيتزا:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.مكونات = []
        # apl-source:10
        ذات.مقاس = "وسط"
# apl-source:11

    # apl-source:12
    def بمقاس(ذات, مقاس):
        # apl-source:13
        ذات.مقاس = مقاس
        # apl-source:14
        return ذات
# apl-source:15

    # apl-source:16
    def أضف_مكون(ذات, مكون):
        # apl-source:17
        ذات.مكونات.append(مكون)
        # apl-source:18
        return ذات
# apl-source:19

    # apl-source:20
    def ابن(ذات):
        # apl-source:21
        return "بيتزا " + ذات.مقاس + " بـ" + " و".join(ذات.مكونات)
# apl-source:22

# apl-source:23
بيتزا = بناي_بيتزا().بمقاس("كبير").أضف_مكون("جبنة").أضف_مكون("فطر").أضف_مكون("زيتون").ابن()
# apl-source:24
print(بيتزا)
# apl-source:25
