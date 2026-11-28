
# apl-source:1
# مثال 654 — عداد count-min
# apl-source:2
# Count-min sketch
# apl-source:3
# Demonstrates: تقدير تكرارات، تجزئات متعددة، أدنى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/654-count-min-sketch.apl
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
# عداد count-min: تقدير تكرارات بذاكرة ثابتة
# apl-source:25
# Demonstrates: عدة تجزئات ببذور, أخذ الأدنى, خطأ جانبي واحد
# apl-source:26
# التقدير أبدا أقل من الحقيقة
# apl-source:27

# apl-source:28
عرض = 101
# apl-source:29
بذور = [7, 13, 19]
# apl-source:30

# apl-source:31
def جدول_جديد():
  # apl-source:32
  جدول = []
  # apl-source:33
  for صف in range(3):
    # apl-source:34
    جدول.append([0] * عرض)
  # apl-source:35
  return جدول
# apl-source:36

# apl-source:37
def تجزئة(نص, بذرة):
  # apl-source:38
  ح = 0
  # apl-source:39
  for حرف in نص:
    # apl-source:40
    ح = (ح * 31 + ord(حرف) + بذرة) % عرض
  # apl-source:41
  return ح
# apl-source:42

# apl-source:43
def أضف(جدول, نص, عدد):
  # apl-source:44
  for ي in range(3):
    # apl-source:45
    جدول[ي][تجزئة(نص, بذور[ي])] = جدول[ي][تجزئة(نص, بذور[ي])] + عدد
# apl-source:46

# apl-source:47
def تقدير(جدول, نص):
  # apl-source:48
  أدنى = جدول[0][تجزئة(نص, بذور[0])]
  # apl-source:49
  for ي in range(1, 3):
    # apl-source:50
    ق = جدول[ي][تجزئة(نص, بذور[ي])]
    # apl-source:51
    if ق < أدنى:
      # apl-source:52
      أدنى = ق
  # apl-source:53
  return أدنى
# apl-source:54

# apl-source:55
جدول = جدول_جديد()
# apl-source:56
أضف(جدول, "تفاح", 5)
# apl-source:57
أضف(جدول, "برتقال", 3)
# apl-source:58
أضف(جدول, "عنب", 2)
# apl-source:59
تأكد_يساوي(تقدير(جدول, "تفاح"), 5, "تفاح بلا تصادم")
# apl-source:60
تأكد_يساوي(تقدير(جدول, "برتقال"), 3, "برتقال بلا تصادم")
# apl-source:61
تأكد_يساوي(تقدير(جدول, "عنب"), 2, "عنب بلا تصادم")
# apl-source:62
تأكد_يساوي(تقدير(جدول, "تفاح") >= 5, True, "التقدير لا ينقص")
# apl-source:63
تأكد_يساوي(تقدير(جدول, "مانجو") >= 0, True, "غير موجود صفر أو تصادم")
# apl-source:64
print("تقدير تفاح:", تقدير(جدول, "تفاح"))
# apl-source:65
