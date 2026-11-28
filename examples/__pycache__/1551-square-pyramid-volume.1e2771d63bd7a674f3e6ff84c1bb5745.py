
# apl-source:1
# مثال 1551 — حجم الهرم قاعدته مربعة
# apl-source:2
# Square pyramid volume
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1551-square-pyramid-volume.apl
# apl-source:6

# apl-source:7
# مساحة القاعدة ضلع مربع
# apl-source:8
# الحجم = القاعدة × الارتفاع ÷ 3
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
def حجم_الهرم(ضلع, ارتفاع):
  # apl-source:19
  return ضلع * ضلع * ارتفاع / 3
# apl-source:20

# apl-source:21
تأكد_يساوي(حجم_الهرم(3, 10), 30.0, "ثلاثة")
# apl-source:22
تأكد_يساوي(حجم_الهرم(6, 5), 60.0, "ستة")
# apl-source:23
تأكد_يساوي(حجم_الهرم(0, 5), 0.0, "بلا قاعدة")
# apl-source:24
