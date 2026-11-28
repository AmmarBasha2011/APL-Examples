
# apl-source:1
# مثال 778 — محاذاة نيدلمان-فنش
# apl-source:2
# Needleman-Wunsch
# apl-source:3
# Demonstrates: ديناميكية شاملة، تتبع خلفي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/778-needleman-wunsch.apl
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
# محاذاة نيدلمان-فنش الشاملة لتسلسلين
# apl-source:25
# Demonstrates: برمجة ديناميكية ثنائية, تتبع خلفي, درجات تطابق/فجوة
# apl-source:26
# خلافاً عن سميث-ووترمان (محلية), هذه محاذاة شاملة من الطرف للطرف
# apl-source:27

# apl-source:28
def محاذاة_شاملة(أ, ب):
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
    صف = جدول[ي]
    # apl-source:39
    صف[0] = 0 - ي
  # apl-source:40
  for ج in range(م + 1):
    # apl-source:41
    صف = جدول[0]
    # apl-source:42
    صف[ج] = 0 - ج
  # apl-source:43
  for ي in range(1, ن + 1):
    # apl-source:44
    for ج in range(1, م + 1):
      # apl-source:45
      if أ[ي - 1] == ب[ج - 1]:
        # apl-source:46
        ق = 1
      # apl-source:47
      else:
        # apl-source:48
        ق = -1
      # apl-source:49
      قطري = جدول[ي - 1][ج - 1] + ق
      # apl-source:50
      اعلى = جدول[ي - 1][ج] - 1
      # apl-source:51
      يسار = جدول[ي][ج - 1] - 1
      # apl-source:52
      افضل = قطري
      # apl-source:53
      if اعلى > افضل:
        # apl-source:54
        افضل = اعلى
      # apl-source:55
      if يسار > افضل:
        # apl-source:56
        افضل = يسار
      # apl-source:57
      صف = جدول[ي]
      # apl-source:58
      صف[ج] = افضل
  # apl-source:59
  محاذاة_أ = ""
  # apl-source:60
  محاذاة_ب = ""
  # apl-source:61
  ي = ن
  # apl-source:62
  ج = م
  # apl-source:63
  while ي > 0 or ج > 0:
    # apl-source:64
    تم = False
    # apl-source:65
    if ي > 0 and ج > 0:
      # apl-source:66
      if أ[ي - 1] == ب[ج - 1]:
        # apl-source:67
        ق = 1
      # apl-source:68
      else:
        # apl-source:69
        ق = -1
      # apl-source:70
      if جدول[ي][ج] == جدول[ي - 1][ج - 1] + ق:
        # apl-source:71
        محاذاة_أ = أ[ي - 1] + محاذاة_أ
        # apl-source:72
        محاذاة_ب = ب[ج - 1] + محاذاة_ب
        # apl-source:73
        ي = ي - 1
        # apl-source:74
        ج = ج - 1
        # apl-source:75
        تم = True
    # apl-source:76
    if تم == False and ي > 0 and جدول[ي][ج] == جدول[ي - 1][ج] - 1:
      # apl-source:77
      محاذاة_أ = أ[ي - 1] + محاذاة_أ
      # apl-source:78
      محاذاة_ب = "-" + محاذاة_ب
      # apl-source:79
      ي = ي - 1
      # apl-source:80
      تم = True
    # apl-source:81
    if تم == False:
      # apl-source:82
      محاذاة_أ = "-" + محاذاة_أ
      # apl-source:83
      محاذاة_ب = ب[ج - 1] + محاذاة_ب
      # apl-source:84
      ج = ج - 1
  # apl-source:85
  return [جدول[ن][م], محاذاة_أ, محاذاة_ب]
# apl-source:86

# apl-source:87
ن1 = محاذاة_شاملة("GATTACA", "GCATGCU")
# apl-source:88
تأكد_يساوي(ن1[0], 0, "درجة GATTACA/GCATGCU")
# apl-source:89
تأكد_يساوي(ن1[1], "G-ATTACA", "محاذاة أولى")
# apl-source:90
تأكد_يساوي(ن1[2], "GCA-TGCU", "محاذاة ثانية")
# apl-source:91
ن2 = محاذاة_شاملة("ACGT", "AAGT")
# apl-source:92
تأكد_يساوي(ن2[0], 2, "درجة ACGT/AAGT")
# apl-source:93
تأكد_يساوي(ن2[1], "ACGT", "محاذاة 2 أولى")
# apl-source:94
تأكد_يساوي(ن2[2], "AAGT", "محاذاة 2 ثانية")
# apl-source:95
ن3 = محاذاة_شاملة("AGT", "AGT")
# apl-source:96
تأكد_يساوي(ن3[0], 3, "تطابق تام")
# apl-source:97
