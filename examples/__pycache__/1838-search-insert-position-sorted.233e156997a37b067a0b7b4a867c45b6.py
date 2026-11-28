
# apl-source:1
# مثال 1838 — موضع الإدراج في قائمة مرتبة
# apl-source:2
# Search insert position
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1838-search-insert-position-sorted.apl
# apl-source:6

# apl-source:7
# نبحث عن أول عنصر أكبر أو مساو
# apl-source:8
# إن لم يوجد فالنهاية
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
def موضع_الإدراج(ق, هدف):
  # apl-source:19
  يسار = 0
  # apl-source:20
  يمين = len(ق)
  # apl-source:21
  while يسار < يمين:
    # apl-source:22
    وسط = (يسار + يمين) // 2
    # apl-source:23
    if ق[وسط] < هدف:
      # apl-source:24
      يسار = وسط + 1
    # apl-source:25
    else:
      # apl-source:26
      يمين = وسط
  # apl-source:27
  return يسار
# apl-source:28

# apl-source:29
تأكد_يساوي(موضع_الإدراج([1, 3, 5, 6], 5), 2, "موجود")
# apl-source:30
تأكد_يساوي(موضع_الإدراج([1, 3, 5, 6], 2), 1, "وسط")
# apl-source:31
تأكد_يساوي(موضع_الإدراج([1, 3, 5, 6], 7), 4, "نهاية")
# apl-source:32
تأكد_يساوي(موضع_الإدراج([1, 3, 5, 6], 0), 0, "بداية")
# apl-source:33
