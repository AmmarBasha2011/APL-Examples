
# apl-source:1
# مثال 1142 — بحث في مصفوفة
# apl-source:2
# Search a sorted 2D matrix
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1142-search-2d-matrix.apl
# apl-source:6

# apl-source:7
# نعامل المصفوفة كقائمة واحدة مرتبة
# apl-source:8
# ونحسب الصف والعمود من الفهرس
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
def موجود(م, هدف):
  # apl-source:19
  if len(م) == 0:
    # apl-source:20
    return False
  # apl-source:21
  ع = len(م[0])
  # apl-source:22
  يسار = 0
  # apl-source:23
  يمين = len(م) * ع - 1
  # apl-source:24
  while يسار <= يمين:
    # apl-source:25
    وسط = (يسار + يمين) // 2
    # apl-source:26
    ق = م[وسط // ع][وسط % ع]
    # apl-source:27
    if ق == هدف:
      # apl-source:28
      return True
    # apl-source:29
    elif ق < هدف:
      # apl-source:30
      يسار = وسط + 1
    # apl-source:31
    else:
      # apl-source:32
      يمين = وسط - 1
  # apl-source:33
  return False
# apl-source:34

# apl-source:35
م = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# apl-source:36
تأكد_يساوي(موجود(م, 3), True, "موجود")
# apl-source:37
تأكد_يساوي(موجود(م, 13), False, "غير موجود")
# apl-source:38
تأكد_يساوي(موجود(م, 60), True, "الأخير")
# apl-source:39
تأكد_يساوي(موجود([], 1), False, "فارغة")
# apl-source:40
