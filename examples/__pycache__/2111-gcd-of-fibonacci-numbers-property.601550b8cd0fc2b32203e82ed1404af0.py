
# apl-source:1
# مثال 2111 — القاسم المشترك الأكبر لأعداد فيبوناتشي
# apl-source:2
# GCD of Fibonacci numbers
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2111-gcd-of-fibonacci-numbers-property.apl
# apl-source:6

# apl-source:7
# # نتحقق من الخاصية الشهيرة
# apl-source:8
# # بحساب الطرفين
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
def فيب(ن):
  # apl-source:19
  ا = 0
  # apl-source:20
  ب = 1
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    ت = ا + ب
    # apl-source:23
    ا = ب
    # apl-source:24
    ب = ت
  # apl-source:25
  return ا
# apl-source:26

# apl-source:27
def قاسم(ا, ب):
  # apl-source:28
  while ب != 0:
    # apl-source:29
    ت = ب
    # apl-source:30
    ب = ا % ب
    # apl-source:31
    ا = ت
  # apl-source:32
  return ا
# apl-source:33

# apl-source:34
تأكد_يساوي(قاسم(فيب(12), فيب(18)), 8, "١٢ و١٨")
# apl-source:35
تأكد_يساوي(قاسم(فيب(10), فيب(15)), 5, "١٠ و١٥")
# apl-source:36
تأكد_يساوي(قاسم(فيب(12), فيب(18)), فيب(قاسم(12, 18)), "الخاصية")
# apl-source:37
