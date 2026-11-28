
# apl-source:1
# مثال 1435 — تدوير نقطة بربع دورة
# apl-source:2
# Rotate point by quarter turns
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1435-rotate-point-quarter.apl
# apl-source:6

# apl-source:7
# ربع دورة يحول (س، ص) إلى (-ص، س)
# apl-source:8
# نكرر حسب العدد بباقي القسمة على أربعة
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
def دور_نقطة(س, ص, ارباع):
  # apl-source:19
  for ع in range(ارباع % 4):
    # apl-source:20
    ت = س
    # apl-source:21
    س = -ص
    # apl-source:22
    ص = ت
  # apl-source:23
  return [س, ص]
# apl-source:24

# apl-source:25
تأكد_يساوي(دور_نقطة(1, 0, 1), [0, 1], "ربع دورة")
# apl-source:26
تأكد_يساوي(دور_نقطة(2, 3, 2), [-2, -3], "نصف دورة")
# apl-source:27
تأكد_يساوي(دور_نقطة(2, 3, 4), [2, 3], "دورة كاملة")
# apl-source:28
