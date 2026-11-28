
# apl-source:1
# مثال 5311 — مقارنة العدد مع 17
# apl-source:2
# Compare number with 17
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5311-triple-compare-17.apl
# apl-source:6

# apl-source:7
# نرجع نصاً: اصغر او اكبر او يساوي
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
def ف(ن):
  # apl-source:18
  if ن < 17:
    # apl-source:19
    return "اصغر"
  # apl-source:20
  elif ن > 17:
    # apl-source:21
    return "اكبر"
  # apl-source:22
  return "يساوي"
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(16), "اصغر", "حالة 1")
# apl-source:25
تأكد_يساوي(ف(17), "يساوي", "حالة 2")
# apl-source:26
تأكد_يساوي(ف(18), "اكبر", "حالة 3")
# apl-source:27
تأكد_يساوي(ف(0), "اصغر", "حالة 4")
# apl-source:28
