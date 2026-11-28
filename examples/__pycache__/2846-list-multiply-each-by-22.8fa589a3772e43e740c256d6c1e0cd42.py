
# apl-source:1
# مثال 2846 — ضرب كل عنصر في 22
# apl-source:2
# Multiply each item by 22
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2846-list-multiply-each-by-22.apl
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
    ر = ر + [ع * 22]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([3, 1, 2]), [66, 22, 44], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([5]), [110], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [22, 44, 66, 88, 110, 132], "حالة 3")
# apl-source:27
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [-44, 0, 154, 154, 88], "حالة 4")
# apl-source:28
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [220, 440, 220, 660, 440, 220], "حالة 5")
# apl-source:29
