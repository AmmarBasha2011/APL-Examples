
# apl-source:1
# مثال 1526 — الدرجة المعيارية
# apl-source:2
# Z score of a value
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1526-z-score-of-value.apl
# apl-source:6

# apl-source:7
# نطرح المتوسط من القيمة
# apl-source:8
# ثم نقسم على الانحراف المعياري
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
def درجة_معيارية(أ, قيمة):
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
  انحراف = (مربعات / len(أ)) ** 0.5
  # apl-source:27
  return (قيمة - متوسط) / انحراف
# apl-source:28

# apl-source:29
تأكد_يساوي(درجة_معيارية([2, 4, 4, 4, 5, 5, 7, 9], 9), 2.0, "أعلى")
# apl-source:30
تأكد_يساوي(درجة_معيارية([2, 4, 4, 4, 5, 5, 7, 9], 5), 0.0, "المتوسط")
# apl-source:31
تأكد_يساوي(درجة_معيارية([2, 4, 4, 4, 5, 5, 7, 9], 3), -1.0, "أقل")
# apl-source:32
