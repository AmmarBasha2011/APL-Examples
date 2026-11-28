
# apl-source:1
# مثال 1650 — هل العدد من فيبوناتشي
# apl-source:2
# Is a Fibonacci number
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1650-fibonacci-membership-check.apl
# apl-source:6

# apl-source:7
# نبدأ بصفر وواحد
# apl-source:8
# نتوقف عند تجاوز العدد
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
def فيبوناتشي_عدد(ن):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = 1
  # apl-source:21
  while أ < ن:
    # apl-source:22
    ت = أ + ب
    # apl-source:23
    أ = ب
    # apl-source:24
    ب = ت
  # apl-source:25
  return أ == ن
# apl-source:26

# apl-source:27
تأكد_يساوي(فيبوناتشي_عدد(13), True, "ثلاثة عشر")
# apl-source:28
تأكد_يساوي(فيبوناتشي_عدد(14), False, "أربعة عشر")
# apl-source:29
تأكد_يساوي(فيبوناتشي_عدد(0), True, "صفر")
# apl-source:30
تأكد_يساوي(فيبوناتشي_عدد(144), True, "144")
# apl-source:31
