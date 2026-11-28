
# apl-source:1
# مثال 4968 — تحقق توازن الأقواس angle
# apl-source:2
# Balanced angle brackets
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4968-balanced-angle.apl
# apl-source:6

# apl-source:7
# عداد يزيد عند الفتح وينقص عند الإغلاق
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  د = 0
  # apl-source:19
  for ح in ن:
    # apl-source:20
    if ح == "<":
      # apl-source:21
      د = د + 1
    # apl-source:22
    elif ح == ">":
      # apl-source:23
      د = د - 1
      # apl-source:24
      if د < 0:
        # apl-source:25
        return False
  # apl-source:26
  return د == 0
# apl-source:27

# apl-source:28
تأكد_يساوي(ف("<<>>"), True, "حالة 1")
# apl-source:29
تأكد_يساوي(ف("<>>"), False, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(""), True, "حالة 3")
# apl-source:31
تأكد_يساوي(ف("<<<>>"), False, "حالة 4")
# apl-source:32
تأكد_يساوي(ف("><"), False, "حالة 5")
# apl-source:33
