
# apl-source:1
# مثال 2080 — الفائدة البسيطة والمبلغ النهائي
# apl-source:2
# Simple interest
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2080-simple-interest-and-final-amount.apl
# apl-source:6

# apl-source:7
# # نستخدم أعدادا صحيحة
# apl-source:8
# # ونرجع الفائدة والمبلغ
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
def بسيطة(اصل, نسبة, سنوات):
  # apl-source:19
  فائدة = اصل * نسبة * سنوات // 100
  # apl-source:20
  return [فائدة, اصل + فائدة]
# apl-source:21

# apl-source:22
تأكد_يساوي(بسيطة(1000, 5, 3), [150, 1150], "ثلاث سنوات")
# apl-source:23
تأكد_يساوي(بسيطة(200, 10, 0), [0, 200], "صفر سنة")
# apl-source:24
