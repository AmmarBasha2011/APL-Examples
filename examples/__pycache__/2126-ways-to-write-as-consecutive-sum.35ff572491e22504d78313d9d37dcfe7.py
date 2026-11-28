
# apl-source:1
# مثال 2126 — طرق كتابة العدد كمجموع متتالية
# apl-source:2
# Consecutive integer sum ways
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2126-ways-to-write-as-consecutive-sum.apl
# apl-source:6

# apl-source:7
# # 15 له أربع طرق
# apl-source:8
# # عدد الطرق يساوي عدد القواسم الفردية
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
def طرق(ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  for بداية in range(1, ن + 1):
    # apl-source:21
    مج = 0
    # apl-source:22
    ي = بداية
    # apl-source:23
    while مج < ن:
      # apl-source:24
      مج = مج + ي
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    if مج == ن:
      # apl-source:27
      عدد = عدد + 1
  # apl-source:28
  return عدد
# apl-source:29

# apl-source:30
تأكد_يساوي(طرق(15), 4, "١٥")
# apl-source:31
تأكد_يساوي(طرق(9), 3, "٩")
# apl-source:32
تأكد_يساوي(طرق(1), 1, "١")
# apl-source:33
تأكد_يساوي(طرق(16), 1, "١٦")
# apl-source:34
