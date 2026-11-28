
# apl-source:1
# مثال 2030 — هل يفصل النصين تعديل واحد بالضبط
# apl-source:2
# One edit distance
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2030-one-edit-distance-string-check.apl
# apl-source:6

# apl-source:7
# # نجد أول موضع اختلاف
# apl-source:8
# # ثم نقارن الباقي حسب فرق الطول
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
def تعديل_واحد(ا, ب):
  # apl-source:19
  if len(ا) > len(ب):
    # apl-source:20
    ت = ا
    # apl-source:21
    ا = ب
    # apl-source:22
    ب = ت
  # apl-source:23
  if len(ب) - len(ا) > 1:
    # apl-source:24
    return False
  # apl-source:25
  ي = 0
  # apl-source:26
  while ي < len(ا) and ا[ي] == ب[ي]:
    # apl-source:27
    ي = ي + 1
  # apl-source:28
  if ي == len(ا):
    # apl-source:29
    return len(ب) - len(ا) == 1
  # apl-source:30
  if len(ا) == len(ب):
    # apl-source:31
    return ا[ي + 1:] == ب[ي + 1:]
  # apl-source:32
  return ا[ي:] == ب[ي + 1:]
# apl-source:33

# apl-source:34
تأكد_يساوي(تعديل_واحد("ab", "acb"), True, "إدراج")
# apl-source:35
تأكد_يساوي(تعديل_واحد("ab", "ab"), False, "متساويان")
# apl-source:36
تأكد_يساوي(تعديل_واحد("a", ""), True, "حذف")
# apl-source:37
تأكد_يساوي(تعديل_واحد("abc", "adc"), True, "استبدال")
# apl-source:38
تأكد_يساوي(تعديل_واحد("abc", "xyz"), False, "ثلاثة فروق")
# apl-source:39
