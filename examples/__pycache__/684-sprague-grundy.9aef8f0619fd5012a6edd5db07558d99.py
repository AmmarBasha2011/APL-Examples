
# apl-source:1
# مثال 684 — سبراغ-غروندي
# apl-source:2
# Sprague-Grundy
# apl-source:3
# Demonstrates: mex، جمع نيم، ألعاب محايدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/684-sprague-grundy.apl
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
# سبراغ-غروندي: تحليل الألعاب المحايدة
# apl-source:25
# Demonstrates: أصغر عدد غائب mex, جمع نيم XOR, لعبة الطرح {1,3,4}
# apl-source:26
# الموقف خاسر عندما يكون XOR الأكوام صفرا
# apl-source:27

# apl-source:28
def غروندي_طرح(ن, خطوات):
  # apl-source:29
  جدول = []
  # apl-source:30
  for ي in range(ن + 1):
    # apl-source:31
    جدول.append(0)
  # apl-source:32
  for حجم in range(1, ن + 1):
    # apl-source:33
    مرئي = []
    # apl-source:34
    for خ in خطوات:
      # apl-source:35
      if خ <= حجم:
        # apl-source:36
        مرئي.append(جدول[حجم - خ])
    # apl-source:37
    غ = 0
    # apl-source:38
    while غ in مرئي:
      # apl-source:39
      غ = غ + 1
    # apl-source:40
    جدول[حجم] = غ
  # apl-source:41
  return جدول
# apl-source:42

# apl-source:43
خطوات = [1, 3, 4]
# apl-source:44
جدول = غروندي_طرح(12, خطوات)
# apl-source:45
تأكد_يساوي(جدول[0], 0, "الكومة الفارغة خاسرة")
# apl-source:46
تأكد_يساوي(جدول[1], 1, "غروندي 1")
# apl-source:47
تأكد_يساوي(جدول[2], 0, "غروندي 2 خاسر")
# apl-source:48
تأكد_يساوي(جدول[4], 2, "غروندي 4")
# apl-source:49
تأكد_يساوي(جدول[5], 3, "غروندي 5")
# apl-source:50
تأكد_يساوي(جدول[7], 0, "غروندي 7 خاسر")
# apl-source:51
تأكد_يساوي(جدول[9], 0, "غروندي 9 خاسر")
# apl-source:52

# apl-source:53
# لعبة من ثلاث أكوام: 3 و 4 و 7
# apl-source:54
نيم = جدول[3] ^ جدول[4] ^ جدول[7]
# apl-source:55
تأكد_يساوي(نيم, 3, "نيم الأكوام 3")
# apl-source:56
تأكد_يساوي(نيم != 0, True, "موقف رابح")
# apl-source:57
نيم2 = جدول[2] ^ جدول[7] ^ جدول[9]
# apl-source:58
تأكد_يساوي(نيم2, 0, "أكوام خاسرة مجموعها خاسر")
# apl-source:59
print("غروندي 0..12:", جدول)
# apl-source:60
