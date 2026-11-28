
# apl-source:1
# مثال 958 — الجدولة المرجحة للفترات
# apl-source:2
# Weighted interval scheduling
# apl-source:3
# Demonstrates: ديناميكية مع متوافق سابق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/958-weighted-interval.apl
# apl-source:6

# apl-source:7
# الجدولة المرجحة للفترات: أقصى ربح بفترات غير متداخلة
# apl-source:8
# برمجة ديناميكية مع البحث عن آخر فترة متوافقة
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
# الفترات [بداية، نهاية، ربح] مرتبة حسب النهاية
# apl-source:19
فترات = [[1, 3, 50], [3, 5, 20], [6, 19, 100], [2, 100, 200]]
# apl-source:20

# apl-source:21
def متوافقة_قبل(فهرس):
  # apl-source:22
  for ج in range(فهرس - 1, -1, -1):
    # apl-source:23
    if فترات[ج][1] <= فترات[فهرس][0]:
      # apl-source:24
      return ج
  # apl-source:25
  return -1
# apl-source:26

# apl-source:27
def أقصى_ربح():
  # apl-source:28
  ن = len(فترات)
  # apl-source:29
  جدول = [0]
  # apl-source:30
  for ك in range(ن):
    # apl-source:31
    سابق = متوافقة_قبل(ك)
    # apl-source:32
    if سابق >= 0:
      # apl-source:33
      مع = جدول[سابق + 1] + فترات[ك][2]
    # apl-source:34
    else:
      # apl-source:35
      مع = فترات[ك][2]
    # apl-source:36
    بدون = جدول[ك]
    # apl-source:37
    if مع > بدون:
      # apl-source:38
      جدول = جدول + [مع]
    # apl-source:39
    else:
      # apl-source:40
      جدول = جدول + [بدون]
  # apl-source:41
  return جدول[ن]
# apl-source:42

# apl-source:43
تأكد_يساوي(أقصى_ربح(), 200, "الربح الأقصى")
# apl-source:44
تأكد_يساوي(متوافقة_قبل(2), 1, "متوافق قبل الثالثة")
# apl-source:45
تأكد_يساوي(متوافقة_قبل(3), -1, "لا متوافق قبل الرابعة")
# apl-source:46
