
# apl-source:1
# مثال 920 — الكسور المصرية
# apl-source:2
# Egyptian fractions
# apl-source:3
# Demonstrates: جشع بكسور وحدانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/920-egyptian-fraction.apl
# apl-source:6

# apl-source:7
# الكسور المصرية: تمثيل كسر بمجموع كسور وحدانية مميزة
# apl-source:8
# الطريقة الجشعة: خذ أكبر كسر وحداني لا يتجاوز الباقي
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
# نمثل الكسر بزوج [بسط, مقام] ونطرح 1/د: ب/م - 1/د = (ب*د - م) / (م*د)
# apl-source:19
def مصرية(بسط, مقام):
  # apl-source:20
  مقامات = []
  # apl-source:21
  ب = بسط
  # apl-source:22
  م = مقام
  # apl-source:23
  while ب > 0:
    # apl-source:24
    # د = سقف(م/ب)
    # apl-source:25
    د = (م + ب - 1) // ب
    # apl-source:26
    مقامات = مقامات + [د]
    # apl-source:27
    ب = ب * د - م
    # apl-source:28
    م = م * د
  # apl-source:29
  return مقامات
# apl-source:30

# apl-source:31
ط5_6 = مصرية(5, 6)
# apl-source:32
print("5/6 =", ط5_6)
# apl-source:33
ط7_15 = مصرية(7, 15)
# apl-source:34
print("7/15 =", ط7_15)
# apl-source:35

# apl-source:36
# 5/6 = 1/2 + 1/3
# apl-source:37
تأكد_يساوي(len(ط5_6), 2, "حدان لـ 5/6")
# apl-source:38
تأكد_يساوي(ط5_6[0], 2, "النصف")
# apl-source:39
تأكد_يساوي(ط5_6[1], 3, "الثلث")
# apl-source:40

# apl-source:41
# 7/15 = 1/3 + 1/8 + 1/120
# apl-source:42
تأكد_يساوي(len(ط7_15), 3, "ثلاثة حدود لـ 7/15")
# apl-source:43
تأكد_يساوي(ط7_15[0], 3, "ثلث")
# apl-source:44
تأكد_يساوي(ط7_15[1], 8, "ثمن")
# apl-source:45
تأكد_يساوي(ط7_15[2], 120, "جزء من 120")
# apl-source:46

# apl-source:47
# التحقق الحسابي: مجموع الكسور الوحدانية يعيد الأصل (بحساب البسط والمقام)
# apl-source:48
def تحقق(مقامات, بسط, مقام):
  # apl-source:49
  ب = 0
  # apl-source:50
  م = 1
  # apl-source:51
  for د in مقامات:
    # apl-source:52
    ب = ب * د + م
    # apl-source:53
    م = م * د
  # apl-source:54
  # اختزل بالقسمة على القاسم المشترك
  # apl-source:55
  أ = ب
  # apl-source:56
  بب = م
  # apl-source:57
  while بب != 0:
    # apl-source:58
    باقي = أ % بب
    # apl-source:59
    أ = بب
    # apl-source:60
    بب = باقي
  # apl-source:61
  ب = ب // أ
  # apl-source:62
  م = م // أ
  # apl-source:63
  if ب == بسط and م == مقام:
    # apl-source:64
    return 1
  # apl-source:65
  return 0
# apl-source:66

# apl-source:67
تأكد_يساوي(تحقق(مصرية(7, 15), 7, 15), 1, "تحقق 7/15")
# apl-source:68
تأكد_يساوي(تحقق(مصرية(43, 48), 43, 48), 1, "تحقق 43/48")
# apl-source:69
