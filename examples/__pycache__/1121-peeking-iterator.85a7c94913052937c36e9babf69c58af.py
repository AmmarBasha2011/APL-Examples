
# apl-source:1
# مثال 1121 — مكرر يطلع على التالي
# apl-source:2
# Peeking iterator
# apl-source:3
# Demonstrates: تخزين العنصر التالي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1121-peeking-iterator.apl
# apl-source:6

# apl-source:7
# نخزن العنصر التالي مسبقاً
# apl-source:8
# فيمكن عرضه دون تحريك المؤشر
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
class مكرر_مطلع:
    # apl-source:19
    def __init__(ذات, عناصر):
        # apl-source:20
        ذات.عناصر = list(عناصر)
        # apl-source:21
        ذات.موضع = 0
# apl-source:22

    # apl-source:23
    def لديه_تالي(ذات):
        # apl-source:24
        return ذات.موضع < len(ذات.عناصر)
# apl-source:25

    # apl-source:26
    def اطلع(ذات):
        # apl-source:27
        return ذات.عناصر[ذات.موضع]
# apl-source:28

    # apl-source:29
    def تالي(ذات):
        # apl-source:30
        س = ذات.عناصر[ذات.موضع]
        # apl-source:31
        ذات.موضع = ذات.موضع + 1
        # apl-source:32
        return س
# apl-source:33

# apl-source:34
م = مكرر_مطلع([1, 2, 3])
# apl-source:35
تأكد_يساوي(م.تالي(), 1, "التالي الأول")
# apl-source:36
تأكد_يساوي(م.اطلع(), 2, "اطلاع")
# apl-source:37
تأكد_يساوي(م.تالي(), 2, "التالي بعد الاطلاع")
# apl-source:38
تأكد_يساوي(م.تالي(), 3, "التالي الأخير")
# apl-source:39
تأكد_يساوي(م.لديه_تالي(), False, "انتهى")
# apl-source:40
