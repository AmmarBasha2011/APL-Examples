
# apl-source:1
# مثال 3285 — ضرب كل عنصر في 39
# apl-source:2
# Multiply each item by 39
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3285-list-multiply-each-by-39.apl
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
  ر = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ر = ر + [ع * 39]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([3, 1, 2]), [117, 39, 78], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([5]), [195], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [39, 78, 117, 156, 195, 234], "حالة 3")
# apl-source:27
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [-78, 0, 273, 273, 156], "حالة 4")
# apl-source:28
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [390, 780, 390, 1170, 780, 390], "حالة 5")
# apl-source:29
