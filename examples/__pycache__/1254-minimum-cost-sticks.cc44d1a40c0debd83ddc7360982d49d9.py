
# apl-source:1
# مثال 1254 — أقل كلفة وصل
# apl-source:2
# Minimum cost to connect sticks
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1254-minimum-cost-sticks.apl
# apl-source:6

# apl-source:7
# نصل دائماً أقصر عصاتين
# apl-source:8
# وكلفة الوصل مجموع طوليهما
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
def كلفة_وصل(عصي):
  # apl-source:19
  ق = sorted(عصي)
  # apl-source:20
  ك = 0
  # apl-source:21
  while len(ق) > 1:
    # apl-source:22
    ا = ق.pop(0)
    # apl-source:23
    ب = ق.pop(0)
    # apl-source:24
    ك = ك + ا + ب
    # apl-source:25
    ق = ق + [ا + ب]
    # apl-source:26
    ق = sorted(ق)
  # apl-source:27
  return ك
# apl-source:28

# apl-source:29
تأكد_يساوي(كلفة_وصل([2,4,3]), 14, "ثلاث")
# apl-source:30
تأكد_يساوي(كلفة_وصل([1,8,3,5]), 30, "أربع")
# apl-source:31
تأكد_يساوي(كلفة_وصل([5]), 0, "عصا")
# apl-source:32
