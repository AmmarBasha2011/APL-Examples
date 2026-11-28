
# apl-source:1
# مثال 2153 — صنف الكسر مع الجمع والاختصار
# apl-source:2
# Fraction class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2153-fraction-class-add-and-reduce.apl
# apl-source:6

# apl-source:7
# # نخزن البسط والمقام
# apl-source:8
# # ونختصر بالقاسم المشترك
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
class كسر:
    # apl-source:19
    def __init__(ذات, ب, م):
        # apl-source:20
        ذات.ب = ب
        # apl-source:21
        ذات.م = م
# apl-source:22

    # apl-source:23
    def اجمع(ذات, اخر):
        # apl-source:24
        ب = ذات.ب * اخر.م + اخر.ب * ذات.م
        # apl-source:25
        م = ذات.م * اخر.م
        # apl-source:26
        ا = ب
        # apl-source:27
        ج = م
        # apl-source:28
        while ج != 0:
            # apl-source:29
            ت = ج
            # apl-source:30
            ج = ا % ج
            # apl-source:31
            ا = ت
        # apl-source:32
        return كسر(ب // ا, م // ا)
# apl-source:33

    # apl-source:34
    def نص_كسر(ذات):
        # apl-source:35
        return str(ذات.ب) + "/" + str(ذات.م)
# apl-source:36

# apl-source:37
ك = كسر(1, 2).اجمع(كسر(1, 3))
# apl-source:38
تأكد_يساوي(ك.نص_كسر(), "5/6", "نصف وثلث")
# apl-source:39
تأكد_يساوي(كسر(1, 4).اجمع(كسر(1, 4)).نص_كسر(), "1/2", "ربعان")
# apl-source:40
تأكد_يساوي(كسر(3, 4).اجمع(كسر(1, 4)).نص_كسر(), "1/1", "واحد")
# apl-source:41
