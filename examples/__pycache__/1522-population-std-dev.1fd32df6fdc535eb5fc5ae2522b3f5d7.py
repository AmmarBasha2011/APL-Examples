
# apl-source:1
# مثال 1522 — الانحراف المعياري للمجتمع
# apl-source:2
# Population standard deviation
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1522-population-std-dev.apl
# apl-source:6

# apl-source:7
# نحسب المتوسط أولاً
# apl-source:8
# ثم متوسط مربعات الفروق وجذره
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
def انحراف_معياري(أ):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ع in أ:
    # apl-source:21
    مجموع = مجموع + ع
  # apl-source:22
  متوسط = مجموع / len(أ)
  # apl-source:23
  مربعات = 0
  # apl-source:24
  for ع in أ:
    # apl-source:25
    مربعات = مربعات + (ع - متوسط) ** 2
  # apl-source:26
  return (مربعات / len(أ)) ** 0.5
# apl-source:27

# apl-source:28
تأكد_يساوي(انحراف_معياري([2, 4, 4, 4, 5, 5, 7, 9]), 2.0, "مثال كلاسيكي")
# apl-source:29
تأكد_يساوي(انحراف_معياري([5, 5, 5]), 0.0, "متساوية")
# apl-source:30
