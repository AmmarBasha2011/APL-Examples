
# apl-source:1
# مثال 679 — محاذاة سميث-ووترمان
# apl-source:2
# Smith-Waterman
# apl-source:3
# Demonstrates: محاذاة محلية، برمجة ديناميكية، تتبع خلفي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/679-smith-waterman.apl
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
# سميث-ووترمان: محاذاة محلية لتسلسلين
# apl-source:25
# Demonstrates: برمجة ديناميكية بصفر أرضي, تتبع خلفي, أفضل مقطع مشترك
# apl-source:26
# يجد أقوى تشابه جزئي بين تسلسلي DNA
# apl-source:27

# apl-source:28
def محاذاة_محلية(أ, ب):
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
  أفضل = 0
  # apl-source:38
  موضع = [0, 0]
  # apl-source:39
  for ي in range(1, ن + 1):
    # apl-source:40
    for ج in range(1, م + 1):
      # apl-source:41
      تطابق = جدول[ي - 1][ج - 1]
      # apl-source:42
      if أ[ي - 1] == ب[ج - 1]:
        # apl-source:43
        تطابق = تطابق + 2
      # apl-source:44
      else:
        # apl-source:45
        تطابق = تطابق - 1
      # apl-source:46
      حذف_ق = جدول[ي - 1][ج] - 1
      # apl-source:47
      إدراج_ق = جدول[ي][ج - 1] - 1
      # apl-source:48
      قيمة = تطابق
      # apl-source:49
      if حذف_ق > قيمة:
        # apl-source:50
        قيمة = حذف_ق
      # apl-source:51
      if إدراج_ق > قيمة:
        # apl-source:52
        قيمة = إدراج_ق
      # apl-source:53
      if قيمة < 0:
        # apl-source:54
        قيمة = 0
      # apl-source:55
      جدول[ي][ج] = قيمة
      # apl-source:56
      if قيمة > أفضل:
        # apl-source:57
        أفضل = قيمة
        # apl-source:58
        موضع = [ي, ج]
  # apl-source:59
  تتبع_أ = ""
  # apl-source:60
  ي = موضع[0]
  # apl-source:61
  ج = موضع[1]
  # apl-source:62
  while ي > 0 and ج > 0 and جدول[ي][ج] > 0:
    # apl-source:63
    if جدول[ي][ج] == جدول[ي - 1][ج - 1] + 2 and أ[ي - 1] == ب[ج - 1]:
      # apl-source:64
      تتبع_أ = أ[ي - 1] + تتبع_أ
      # apl-source:65
      ي = ي - 1
      # apl-source:66
      ج = ج - 1
    # apl-source:67
    elif جدول[ي][ج] == جدول[ي - 1][ج] - 1:
      # apl-source:68
      تتبع_أ = أ[ي - 1] + تتبع_أ
      # apl-source:69
      ي = ي - 1
    # apl-source:70
    else:
      # apl-source:71
      ج = ج - 1
  # apl-source:72
  return [أفضل, تتبع_أ]
# apl-source:73

# apl-source:74
ناتج = محاذاة_محلية("AGCACACA", "ACACACTA")
# apl-source:75
تأكد_يساوي(ناتج[0], 12, "أفضل درجة محلية")
# apl-source:76
تأكد_يساوي(ناتج[1], "AGCACACA", "المقطع المتحاذي")
# apl-source:77
ناتج2 = محاذاة_محلية("AAAA", "TTTT")
# apl-source:78
تأكد_يساوي(ناتج2[0], 0, "لا تشابه صفر")
# apl-source:79
print("أفضل:", ناتج)
# apl-source:80
