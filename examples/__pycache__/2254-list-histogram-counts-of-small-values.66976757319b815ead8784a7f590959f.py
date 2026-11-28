
# apl-source:1
# مثال 2254 — مدرج تكراري للقيم الصغيرة
# apl-source:2
# Histogram of 0..4
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2254-list-histogram-counts-of-small-values.apl
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
  for ي in range(5):
    # apl-source:21
    ر = ر + [ق.count(ي)]
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([0, 1, 1, 2]), [1, 2, 1, 0, 0], "حالة 1")
# apl-source:25
تأكد_يساوي(ف([4, 4, 4]), [0, 0, 0, 0, 3], "حالة 2")
# apl-source:26
تأكد_يساوي(ف([]), [0, 0, 0, 0, 0], "حالة 3")
# apl-source:27
تأكد_يساوي(ف([0, 1, 2, 3, 4]), [1, 1, 1, 1, 1], "حالة 4")
# apl-source:28
