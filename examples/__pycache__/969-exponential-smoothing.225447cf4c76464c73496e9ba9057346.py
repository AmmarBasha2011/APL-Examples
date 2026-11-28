
# apl-source:1
# مثال 969 — التمهيد الأسي
# apl-source:2
# Exponential smoothing
# apl-source:3
# Demonstrates: وزن يتلاشى هندسياً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/969-exponential-smoothing.apl
# apl-source:6

# apl-source:7
# التمهيد الأسي: سلسلة زمنية ملساء بوزن يتلاشى هندسياً
# apl-source:8
# كل قيمة ممهدة مزيج من القراءة الجديدة والممهدة السابقة
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
def مهّد(قراءات, ألفا):
  # apl-source:19
  ناتج = [قراءات[0]]
  # apl-source:20
  for i in range(1, len(قراءات)):
    # apl-source:21
    جديدة = (ألفا * قراءات[i]) + ((1 - ألفا) * ناتج[i - 1])
    # apl-source:22
    ناتج = ناتج + [جديدة]
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
ناتج = مهّد([10, 12, 13, 15, 14, 16], 0.5)
# apl-source:26
تأكد_يساوي(round(ناتج[0], 4), 10, "البذرة الأولى")
# apl-source:27
تأكد_يساوي(round(ناتج[1], 4), 11, "أول تمهيد")
# apl-source:28
تأكد_يساوي(round(ناتج[3], 4), 13.5, "منتصف السلسلة")
# apl-source:29
تأكد_يساوي(round(ناتج[5], 4), 14.875, "آخر السلسلة")
# apl-source:30
تأكد_يساوي(len(ناتج), 6, "طول الناتج")
# apl-source:31
