
# apl-source:1
# مثال 1976 — عدد أضلاع شاشة السبع قطع
# apl-source:2
# Seven segment lit count
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1976-seven-segment-lit-segments-total.apl
# apl-source:6

# apl-source:7
# # الأرقام من 0 إلى 9 تستخدم 6 و2 و5 و5 و4 و5 و6 و3 و7 و6 قطع
# apl-source:8
# # نجمع القطع لكل رقم في العدد
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
def قطع(ن):
  # apl-source:19
  جدول = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
  # apl-source:20
  مج = 0
  # apl-source:21
  for ر in str(ن):
    # apl-source:22
    مج = مج + جدول[int(ر)]
  # apl-source:23
  return مج
# apl-source:24

# apl-source:25
تأكد_يساوي(قطع(1234), 16, "١٢٣٤")
# apl-source:26
تأكد_يساوي(قطع(8), 7, "٨")
# apl-source:27
تأكد_يساوي(قطع(100), 14, "١٠٠")
# apl-source:28
تأكد_يساوي(قطع(0), 6, "صفر")
# apl-source:29
