
# apl-source:1
# مثال 2396 — صنف مفتاح تشغيل
# apl-source:2
# Toggle switch class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2396-class-toggle-switch-state-flips.apl
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
class مفتاح:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.شغال = False
# apl-source:21

    # apl-source:22
    def بدل(ذات):
        # apl-source:23
        if ذات.شغال:
            # apl-source:24
            ذات.شغال = False
        # apl-source:25
        else:
            # apl-source:26
            ذات.شغال = True
# apl-source:27

# apl-source:28
م = مفتاح()
# apl-source:29
تأكد_يساوي(م.شغال, False, "البداية")
# apl-source:30
م.بدل()
# apl-source:31
تأكد_يساوي(م.شغال, True, "بعد مرة")
# apl-source:32
م.بدل()
# apl-source:33
تأكد_يساوي(م.شغال, False, "بعد مرتين")
# apl-source:34
