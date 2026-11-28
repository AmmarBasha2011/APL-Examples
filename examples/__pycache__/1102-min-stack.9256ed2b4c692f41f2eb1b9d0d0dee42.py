
# apl-source:1
# مثال 1102 — مكدس بأدنى قيمة
# apl-source:2
# Min stack
# apl-source:3
# Demonstrates: مكدس مساعد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1102-min-stack.apl
# apl-source:6

# apl-source:7
# مكدس ثان يحفظ الأدنى عند كل مستوى
# apl-source:8
# فيبقى الأدنى متاحاً بعد كل دفع وسحب
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
class مكدس_ادنى:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.عناصر = []
        # apl-source:21
        ذات.ادنيات = []
# apl-source:22

    # apl-source:23
    def ادفع(ذات, س):
        # apl-source:24
        ذات.عناصر = ذات.عناصر + [س]
        # apl-source:25
        if (len(ذات.ادنيات) == 0) or (س <= ذات.ادنيات[-1]):
            # apl-source:26
            ذات.ادنيات = ذات.ادنيات + [س]
# apl-source:27

    # apl-source:28
    def اسحب(ذات):
        # apl-source:29
        س = ذات.عناصر.pop()
        # apl-source:30
        if س == ذات.ادنيات[-1]:
            # apl-source:31
            ذات.ادنيات.pop()
        # apl-source:32
        return س
# apl-source:33

    # apl-source:34
    def قمة(ذات):
        # apl-source:35
        return ذات.عناصر[-1]
# apl-source:36

    # apl-source:37
    def ادنى(ذات):
        # apl-source:38
        return ذات.ادنيات[-1]
# apl-source:39

# apl-source:40
م = مكدس_ادنى()
# apl-source:41
م.ادفع(-2)
# apl-source:42
م.ادفع(0)
# apl-source:43
م.ادفع(-3)
# apl-source:44
تأكد_يساوي(م.ادنى(), -3, "الأدنى بعد ثلاثة دفعات")
# apl-source:45
م.اسحب()
# apl-source:46
تأكد_يساوي(م.قمة(), 0, "القمة بعد السحب")
# apl-source:47
تأكد_يساوي(م.ادنى(), -2, "الأدنى بعد السحب")
# apl-source:48
م.ادفع(-2)
# apl-source:49
م.اسحب()
# apl-source:50
تأكد_يساوي(م.ادنى(), -2, "الأدنى مع تكرار")
# apl-source:51
