
# apl-source:1
# مثال 1408 — رقم تشامبرنون
# apl-source:2
# Champernowne constant digit
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1408-champernowne-digit.apl
# apl-source:6

# apl-source:7
# نتخطى كتل الأعداد حسب عدد أرقامها
# apl-source:8
# ثم نحدد الرقم_كاملاً والرقم داخله
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
def رقم_ن(ن):
  # apl-source:19
  ارقام = 1
  # apl-source:20
  عدد = 9
  # apl-source:21
  بداية = 1
  # apl-source:22
  while ن > ارقام * عدد:
    # apl-source:23
    ن = ن - ارقام * عدد
    # apl-source:24
    ارقام = ارقام + 1
    # apl-source:25
    عدد = عدد * 10
    # apl-source:26
    بداية = بداية * 10
  # apl-source:27
  الرقم_كاملاً = بداية + (ن - 1) // ارقام
  # apl-source:28
  return int(str(الرقم_كاملاً)[(ن - 1) % ارقام])
# apl-source:29

# apl-source:30
تأكد_يساوي(رقم_ن(1), 1, "الأول")
# apl-source:31
تأكد_يساوي(رقم_ن(12), 1, "الثاني عشر")
# apl-source:32
تأكد_يساوي(رقم_ن(15), 2, "الخامس عشر")
# apl-source:33
تأكد_يساوي(رقم_ن(190), 1, "مئة وتسعون")
# apl-source:34
تأكد_يساوي(رقم_ن(191), 0, "مئة وواحد وتسعون")
# apl-source:35
