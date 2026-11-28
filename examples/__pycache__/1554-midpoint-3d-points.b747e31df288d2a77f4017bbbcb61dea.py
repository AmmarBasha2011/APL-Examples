
# apl-source:1
# مثال 1554 — منتصف قطعة في الفراغ
# apl-source:2
# Midpoint of a 3D segment
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1554-midpoint-3d-points.apl
# apl-source:6

# apl-source:7
# الوسط هو متوسط الطرفين
# apl-source:8
# نحسبه لكل محور
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
def منتصف(أ, ب):
  # apl-source:19
  return [(أ[0] + ب[0]) / 2, (أ[1] + ب[1]) / 2, (أ[2] + ب[2]) / 2]
# apl-source:20

# apl-source:21
تأكد_يساوي(منتصف([0, 0, 0], [2, 4, 6]), [1.0, 2.0, 3.0], "من الأصل")
# apl-source:22
تأكد_يساوي(منتصف([-2, 0, 4], [2, 2, 0]), [0.0, 1.0, 2.0], "سالب")
# apl-source:23
تأكد_يساوي(منتصف([5, 5, 5], [5, 5, 5]), [5.0, 5.0, 5.0], "نقطة")
# apl-source:24
