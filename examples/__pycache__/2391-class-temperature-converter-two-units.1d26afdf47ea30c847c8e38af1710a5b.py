
# apl-source:1
# مثال 2391 — صنف محول حرارة
# apl-source:2
# Temperature converter class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2391-class-temperature-converter-two-units.apl
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
class حرارة:
    # apl-source:19
    def __init__(ذات, س):
        # apl-source:20
        ذات.س = س
# apl-source:21

    # apl-source:22
    def فهرنهايت(ذات):
        # apl-source:23
        return ذات.س * 9 // 5 + 32
# apl-source:24

    # apl-source:25
    def كلفن(ذات):
        # apl-source:26
        return ذات.س + 273
# apl-source:27

# apl-source:28
ح = حرارة(100)
# apl-source:29
تأكد_يساوي(ح.فهرنهايت(), 212, "غليان")
# apl-source:30
تأكد_يساوي(ح.كلفن(), 373, "كلفن")
# apl-source:31
تأكد_يساوي(حرارة(0).فهرنهايت(), 32, "تجمد")
# apl-source:32
