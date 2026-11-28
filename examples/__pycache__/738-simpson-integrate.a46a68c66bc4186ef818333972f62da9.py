
# apl-source:1
# مثال 738 — قاعدة سيمبسون
# apl-source:2
# Simpson's rule
# apl-source:3
# Demonstrates: أوزان 4-2، شرائح، تقارب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/738-simpson-integrate.apl
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
# التكامل العددي بقاعدة سيمبسون المركبة
# apl-source:25
# Demonstrates: أوزان 4-2-4-2, دالة تمرر كوسيط, تقارب مع زيادة الشرائح
# apl-source:26
# سيمبسون دقيق تماماً للكثيرات حتى الدرجة الثالثة
# apl-source:27

# apl-source:28
def سيمبسون(د, أ, ب, ش):
  # apl-source:29
  ارتفاع = (ب - أ) / ش
  # apl-source:30
  مجموع = د(أ) + د(ب)
  # apl-source:31
  for ي in range(1, ش):
    # apl-source:32
    if ي % 2 == 1:
      # apl-source:33
      مجموع = مجموع + 4 * د(أ + ي * ارتفاع)
    # apl-source:34
    else:
      # apl-source:35
      مجموع = مجموع + 2 * د(أ + ي * ارتفاع)
  # apl-source:36
  return مجموع * ارتفاع / 3
# apl-source:37

# apl-source:38
def مربع(س):
  # apl-source:39
  return س * س
# apl-source:40

# apl-source:41
def تكعيبي(س):
  # apl-source:42
  return س * س * س - 2 * س + 1
# apl-source:43

# apl-source:44
def قوة_رابعة(س):
  # apl-source:45
  return س * س * س * س
# apl-source:46

# apl-source:47
تأكد_يساوي(round(سيمبسون(مربع, 0, 2, 100), 4), 2.6667, "تكامل س^2 من 0 إلى 2")
# apl-source:48
تأكد_يساوي(round(سيمبسون(تكعيبي, 0, 2, 100), 4), 2.0, "تكعيبي دقيق تماماً")
# apl-source:49
تأكد_يساوي(round(سيمبسون(قوة_رابعة, 0, 1, 100), 6), 0.2, "س^4 من 0 إلى 1")
# apl-source:50

# apl-source:51
# التقارب: شرائح أكثر تعني خطأ أصغر لس^4
# apl-source:52
خطأ_خشن = 0.2 - سيمبسون(قوة_رابعة, 0, 1, 10)
# apl-source:53
خطأ_دقيق = 0.2 - سيمبسون(قوة_رابعة, 0, 1, 100)
# apl-source:54
if خطأ_خشن < 0:
  # apl-source:55
  خطأ_خشن = -خطأ_خشن
# apl-source:56
if خطأ_دقيق < 0:
  # apl-source:57
  خطأ_دقيق = -خطأ_دقيق
# apl-source:58
تأكد_يساوي(خطأ_دقيق < خطأ_خشن, True, "الدقة تتحسن")
# apl-source:59

# apl-source:60
تأكد_يساوي(سيمبسون(مربع, 0, 0, 10), 0, "فترة صفرية")
# apl-source:61

# apl-source:62
print("∫س^2 من 0 إلى 2 ≈", round(سيمبسون(مربع, 0, 2, 100), 4))
# apl-source:63
