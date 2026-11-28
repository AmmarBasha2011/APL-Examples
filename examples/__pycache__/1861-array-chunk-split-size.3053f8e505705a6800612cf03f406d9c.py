
# apl-source:1
# مثال 1861 — تقسيم القائمة لأجزاء
# apl-source:2
# Split list into chunks
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1861-array-chunk-split-size.apl
# apl-source:6

# apl-source:7
# نأخذ ك عنصراً في كل مرة
# apl-source:8
# الجزء الأخير قد يكون أقصر
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
def قسّم(ق, ك):
  # apl-source:19
  ناتج = []
  # apl-source:20
  ي = 0
  # apl-source:21
  while ي < len(ق):
    # apl-source:22
    ناتج.append(ق[ي:ي + ك])
    # apl-source:23
    ي = ي + ك
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(قسّم([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]], "ناقص")
# apl-source:27
تأكد_يساوي(قسّم([1, 2, 3, 4], 2), [[1, 2], [3, 4]], "تام")
# apl-source:28
تأكد_يساوي(قسّم([], 3), [], "فارغة")
# apl-source:29
