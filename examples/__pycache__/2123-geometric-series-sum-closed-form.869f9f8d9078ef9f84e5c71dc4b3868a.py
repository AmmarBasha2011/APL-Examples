
# apl-source:1
# مثال 2123 — مجموع المتسلسلة الهندسية
# apl-source:2
# Geometric series sum
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2123-geometric-series-sum-closed-form.apl
# apl-source:6

# apl-source:7
# # الحالة r=1 خاصة
# apl-source:8
# # نستخدم القسمة الصحيحة
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
def مجموع_هندسي(ا, ر, ن):
  # apl-source:19
  if ر == 1:
    # apl-source:20
    return ا * ن
  # apl-source:21
  return ا * (ر ** ن - 1) // (ر - 1)
# apl-source:22

# apl-source:23
تأكد_يساوي(مجموع_هندسي(1, 2, 10), 1023, "اثنان")
# apl-source:24
تأكد_يساوي(مجموع_هندسي(3, 1, 5), 15, "ر=١")
# apl-source:25
تأكد_يساوي(مجموع_هندسي(2, 3, 4), 80, "ثلاثة")
# apl-source:26
