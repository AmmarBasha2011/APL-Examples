
# apl-source:1
# مثال 5276 — الحد ن في متتالية هندسية أساسها 14
# apl-source:2
# Nth term of geometric sequence, ratio 14
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5276-geo-seq-14.apl
# apl-source:6

# apl-source:7
# كل حد = السابق × الأساس
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
def ف(أ, ن):
  # apl-source:18
  ر = أ
  # apl-source:19
  for ي in range(ن - 1):
    # apl-source:20
    ر = ر * 14
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(1, 1), 1, "حالة 1")
# apl-source:24
تأكد_يساوي(ف(1, 5), 38416, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(3, 4), 8232, "حالة 3")
# apl-source:26
تأكد_يساوي(ف(2, 6), 1075648, "حالة 4")
# apl-source:27
