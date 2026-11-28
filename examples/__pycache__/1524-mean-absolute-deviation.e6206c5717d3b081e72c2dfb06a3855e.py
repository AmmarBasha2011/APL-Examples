
# apl-source:1
# مثال 1524 — متوسط الانحراف المطلق
# apl-source:2
# Mean absolute deviation
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1524-mean-absolute-deviation.apl
# apl-source:6

# apl-source:7
# الفرق المطلق لا يحتاج جذراً
# apl-source:8
# نجمعها ونقسم على العدد
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
def انحراف_مطلق(أ):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ع in أ:
    # apl-source:21
    مجموع = مجموع + ع
  # apl-source:22
  متوسط = مجموع / len(أ)
  # apl-source:23
  كل = 0
  # apl-source:24
  for ع in أ:
    # apl-source:25
    ف = ع - متوسط
    # apl-source:26
    if ف < 0:
      # apl-source:27
      ف = -ف
    # apl-source:28
    كل = كل + ف
  # apl-source:29
  return كل / len(أ)
# apl-source:30

# apl-source:31
تأكد_يساوي(انحراف_مطلق([1, 2, 3, 4, 5]), 1.2, "خمسة")
# apl-source:32
تأكد_يساوي(انحراف_مطلق([6, 6]), 0.0, "متساويان")
# apl-source:33
