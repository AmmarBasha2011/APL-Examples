
# apl-source:1
# مثال 815 — النقل العمودي
# apl-source:2
# Columnar transposition
# apl-source:3
# Demonstrates: ترتيب أعمدة بالمفتاح، صفوف ناقصة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/815-columnar-transposition.apl
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
# شفرة النقل العمودي: كتابة بصفوف وقراءة بأعمدة حسب ترتيب المفتاح
# apl-source:25
# Demonstrates: ترتيب أعمدة أبجدي, صفوف غير مكتملة, فك بالعكس
# apl-source:26

# apl-source:27
def ترتيب_مفتاح(مفتاح):
  # apl-source:28
  دلائل = []
  # apl-source:29
  for ي in range(len(مفتاح)):
    # apl-source:30
    دلائل.append(ي)
  # apl-source:31
  for ي in range(len(دلائل)):
    # apl-source:32
    أدنى = ي
    # apl-source:33
    for ج in range(ي + 1, len(دلائل)):
      # apl-source:34
      if مفتاح[دلائل[ج]] < مفتاح[دلائل[أدنى]]:
        # apl-source:35
        أدنى = ج
    # apl-source:36
    مؤقت = دلائل[ي]
    # apl-source:37
    دلائل[ي] = دلائل[أدنى]
    # apl-source:38
    دلائل[أدنى] = مؤقت
  # apl-source:39
  return دلائل
# apl-source:40

# apl-source:41
def شفر_عمودي(نص, مفتاح):
  # apl-source:42
  ن = len(مفتاح)
  # apl-source:43
  ترتيب = ترتيب_مفتاح(مفتاح)
  # apl-source:44
  ناتج = ""
  # apl-source:45
  for عمود in ترتيب:
    # apl-source:46
    صف = 0
    # apl-source:47
    while صف * ن + عمود < len(نص):
      # apl-source:48
      ناتج = ناتج + نص[صف * ن + عمود]
      # apl-source:49
      صف = صف + 1
  # apl-source:50
  return ناتج
# apl-source:51

# apl-source:52
تأكد_يساوي(ترتيب_مفتاح("ZEBRA"), [4, 2, 1, 3, 0], "ترتيب ZEBRA")
# apl-source:53
تأكد_يساوي(شفر_عمودي("WEAREDISCOVERED", "ZEBRA"), "EODASREIERCEWDV", "تشفير كلاسيكي")
# apl-source:54
تأكد_يساوي(شفر_عمودي("HELLOWORLD", "KEY"), "EORHLODLWL", "تشفير قصير")
# apl-source:55
تأكد_يساوي(len(شفر_عمودي("ABCDEFG", "DCBA")), 7, "الطول محفوظ")
# apl-source:56
