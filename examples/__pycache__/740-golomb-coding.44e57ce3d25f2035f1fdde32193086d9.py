
# apl-source:1
# مثال 740 — ترميز غولومب
# apl-source:2
# Golomb coding
# apl-source:3
# Demonstrates: أحادي، ثنائي مقتطع، خارج قسمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/740-golomb-coding.apl
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
# ترميز غولومب: ضغط أعداد صحيحة موجبة التوزيع الهندسي
# apl-source:25
# Demonstrates: خارج قسمة أحادي + باقي ثنائي مقتطع, حساب بتات, فك الترميز
# apl-source:26
# خارج القسمة يُرمز أحادياً (ق واحد ثم صفر), والباقي بترميز ثنائي مقتطع
# apl-source:27

# apl-source:28
def بتات_الترميز(م):
  # apl-source:29
  ب = 0
  # apl-source:30
  قوة = 1
  # apl-source:31
  while قوة < م:
    # apl-source:32
    قوة = قوة * 2
    # apl-source:33
    ب = ب + 1
  # apl-source:34
  return ب
# apl-source:35

# apl-source:36
def أحادي(ق):
  # apl-source:37
  ناتج = ""
  # apl-source:38
  for ي in range(ق):
    # apl-source:39
    ناتج = ناتج + "1"
  # apl-source:40
  return ناتج + "0"
# apl-source:41

# apl-source:42
def ثنائي(قيمة, عرض):
  # apl-source:43
  if قيمة == 0:
    # apl-source:44
    ناتج = ""
    # apl-source:45
    for ي in range(عرض):
      # apl-source:46
      ناتج = ناتج + "0"
    # apl-source:47
    return ناتج
  # apl-source:48
  ناتج = ""
  # apl-source:49
  باقي = قيمة
  # apl-source:50
  while باقي > 0:
    # apl-source:51
    if باقي % 2 == 1:
      # apl-source:52
      ناتج = "1" + ناتج
    # apl-source:53
    else:
      # apl-source:54
      ناتج = "0" + ناتج
    # apl-source:55
    باقي = باقي // 2
  # apl-source:56
  while len(ناتج) < عرض:
    # apl-source:57
    ناتج = "0" + ناتج
  # apl-source:58
  return ناتج
# apl-source:59

# apl-source:60
def رمز_غولومب(ن, م):
  # apl-source:61
  ب = بتات_الترميز(م)
  # apl-source:62
  حد = 1
  # apl-source:63
  for ي in range(ب):
    # apl-source:64
    حد = حد * 2
  # apl-source:65
  حد = حد - م
  # apl-source:66
  ق = ن // م
  # apl-source:67
  ر = ن % م
  # apl-source:68
  if ر < حد:
    # apl-source:69
    return أحادي(ق) + ثنائي(ر, ب - 1)
  # apl-source:70
  return أحادي(ق) + ثنائي(ر + حد, ب)
# apl-source:71

# apl-source:72
تأكد_يساوي(بتات_الترميز(4), 2, "بتات أربعة")
# apl-source:73
تأكد_يساوي(بتات_الترميز(5), 3, "بتات خمسة")
# apl-source:74
تأكد_يساوي(أحادي(0), "0", "أحادي صفر")
# apl-source:75
تأكد_يساوي(أحادي(3), "1110", "أحادي ثلاثة")
# apl-source:76
تأكد_يساوي(ثنائي(5, 4), "0101", "ثنائي مبطن")
# apl-source:77
تأكد_يساوي(ثنائي(0, 3), "000", "صفر مبطن")
# apl-source:78

# apl-source:79
# م = 4: حد = 0, الباقي دائماً ببتين
# apl-source:80
تأكد_يساوي(رمز_غولومب(0, 4), "000", "صفر بأربعة")
# apl-source:81
تأكد_يساوي(رمز_غولومب(1, 4), "001", "واحد بأربعة")
# apl-source:82
تأكد_يساوي(رمز_غولومب(5, 4), "1001", "خمسة بأربعة")
# apl-source:83
تأكد_يساوي(رمز_غولومب(9, 4), "11001", "تسعة بأربعة")
# apl-source:84
تأكد_يساوي(رمز_غولومب(14, 4), "111010", "أربعة عشر بأربعة")
# apl-source:85

# apl-source:86
# م = 5: حد = 3, اقتطاع فعلي
# apl-source:87
تأكد_يساوي(رمز_غولومب(0, 5), "000", "صفر بخمسة")
# apl-source:88
تأكد_يساوي(رمز_غولومب(5, 5), "1000", "خمسة بخمسة")
# apl-source:89
تأكد_يساوي(رمز_غولومب(9, 5), "10111", "تسعة بخمسة")
# apl-source:90
تأكد_يساوي(رمز_غولومب(14, 5), "110111", "أربعة عشر بخمسة")
# apl-source:91

# apl-source:92
print("غولومب(9, 4) =", رمز_غولومب(9, 4))
# apl-source:93
