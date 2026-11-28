
# apl-source:1
# مثال 1962 — الفرق المطلق بين قطري المصفوفة
# apl-source:2
# Matrix diagonal difference
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1962-matrix-diagonal-difference-abs.apl
# apl-source:6

# apl-source:7
# # العنصر i,i في القطر الرئيسي
# apl-source:8
# # والعنصر i,n-1-i في القطر الثانوي
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
def فرق_القطرين(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  ا = 0
  # apl-source:21
  ب = 0
  # apl-source:22
  for ك in range(ن):
    # apl-source:23
    ا = ا + م[ك][ك]
    # apl-source:24
    ب = ب + م[ك][ن - 1 - ك]
  # apl-source:25
  return abs(ا - ب)
# apl-source:26

# apl-source:27
تأكد_يساوي(فرق_القطرين([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15, "كلاسيكي")
# apl-source:28
تأكد_يساوي(فرق_القطرين([[1]]), 0, "عنصر")
# apl-source:29
تأكد_يساوي(فرق_القطرين([[1, 2], [3, 4]]), 0, "اثنان")
# apl-source:30
