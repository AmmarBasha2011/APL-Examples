
# apl-source:1
# مثال 4764 — المضاعف المشترك الأصغر لقائمة
# apl-source:2
# LCM of a list
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4764-lcm-of-list.apl
# apl-source:6

# apl-source:7
# المضاعف = حاصل الضرب ÷ القاسم
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
  ن = 1
  # apl-source:19
  for خ in ق:
    # apl-source:20
    أ = ن
    # apl-source:21
    ب = خ
    # apl-source:22
    while ب != 0:
      # apl-source:23
      أ, ب = ب, أ % ب
    # apl-source:24
    ن = ن * خ // أ
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([4, 6]), 12, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([2, 3, 5]), 30, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([12, 18, 24]), 72, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([7]), 7, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), 60, "حالة 5")
# apl-source:32
