
# apl-source:1
# مثال 2394 — صنف طالب بالدرجات
# apl-source:2
# Student grades class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2394-class-student-grades-average-best.apl
# apl-source:6

# apl-source:7
# # نعرف صنفا
# apl-source:8
# # ونختبر سلوكه
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
class طالب:
    # apl-source:19
    def __init__(ذات, ا):
        # apl-source:20
        ذات.ا = ا
        # apl-source:21
        ذات.د = []
# apl-source:22

    # apl-source:23
    def اضف(ذات, ق):
        # apl-source:24
        ذات.د = ذات.د + [ق]
# apl-source:25

    # apl-source:26
    def متوسط(ذات):
        # apl-source:27
        return sum(ذات.د) / len(ذات.د)
# apl-source:28

    # apl-source:29
    def اعلى(ذات):
        # apl-source:30
        return max(ذات.د)
# apl-source:31

# apl-source:32
ط = طالب("سلمى")
# apl-source:33
ط.اضف(80)
# apl-source:34
ط.اضف(90)
# apl-source:35
ط.اضف(100)
# apl-source:36
تأكد_يساوي(ط.متوسط(), 90, "المتوسط")
# apl-source:37
تأكد_يساوي(ط.اعلى(), 100, "الأعلى")
# apl-source:38
تأكد_يساوي(ط.ا, "سلمى", "الاسم")
# apl-source:39
