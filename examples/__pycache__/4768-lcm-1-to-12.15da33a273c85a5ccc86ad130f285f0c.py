
# apl-source:1
# مثال 4768 — أصغر عدد يقبل القسمة على كل الأعداد من 1 إلى 12
# apl-source:2
# Smallest number divisible by 1..12
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4768-lcm-1-to-12.apl
# apl-source:6

# apl-source:7
# نحسب المضاعف المشترك الأصغر تدريجيًا
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
def ف(ب):
  # apl-source:18
  ن = 1
  # apl-source:19
  for خ in range(1, ب + 1):
    # apl-source:20
    أ = ن
    # apl-source:21
    ح = خ
    # apl-source:22
    while ح != 0:
      # apl-source:23
      أ, ح = ح, أ % ح
    # apl-source:24
    ن = ن * خ // أ
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(12), 27720, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(1), 1, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(10), 2520, "حالة 3")
# apl-source:30
