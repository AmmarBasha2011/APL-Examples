
# apl-source:1
# مثال 1693 — مجموع قطري المصفوفة
# apl-source:2
# Sum of both matrix diagonals
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1693-matrix-main-diagonal-sum.apl
# apl-source:6

# apl-source:7
# نجمع العناصر بالمؤشرين
# apl-source:8
# نطرح المركز عند الأبعاد الفردية
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
def مجموع_القطرين(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    مجموع = مجموع + م[ك][ك]
    # apl-source:23
    if ك != ن - 1 - ك:
      # apl-source:24
      مجموع = مجموع + م[ك][ن - 1 - ك]
  # apl-source:25
  return مجموع
# apl-source:26

# apl-source:27
تأكد_يساوي(مجموع_القطرين([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25, "ثلاثة")
# apl-source:28
تأكد_يساوي(مجموع_القطرين([[1, 2], [3, 4]]), 10, "اثنان")
# apl-source:29
تأكد_يساوي(مجموع_القطرين([[5]]), 5, "واحد")
# apl-source:30
