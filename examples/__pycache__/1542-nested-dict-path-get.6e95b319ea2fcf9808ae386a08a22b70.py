
# apl-source:1
# مثال 1542 — قراءة قيمة متداخلة بمسار
# apl-source:2
# Nested dictionary path lookup
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1542-nested-dict-path-get.apl
# apl-source:6

# apl-source:7
# نتدرج مفتاحاً بعد آخر
# apl-source:8
# إن غاب مفتاح نرجع القيمة الافتراضية
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
def اقرأ_المسار(ق, مسار, افتراضي):
  # apl-source:19
  حالي = ق
  # apl-source:20
  for ك in مسار:
    # apl-source:21
    if type(حالي) != type({}):
      # apl-source:22
      return افتراضي
    # apl-source:23
    if ك in حالي:
      # apl-source:24
      حالي = حالي[ك]
    # apl-source:25
    else:
      # apl-source:26
      return افتراضي
  # apl-source:27
  return حالي
# apl-source:28

# apl-source:29
بيانات = {"مستخدم": {"اسم": "علي", "عنوان": {"مدينة": "المنصورة"}}}
# apl-source:30
تأكد_يساوي(اقرأ_المسار(بيانات, ["مستخدم", "اسم"], "؟"), "علي", "مستوى ثان")
# apl-source:31
تأكد_يساوي(اقرأ_المسار(بيانات, ["مستخدم", "عنوان", "مدينة"], "؟"), "المنصورة", "مستوى ثالث")
# apl-source:32
تأكد_يساوي(اقرأ_المسار(بيانات, ["مستخدم", "هاتف"], "غير معروف"), "غير معروف", "غائب")
# apl-source:33
