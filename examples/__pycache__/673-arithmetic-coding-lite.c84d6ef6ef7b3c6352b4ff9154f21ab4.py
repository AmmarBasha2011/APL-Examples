
# apl-source:1
# مثال 673 — الترميز الحسابي المصغر
# apl-source:2
# Arithmetic coding lite
# apl-source:3
# Demonstrates: مدى احتمالي، ترميز كسور، فك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/673-arithmetic-coding-lite.apl
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
# الترميز الحسابي: رسالة كاملة في عدد واحد
# apl-source:25
# Demonstrates: مجالات متداخلة, ترميز هورنر بأساس الكلي, فك بالقلب
# apl-source:26
# النص كله يصير فترة واحدة بين عددين
# apl-source:27

# apl-source:28
رموز = ["A", "B", "C"]
# apl-source:29
تكرارات = [2, 7, 1]
# apl-source:30
تراكمي = [0, 2, 9]
# apl-source:31
كلي = 10
# apl-source:32

# apl-source:33
def رمز_من_رقم(رقم):
  # apl-source:34
  for ي in range(3):
    # apl-source:35
    if تراكمي[ي] == رقم:
      # apl-source:36
      return رموز[ي]
  # apl-source:37
  return ""
# apl-source:38

# apl-source:39
def شفر(نص):
  # apl-source:40
  منخفض = 0
  # apl-source:41
  مجال = 1
  # apl-source:42
  for حرف in نص:
    # apl-source:43
    رقم = 0
    # apl-source:44
    for ي in range(3):
      # apl-source:45
      if رموز[ي] == حرف:
        # apl-source:46
        رقم = تراكمي[ي]
        # apl-source:47
        مجال = مجال * تكرارات[ي]
    # apl-source:48
    منخفض = منخفض * كلي + رقم
  # apl-source:49
  return [منخفض, مجال]
# apl-source:50

# apl-source:51
def فك(قيمة, خطوات):
  # apl-source:52
  نص = ""
  # apl-source:53
  قوة = 1
  # apl-source:54
  for ي in range(خطوات - 1):
    # apl-source:55
    قوة = قوة * كلي
  # apl-source:56
  while قوة > 0:
    # apl-source:57
    رقم = قيمة // قوة
    # apl-source:58
    قيمة = قيمة % قوة
    # apl-source:59
    نص = نص + رمز_من_رقم(رقم)
    # apl-source:60
    قوة = قوة // كلي
  # apl-source:61
  return نص
# apl-source:62

# apl-source:63
مشفر = شفر("ABCA")
# apl-source:64
تأكد_يساوي(مشفر[0], 290, "العدد المشفر")
# apl-source:65
تأكد_يساوي(مشفر[1], 28, "عرض الفترة")
# apl-source:66
تأكد_يساوي(فك(مشفر[0], 4), "ABCA", "الفك يعيد النص")
# apl-source:67
تأكد_يساوي(فك(شفر("BBBB")[0], 4), "BBBB", "نص مكرر")
# apl-source:68
print("ABCA تساوي الفترة:", مشفر)
# apl-source:69
