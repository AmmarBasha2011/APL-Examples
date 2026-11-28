
# apl-source:1
# مثال 4936 — تقسيم القائمة إلى أجزاء بحجم 4
# apl-source:2
# Chunk list into size 4
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4936-chunk-4.apl
# apl-source:6

# apl-source:7
# كل جزء 4 عناصر
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ق):
  # apl-source:18
  ر = []
  # apl-source:19
  ي = 0
  # apl-source:20
  while ي < len(ق):
    # apl-source:21
    ر = ر + [ق[ي:ي + 4]]
    # apl-source:22
    ي = ي + 4
  # apl-source:23
  return ر
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]], "حالة 1")
# apl-source:26
تأكد_يساوي(ف([]), [], "حالة 2")
# apl-source:27
تأكد_يساوي(ف(["a", "b", "c", "d", "e", "f", "g"]), [["a", "b", "c", "d"], ["e", "f", "g"]], "حالة 3")
# apl-source:28
