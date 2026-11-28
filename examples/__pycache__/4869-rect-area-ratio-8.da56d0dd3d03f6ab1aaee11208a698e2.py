
# apl-source:1
# مثال 4869 — مساحة مستطيل طوله 8 أضعاف عرضه
# apl-source:2
# Area of rectangle with length 8x width
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4869-rect-area-ratio-8.apl
# apl-source:6

# apl-source:7
# المساحة = العرض × الطول
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
def ف(ع):
  # apl-source:18
  return ع * (ع * 8)
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(1), 8, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(2), 32, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(5), 200, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(10), 800, "حالة 4")
# apl-source:24
