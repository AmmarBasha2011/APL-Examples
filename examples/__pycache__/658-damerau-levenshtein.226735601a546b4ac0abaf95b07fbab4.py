
# apl-source:1
# مثال 658 — مسافة داميراو-لفنشتاين
# apl-source:2
# Damerau-Levenshtein
# apl-source:3
# Demonstrates: مسافة تحرير، تبديل جيران، برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/658-damerau-levenshtein.apl
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
# مسافة داميراو-لفنشتاين: تحرير مع تبديل الجيران
# apl-source:25
# Demonstrates: برمجة ديناميكية, حذف وإدراج واستبدال وتبديل
# apl-source:26
# يحسب خطأ إملائيا شائعا بتكلفة واحدة
# apl-source:27

# apl-source:28
def مسافة(أ, ب):
  # apl-source:29
  ن = len(أ)
  # apl-source:30
  م = len(ب)
  # apl-source:31
  جدول = []
  # apl-source:32
  for ي in range(ن + 1):
    # apl-source:33
    صف = []
    # apl-source:34
    for ج in range(م + 1):
      # apl-source:35
      صف.append(0)
    # apl-source:36
    جدول.append(صف)
  # apl-source:37
  for ي in range(ن + 1):
    # apl-source:38
    جدول[ي][0] = ي
  # apl-source:39
  for ج in range(م + 1):
    # apl-source:40
    جدول[0][ج] = ج
  # apl-source:41
  for ي in range(1, ن + 1):
    # apl-source:42
    for ج in range(1, م + 1):
      # apl-source:43
      تكلفة = 0
      # apl-source:44
      if أ[ي - 1] != ب[ج - 1]:
        # apl-source:45
        تكلفة = 1
      # apl-source:46
      أدنى = جدول[ي - 1][ج] + 1
      # apl-source:47
      if جدول[ي][ج - 1] + 1 < أدنى:
        # apl-source:48
        أدنى = جدول[ي][ج - 1] + 1
      # apl-source:49
      if جدول[ي - 1][ج - 1] + تكلفة < أدنى:
        # apl-source:50
        أدنى = جدول[ي - 1][ج - 1] + تكلفة
      # apl-source:51
      if ي > 1 and ج > 1 and أ[ي - 1] == ب[ج - 2] and أ[ي - 2] == ب[ج - 1]:
        # apl-source:52
        if جدول[ي - 2][ج - 2] + 1 < أدنى:
          # apl-source:53
          أدنى = جدول[ي - 2][ج - 2] + 1
      # apl-source:54
      جدول[ي][ج] = أدنى
  # apl-source:55
  return جدول[ن][م]
# apl-source:56

# apl-source:57
تأكد_يساوي(مسافة("كتاب", "كتبا"), 1, "تبديل جار واحد")
# apl-source:58
تأكد_يساوي(مسافة("مرحبا", "مرحبا"), 0, "تطابق تام")
# apl-source:59
تأكد_يساوي(مسافة("سلام", "سلم"), 1, "حذف حرف")
# apl-source:60
تأكد_يساوي(مسافة("بيت", "بنت"), 1, "استبدال حرف")
# apl-source:61
تأكد_يساوي(مسافة("مدرسة", "مدرس"), 1, "حذف أخير")
# apl-source:62
تأكد_يساوي(مسافة("", "أب"), 2, "من فارغ")
# apl-source:63
تأكد_يساوي(مسافة("كتاب", "قلم"), 4, "مختلفان تماما")
# apl-source:64
print("انتهت المسافات")
# apl-source:65
