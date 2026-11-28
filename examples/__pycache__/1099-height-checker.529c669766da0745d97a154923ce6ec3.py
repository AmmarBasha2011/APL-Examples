
# apl-source:1
# مثال 1099 — فاحص الأطوال
# apl-source:2
# Height checker
# apl-source:3
# Demonstrates: مقارنة بالنسخة المرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1099-height-checker.apl
# apl-source:6

# apl-source:7
# الصف المتوقع هو الأطوال مرتبة تصاعدياً
# apl-source:8
# نعد المواضع التي يختلف فيها الطول الفعلي عن المتوقع
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
def اخطاء_الصف(اطوال):
  # apl-source:19
  متوقع = sorted(اطوال)
  # apl-source:20
  عدد_ = 0
  # apl-source:21
  for ع in range(len(اطوال)):
    # apl-source:22
    if اطوال[ع] != متوقع[ع]:
      # apl-source:23
      عدد_ = عدد_ + 1
  # apl-source:24
  return عدد_
# apl-source:25

# apl-source:26
تأكد_يساوي(اخطاء_الصف([1, 1, 4, 2, 1, 3]), 3, "ثلاثة")
# apl-source:27
تأكد_يساوي(اخطاء_الصف([5, 1, 2, 3, 4]), 5, "الكل")
# apl-source:28
تأكد_يساوي(اخطاء_الصف([1, 2, 3, 4, 5]), 0, "مرتبة")
# apl-source:29
