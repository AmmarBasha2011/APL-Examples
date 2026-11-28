
# apl-source:1
# مثال 1248 — وزن آخر حجر
# apl-source:2
# Last stone weight
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1248-last-stone-weight.apl
# apl-source:6

# apl-source:7
# نأخذ أثقل حجرين في كل مرة
# apl-source:8
# ونعيد الفرق لو لم يتساويا
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
def اخر_حجر(احجار):
  # apl-source:19
  ق = list(احجار)
  # apl-source:20
  while len(ق) > 1:
    # apl-source:21
    ق = sorted(ق)
    # apl-source:22
    ا = ق.pop()
    # apl-source:23
    ب = ق.pop()
    # apl-source:24
    if ا != ب:
      # apl-source:25
      ق = ق + [ا - ب]
  # apl-source:26
  if len(ق) == 0:
    # apl-source:27
    return 0
  # apl-source:28
  return ق[0]
# apl-source:29

# apl-source:30
تأكد_يساوي(اخر_حجر([2,7,4,1,8,1]), 1, "مثال أول")
# apl-source:31
تأكد_يساوي(اخر_حجر([1]), 1, "حجر")
# apl-source:32
تأكد_يساوي(اخر_حجر([3,3]), 0, "متساويان")
# apl-source:33
