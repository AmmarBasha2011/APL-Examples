
# apl-source:1
# مثال 4928 — كل عنصر رقم 2
# apl-source:2
# Every 2th element
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4928-every-kth-2.apl
# apl-source:6

# apl-source:7
# نستخدم الشريحة مع خطوة
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
  return ق[::2]
# apl-source:19

# apl-source:20
تأكد_يساوي(ف([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], "حالة 1")
# apl-source:21
تأكد_يساوي(ف(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]), ["a", "c", "e", "g", "i", "k", "m", "o"], "حالة 2")
# apl-source:22
تأكد_يساوي(ف([7, 8, 9]), [7, 9], "حالة 3")
# apl-source:23
