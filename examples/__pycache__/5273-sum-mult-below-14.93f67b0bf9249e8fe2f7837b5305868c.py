
# apl-source:1
# مثال 5273 — مجموع مضاعفات 14 تحت ن
# apl-source:2
# Sum of multiples of 14 below n
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5273-sum-mult-below-14.apl
# apl-source:6

# apl-source:7
# نمر على الأعداد ونجمع المضاعفات
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  م = 0
  # apl-source:19
  for ي in range(ن):
    # apl-source:20
    if ي % 14 == 0:
      # apl-source:21
      م = م + ي
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(10), 0, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(50), 84, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(100), 392, "حالة 4")
# apl-source:28
