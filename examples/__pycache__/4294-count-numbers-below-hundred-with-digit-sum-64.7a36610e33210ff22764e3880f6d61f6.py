
# apl-source:1
# مثال 4294 — أعداد دون المئة مجموع أرقامها 64
# apl-source:2
# Numbers below 100 with digit sum 64
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4294-count-numbers-below-hundred-with-digit-sum-64.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  ع = 0
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    م = 0
    # apl-source:22
    for ر in str(ي):
      # apl-source:23
      م = م + int(ر)
    # apl-source:24
    if م == 64:
      # apl-source:25
      ع = ع + 1
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(10), 0, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(50), 0, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(100), 0, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(200), 0, "حالة 4")
# apl-source:32
