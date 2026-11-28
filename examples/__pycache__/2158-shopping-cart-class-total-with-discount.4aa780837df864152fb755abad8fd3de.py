
# apl-source:1
# مثال 2158 — صنف سلة تسوق بخصم نسبة
# apl-source:2
# Shopping cart class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2158-shopping-cart-class-total-with-discount.apl
# apl-source:6

# apl-source:7
# # السعر بالقروش
# apl-source:8
# # الخصم بالقسمة الصحيحة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class سلة:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.بنود = []
# apl-source:21

    # apl-source:22
    def اضف(ذات, سعر, كمية):
        # apl-source:23
        ذات.بنود = ذات.بنود + [[سعر, كمية]]
# apl-source:24

    # apl-source:25
    def مجموع(ذات, خصم):
        # apl-source:26
        م = 0
        # apl-source:27
        for ب in ذات.بنود:
            # apl-source:28
            م = م + ب[0] * ب[1]
        # apl-source:29
        return م * (100 - خصم) // 100
# apl-source:30

# apl-source:31
س = سلة()
# apl-source:32
س.اضف(250, 2)
# apl-source:33
س.اضف(100, 3)
# apl-source:34
تأكد_يساوي(س.مجموع(0), 800, "بلا خصم")
# apl-source:35
تأكد_يساوي(س.مجموع(10), 720, "عشرة بالمئة")
# apl-source:36
تأكد_يساوي(سلة().مجموع(50), 0, "فارغة")
# apl-source:37
