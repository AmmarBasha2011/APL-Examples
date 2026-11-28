
# apl-source:1
# مثال 1641 — القاسم المشترك الأكبر لقائمة
# apl-source:2
# GCD of a list of numbers
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1641-gcd-of-number-list.apl
# apl-source:6

# apl-source:7
# قاسم قائمة = قاسم أول عنصر مع قاسم الباقي
# apl-source:8
# نحدث القاسم بعنصر عنصر
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
def قاسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = ب
    # apl-source:21
    ب = أ % ب
    # apl-source:22
    أ = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def قاسم_القائمة(ق):
  # apl-source:26
  ناتج = ق[0]
  # apl-source:27
  for ع in ق:
    # apl-source:28
    ناتج = قاسم(ناتج, ع)
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(قاسم_القائمة([12, 18, 24]), 6, "ستة")
# apl-source:32
تأكد_يساوي(قاسم_القائمة([7, 13]), 1, "أوليان")
# apl-source:33
تأكد_يساوي(قاسم_القائمة([9]), 9, "عدد واحد")
# apl-source:34
