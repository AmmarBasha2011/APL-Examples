
# apl-source:1
# مثال 1077 — عكس عدد صحيح
# apl-source:2
# Reverse integer with overflow guard
# apl-source:3
# Demonstrates: خانة خانة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1077-reverse-integer.apl
# apl-source:6

# apl-source:7
# نبني العدد المعكوس من الخانات بالباقي والقسمة
# apl-source:8
# ولو تجاوز حد 32 بت نرجع صفراً
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
def اعكس_عدد(ن):
  # apl-source:19
  اشارة = 1
  # apl-source:20
  if ن < 0:
    # apl-source:21
    اشارة = -1
    # apl-source:22
    ن = -ن
  # apl-source:23
  ناتج = 0
  # apl-source:24
  while ن > 0:
    # apl-source:25
    ناتج = (ناتج * 10) + (ن % 10)
    # apl-source:26
    ن = ن // 10
  # apl-source:27
  ناتج = ناتج * اشارة
  # apl-source:28
  if (ناتج > ((2147483648) - 1)) or (ناتج < (-(2147483648))):
    # apl-source:29
    return 0
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(اعكس_عدد(123), 321, "موجب")
# apl-source:33
تأكد_يساوي(اعكس_عدد(-123), -321, "سالب")
# apl-source:34
تأكد_يساوي(اعكس_عدد(120), 21, "صفر في النهاية")
# apl-source:35
تأكد_يساوي(اعكس_عدد(1534236469), 0, "تجاوز")
# apl-source:36
