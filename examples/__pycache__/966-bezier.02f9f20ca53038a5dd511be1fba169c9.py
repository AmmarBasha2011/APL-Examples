
# apl-source:1
# مثال 966 — منحنى بيزيه التربيعي
# apl-source:2
# Quadratic Bezier curve
# apl-source:3
# Demonstrates: ترجيح ثلاثي بالتحكم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/966-bezier.apl
# apl-source:6

# apl-source:7
# منحنى بيزيه التربيعي: تقييم نقطة على المنحنى عند معامل ت
# apl-source:8
# ترجيح ثلاثي بنقاط التحكم
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
def بيزيه(ن0, ن1, ن2, ت):
  # apl-source:19
  أ = (1 - ت) * (1 - ت)
  # apl-source:20
  ب = 2 * (1 - ت) * ت
  # apl-source:21
  ج = ت * ت
  # apl-source:22
  س = (أ * ن0[0]) + (ب * ن1[0]) + (ج * ن2[0])
  # apl-source:23
  ص = (أ * ن0[1]) + (ب * ن1[1]) + (ج * ن2[1])
  # apl-source:24
  return [س, ص]
# apl-source:25

# apl-source:26
نقطة1 = بيزيه([0, 0], [2, 4], [4, 0], 0.5)
# apl-source:27
نقطة2 = بيزيه([0, 0], [2, 4], [4, 0], 0.25)
# apl-source:28
تأكد_يساوي(round(نقطة1[0], 6), 2, "س عند المنتصف")
# apl-source:29
تأكد_يساوي(round(نقطة1[1], 6), 2, "ص عند المنتصف")
# apl-source:30
تأكد_يساوي(round(نقطة2[0], 6), 1, "س عند الربع")
# apl-source:31
تأكد_يساوي(round(نقطة2[1], 6), 1.5, "ص عند الربع")
# apl-source:32
