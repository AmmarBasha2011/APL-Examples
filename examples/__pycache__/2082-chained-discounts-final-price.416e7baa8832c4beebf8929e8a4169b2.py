
# apl-source:1
# مثال 2082 — سعر بعد خصومات متتالية
# apl-source:2
# Chained discounts
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2082-chained-discounts-final-price.apl
# apl-source:6

# apl-source:7
# # نستخدم القسمة الصحيحة
# apl-source:8
# # الخصمان 10 و20 لا يساويان 30
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
def سعر(اصل, خصومات):
  # apl-source:19
  for خ in خصومات:
    # apl-source:20
    اصل = اصل * (100 - خ) // 100
  # apl-source:21
  return اصل
# apl-source:22

# apl-source:23
تأكد_يساوي(سعر(200, [10, 20]), 144, "خصمان")
# apl-source:24
تأكد_يساوي(سعر(200, [50]), 100, "نصف")
# apl-source:25
تأكد_يساوي(سعر(200, []), 200, "بلا خصم")
# apl-source:26
