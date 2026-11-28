
# apl-source:1
# مثال 5045 — حصر القيمة بين 50 و 75
# apl-source:2
# Clamp value into [50,75]
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5045-clamp-50-75.apl
# apl-source:6

# apl-source:7
# إن كانت أقل من الحد الأدنى نرجع الحد الأدنى
# apl-source:8
# وإن زادت نرجع الحد الأعلى
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
def ف(ن):
  # apl-source:19
  if ن < 50:
    # apl-source:20
    return 50
  # apl-source:21
  if ن > 75:
    # apl-source:22
    return 75
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(45), 50, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(80), 75, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(62), 62, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(50), 50, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(75), 75, "حالة 5")
# apl-source:30
