
# apl-source:1
# مثال 1730 — الرقم المفقود
# apl-source:2
# Missing number from 0 to n
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1730-missing-number-in-range.apl
# apl-source:6

# apl-source:7
# مجموع 0 إلى ن معروف
# apl-source:8
# المفقود هو الفرق
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
def مفقود(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  متوقع = ن * (ن + 1) // 2
  # apl-source:21
  فعلي = 0
  # apl-source:22
  for ع in ق:
    # apl-source:23
    فعلي = فعلي + ع
  # apl-source:24
  return متوقع - فعلي
# apl-source:25

# apl-source:26
تأكد_يساوي(مفقود([3, 0, 1]), 2, "اثنان")
# apl-source:27
تأكد_يساوي(مفقود([0, 1]), 2, "الأخير")
# apl-source:28
تأكد_يساوي(مفقود([1]), 0, "الأول")
# apl-source:29
