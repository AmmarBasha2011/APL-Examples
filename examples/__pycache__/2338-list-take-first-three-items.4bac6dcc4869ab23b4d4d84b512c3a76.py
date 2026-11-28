
# apl-source:1
# مثال 2338 — أول ثلاثة عناصر
# apl-source:2
# Take first three
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2338-list-take-first-three-items.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  return ق[:3]
# apl-source:20

# apl-source:21
تأكد_يساوي(ف([1, 2, 3, 4]), [1, 2, 3], "حالة 1")
# apl-source:22
تأكد_يساوي(ف([1]), [1], "حالة 2")
# apl-source:23
تأكد_يساوي(ف([]), [], "حالة 3")
# apl-source:24
تأكد_يساوي(ف([5, 6, 7]), [5, 6, 7], "حالة 4")
# apl-source:25
