
# apl-source:1
# مثال 595 — ضريبة الدخل المصرية
# apl-source:2
# Egypt income tax
# apl-source:3
# Demonstrates: ضريبة، شرائح تصاعدية، صافي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/595-egypt-income-tax.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# ضريبة الدخل المصرية: شرائح تصاعدية (تقريبية لغرض التعلم)
# apl-source:25
# Demonstrates: شرائح متراكمة, حساب الضريبة على كل شريحة وحدها
# apl-source:26
# الشرائح المفترضة: 0-30000 إعفاء, حتى 45000 ب 15%, حتى 60000 ب 20%, حتى 200000 ب 25%, حتى 400000 ب 30%, فوقها 35%
# apl-source:27

# apl-source:28
شرائح = [[30000, 0], [45000, 15], [60000, 20], [200000, 25], [400000, 30], [1000000000000, 35]]
# apl-source:29

# apl-source:30
def احسب_ضريبة(دخل):
  # apl-source:31
  ضريبة = 0
  # apl-source:32
  بداية = 0
  # apl-source:33
  for شريحة in شرائح:
    # apl-source:34
    نهاية = شريحة[0]
    # apl-source:35
    نسبة = شريحة[1]
    # apl-source:36
    if دخل > بداية:
      # apl-source:37
      خاضع = min(دخل, نهاية) - بداية
      # apl-source:38
      ضريبة = ضريبة + خاضع * نسبة // 100
      # apl-source:39
      بداية = نهاية
  # apl-source:40
  return ضريبة
# apl-source:41

# apl-source:42
تأكد_يساوي(احسب_ضريبة(25000), 0, "دخل معفى")
# apl-source:43
تأكد_يساوي(احسب_ضريبة(50000), 3250, "شريحتان")
# apl-source:44
تأكد_يساوي(احسب_ضريبة(100000), 15250, "أربع شرائح")
# apl-source:45
print("ضريبة دخل 100000:", احسب_ضريبة(100000))
# apl-source:46
صافي = 100000 - احسب_ضريبة(100000)
# apl-source:47
print("الصافي:", صافي)
# apl-source:48
تأكد_يساوي(صافي, 84750, "الصافي بعد الضريبة")
# apl-source:49
