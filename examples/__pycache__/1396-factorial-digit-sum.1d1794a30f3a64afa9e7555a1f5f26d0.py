
# apl-source:1
# مثال 1396 — مجموع أرقام المضروب
# apl-source:2
# Sum of digits of factorial
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1396-factorial-digit-sum.apl
# apl-source:6

# apl-source:7
# نحسب المضروب بأعداد كبيرة
# apl-source:8
# ثم نجمع أرقامه
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
def مضروب_ن(ن):
  # apl-source:19
  ر = 1
  # apl-source:20
  for ع in range(2, ن + 1):
    # apl-source:21
    ر = ر * ع
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
def مجموع_ارقام_المضروب(ن):
  # apl-source:25
  م = 0
  # apl-source:26
  for ح in str(مضروب_ن(ن)):
    # apl-source:27
    م = م + int(ح)
  # apl-source:28
  return م
# apl-source:29

# apl-source:30
تأكد_يساوي(مجموع_ارقام_المضروب(10), 27, "عشرة")
# apl-source:31
تأكد_يساوي(مجموع_ارقام_المضروب(100), 648, "مئة")
# apl-source:32
تأكد_يساوي(مجموع_ارقام_المضروب(1), 1, "واحد")
# apl-source:33
