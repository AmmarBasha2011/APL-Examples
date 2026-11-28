
# apl-source:1
# مثال 4873 — مجموع الأعداد من 1 إلى ضعف 9 وزيادة
# apl-source:2
# Sum 1..n for scaled n (k=9)
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4873-triangle-number-9.apl
# apl-source:6

# apl-source:7
# مجموع الأعداد المتتالية = ن(ن+1)/2
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
  ن = ن * 9
  # apl-source:19
  return ن * (ن + 1) // 2
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(1), 45, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(2), 171, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(3), 378, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(10), 4095, "حالة 4")
# apl-source:25
