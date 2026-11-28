
# apl-source:1
# مثال 2051 — جمع عددين بالعمليات على البتات
# apl-source:2
# Add integers with bit ops
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2051-add-two-integers-with-xor-and-carry.apl
# apl-source:6

# apl-source:7
# # نكرر حتى ينتهي الحمل
# apl-source:8
# # للأعداد غير السالبة
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
def اجمع(ا, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    حمل = (ا & ب) << 1
    # apl-source:21
    ا = ا ^ ب
    # apl-source:22
    ب = حمل
  # apl-source:23
  return ا
# apl-source:24

# apl-source:25
تأكد_يساوي(اجمع(1, 2), 3, "١ و٢")
# apl-source:26
تأكد_يساوي(اجمع(2, 3), 5, "٢ و٣")
# apl-source:27
تأكد_يساوي(اجمع(0, 0), 0, "صفران")
# apl-source:28
تأكد_يساوي(اجمع(7, 8), 15, "٧ و٨")
# apl-source:29
تأكد_يساوي(اجمع(255, 1), 256, "حمل طويل")
# apl-source:30
