
# apl-source:1
# مثال 2397 — صنف مجمع بسجل
# apl-source:2
# Accumulator with history
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2397-class-accumulator-history-list.apl
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
class مجمع:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.م = 0
        # apl-source:21
        ذات.س = []
# apl-source:22

    # apl-source:23
    def اضف(ذات, ق):
        # apl-source:24
        ذات.م = ذات.م + ق
        # apl-source:25
        ذات.س = ذات.س + [ذات.م]
# apl-source:26

# apl-source:27
مج = مجمع()
# apl-source:28
مج.اضف(5)
# apl-source:29
مج.اضف(10)
# apl-source:30
مج.اضف(-3)
# apl-source:31
تأكد_يساوي(مج.م, 12, "المجموع")
# apl-source:32
تأكد_يساوي(مج.س, [5, 15, 12], "السجل")
# apl-source:33
