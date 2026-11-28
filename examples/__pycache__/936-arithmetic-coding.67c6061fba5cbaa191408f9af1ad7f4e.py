
# apl-source:1
# مثال 936 — الترميز الحسابي
# apl-source:2
# Arithmetic coding
# apl-source:3
# Demonstrates: تضييق مدى كسري
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/936-arithmetic-coding.apl
# apl-source:6

# apl-source:7
# الترميز الحسابي: ضغط السلسلة كلها في كسر واحد من [0,1)
# apl-source:8
# كل رمز يضيق المدى حسب احتماله التراكمي
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
# نمثل الكسور بأزواج [بسط, مقام] لتفادي أخطاء الفاصلة
# apl-source:19
# الترددات ثابتة: A=3 B=1 C=1 من 5... نستخدم نموذجاً مبنياً من السلسلة نفسها
# apl-source:20
def رمز_حسابياً(سلسلة):
  # apl-source:21
  # احسب الترددات
  # apl-source:22
  رموز = []
  # apl-source:23
  تردد = []
  # apl-source:24
  for i in range(len(سلسلة)):
    # apl-source:25
    حرف = سلسلة[i]
    # apl-source:26
    موضع = -1
    # apl-source:27
    for ج in range(len(رموز)):
      # apl-source:28
      if رموز[ج] == حرف:
        # apl-source:29
        موضع = ج
    # apl-source:30
    if موضع >= 0:
      # apl-source:31
      تردد[موضع] = تردد[موضع] + 1
    # apl-source:32
    else:
      # apl-source:33
      رموز = رموز + [حرف]
      # apl-source:34
      تردد = تردد + [1]
  # apl-source:35
  مجموع = len(سلسلة)
  # apl-source:36
  أدنى_ب = 0
  # apl-source:37
  أدنى_م = 1
  # apl-source:38
  أعلى_ب = 1
  # apl-source:39
  أعلى_م = 1
  # apl-source:40
  for i in range(len(سلسلة)):
    # apl-source:41
    حرف = سلسلة[i]
    # apl-source:42
    # التراكمي قبل الحرف وعرضه
    # apl-source:43
    قبل = 0
    # apl-source:44
    عرض = 0
    # apl-source:45
    for ج in range(len(رموز)):
      # apl-source:46
      if رموز[ج] == حرف:
        # apl-source:47
        عرض = تردد[ج]
      # apl-source:48
      elif عرض == 0:
        # apl-source:49
        قبل = قبل + تردد[ج]
    # apl-source:50
    # مدى = أعلى - أدنى
    # apl-source:51
    مدى_ب = أعلى_ب * أدنى_م - أدنى_ب * أعلى_م
    # apl-source:52
    مدى_م = أعلى_م * أدنى_م
    # apl-source:53
    # أعلى جديد = أدنى + مدى * (قبل+عرض)/مجموع
    # apl-source:54
    ج_أعلى_ب = أدنى_ب * مدى_م * مجموع + مدى_ب * (قبل + عرض) * أدنى_م
    # apl-source:55
    ج_أعلى_م = أدنى_م * مدى_م * مجموع
    # apl-source:56
    # أدنى جديد = أدنى + مدى * قبل/مجموع
    # apl-source:57
    ج_أدنى_ب = أدنى_ب * مدى_م * مجموع + مدى_ب * قبل * أدنى_م
    # apl-source:58
    ج_أدنى_م = أدنى_م * مدى_م * مجموع
    # apl-source:59
    أدنى_ب = ج_أدنى_ب
    # apl-source:60
    أدنى_م = ج_أدنى_م
    # apl-source:61
    أعلى_ب = ج_أعلى_ب
    # apl-source:62
    أعلى_م = ج_أعلى_م
  # apl-source:63
  return [[أدنى_ب, أدنى_م], [أعلى_ب, أعلى_م]]
# apl-source:64

# apl-source:65
ناتج = رمز_حسابياً("ABAC")
# apl-source:66
أدنى = ناتج[0][0] / ناتج[0][1]
# apl-source:67
أعلى = ناتج[1][0] / ناتج[1][1]
# apl-source:68
print("المدى:", أدنى, "إلى", أعلى)
# apl-source:69

# apl-source:70
# الترددات: A=2 B=1 C=1 من 4. الترميز يعطي [0.296875, 0.3125)
# apl-source:71
تأكد_يساوي(round(أدنى, 6), 0.296875, "الحد الأدنى")
# apl-source:72
تأكد_يساوي(round(أعلى, 6), 0.3125, "الحد الأعلى")
# apl-source:73

# apl-source:74
# ترتيب الرموز يغير المدى لكن الاحتمال الكلي ثابت
# apl-source:75
ناتج2 = رمز_حسابياً("AA")
# apl-source:76
أدنى2 = ناتج2[0][0] / ناتج2[0][1]
# apl-source:77
أعلى2 = ناتج2[1][0] / ناتج2[1][1]
# apl-source:78
تأكد_يساوي(round(أدنى2, 6), 0, "AA أدنى")
# apl-source:79
تأكد_يساوي(round(أعلى2, 6), 1, "AA أعلى: رمز واحد يملأ المدى")
# apl-source:80
