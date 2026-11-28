
# apl-source:1
# مثال 807 — تقسيمات الأعداد
# apl-source:2
# Integer partitions
# apl-source:3
# Demonstrates: ديناميكية، تعديد عودي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/807-integer-partitions.apl
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
# عدّ تقسيمات العدد الصحيح p(n): ببرمجة ديناميكية وتعديد عودي
# apl-source:25
# Demonstrates: جدول مسارات جزئية, تعديد تنازلي غير متزايد, ثوابت أويلر
# apl-source:26

# apl-source:27
def عدد_التقسيمات(ن):
  # apl-source:28
  جدول = []
  # apl-source:29
  for ي in range(ن + 1):
    # apl-source:30
    جدول.append(0)
  # apl-source:31
  جدول[0] = 1
  # apl-source:32
  for ك in range(1, ن + 1):
    # apl-source:33
    for ج in range(ك, ن + 1):
      # apl-source:34
      جدول[ج] = جدول[ج] + جدول[ج - ك]
  # apl-source:35
  return جدول[ن]
# apl-source:36

# apl-source:37
def عدّد(ن, أقصى):
  # apl-source:38
  if ن == 0:
    # apl-source:39
    return [[]]
  # apl-source:40
  نتيجة = []
  # apl-source:41
  بداية = ن
  # apl-source:42
  if أقصى < ن:
    # apl-source:43
    بداية = أقصى
  # apl-source:44
  ي = بداية
  # apl-source:45
  while ي >= 1:
    # apl-source:46
    for باقي in عدّد(ن - ي, ي):
      # apl-source:47
      تقسيم = [ي]
      # apl-source:48
      for جزء in باقي:
        # apl-source:49
        تقسيم.append(جزء)
      # apl-source:50
      نتيجة.append(تقسيم)
    # apl-source:51
    ي = ي - 1
  # apl-source:52
  return نتيجة
# apl-source:53

# apl-source:54
تأكد_يساوي(عدد_التقسيمات(5), 7, "تقسيمات خمسة")
# apl-source:55
تأكد_يساوي(عدد_التقسيمات(10), 42, "تقسيمات عشرة")
# apl-source:56
تأكد_يساوي(عدد_التقسيمات(20), 627, "تقسيمات عشرين")
# apl-source:57
تأكد_يساوي(عدّد(4, 4), [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]], "تعديد الأربعة")
# apl-source:58
تأكد_يساوي(len(عدّد(5, 5)), عدد_التقسيمات(5), "تطابق العد والتعديد")
# apl-source:59
