
# apl-source:1
# مثال 1616 — جمع عددين من قوائم أرقام
# apl-source:2
# Add two numbers stored as digit lists
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1616-digit-lists-addition-carry.apl
# apl-source:6

# apl-source:7
# الرقم الأول هو الآحاد
# apl-source:8
# نحمل المرحّل للخانة التالية
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
def اجمع_القائمتين(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  مرحّل = 0
  # apl-source:21
  ي = 0
  # apl-source:22
  while ي < len(أ) or ي < len(ب) or مرحّل > 0:
    # apl-source:23
    م = مرحّل
    # apl-source:24
    if ي < len(أ):
      # apl-source:25
      م = م + أ[ي]
    # apl-source:26
    if ي < len(ب):
      # apl-source:27
      م = م + ب[ي]
    # apl-source:28
    ناتج.append(م % 10)
    # apl-source:29
    مرحّل = م // 10
    # apl-source:30
    ي = ي + 1
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(اجمع_القائمتين([2, 4, 3], [5, 6, 4]), [7, 0, 8], "342 + 465")
# apl-source:34
تأكد_يساوي(اجمع_القائمتين([9, 9], [1]), [0, 0, 1], "مرحّل")
# apl-source:35
تأكد_يساوي(اجمع_القائمتين([0], [0]), [0], "صفران")
# apl-source:36
