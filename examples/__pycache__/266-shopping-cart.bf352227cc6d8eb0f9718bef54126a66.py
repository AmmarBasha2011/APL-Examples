
# apl-source:1
# مثال 266 — سلة تسوق
# apl-source:2
# Shopping cart
# apl-source:3
# Demonstrates: إضافة وحذف وإجمالي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/266-shopping-cart.apl
# apl-source:6

# apl-source:7
class سلة:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.عناصر = []
# apl-source:10

    # apl-source:11
    def أضف_عنصرا(ذات, اسم, سعر, كمية):
        # apl-source:12
        ذات.عناصر.append({"اسم": اسم, "سعر": سعر, "كمية": كمية})
# apl-source:13

    # apl-source:14
    def إجمالي(ذات):
        # apl-source:15
        مجموع = 0
        # apl-source:16
        for عنصر in ذات.عناصر:
            # apl-source:17
            مجموع = مجموع + عنصر["سعر"] * عنصر["كمية"]
        # apl-source:18
        return مجموع
# apl-source:19

    # apl-source:20
    def اطبع_فاتورة(ذات):
        # apl-source:21
        for عنصر in ذات.عناصر:
            # apl-source:22
            print(عنصر["اسم"], "x", عنصر["كمية"], "=", عنصر["سعر"] * عنصر["كمية"])
        # apl-source:23
        print("الإجمالي:", ذات.إجمالي())
# apl-source:24

# apl-source:25
س = سلة()
# apl-source:26
س.أضف_عنصرا("خبز", 10, 2)
# apl-source:27
س.أضف_عنصرا("حليب", 25, 1)
# apl-source:28
س.أضف_عنصرا("جبنة", 40, 1)
# apl-source:29
س.اطبع_فاتورة()
# apl-source:30
