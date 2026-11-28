
# apl-source:1
# مثال 975 — رمز لوجندر
# apl-source:2
# Legendre symbol
# apl-source:3
# Demonstrates: معيار أويلر بالأس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/975-legendre-symbol.apl
# apl-source:6

# apl-source:7
# رمز لوجندر: هل أ باقي تربيعي بترد أولي فردي
# apl-source:8
# معيار أويلر: أ^((ب-1)/2) تعطي 1 أو ب-1
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
def قوة_مود(أ, هـ, م):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  قاعدة = أ % م
  # apl-source:21
  باقي = هـ
  # apl-source:22
  while باقي > 0:
    # apl-source:23
    if (باقي % 2) == 1:
      # apl-source:24
      ناتج = (ناتج * قاعدة) % م
    # apl-source:25
    قاعدة = (قاعدة * قاعدة) % م
    # apl-source:26
    باقي = باقي // 2
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def لوجندر(أ, ب):
  # apl-source:30
  return قوة_مود(أ, (ب - 1) // 2, ب)
# apl-source:31

# apl-source:32
تأكد_يساوي(لوجندر(1, 7), 1, "الواحد باقي تربيعي")
# apl-source:33
تأكد_يساوي(لوجندر(2, 7), 1, "الاثنان باقي تربيعي")
# apl-source:34
تأكد_يساوي(لوجندر(3, 7), 6, "الثلاثة ليست باقياً تربيعياً")
# apl-source:35
تأكد_يساوي(لوجندر(4, 7), 1, "الأربعة مربع كامل")
# apl-source:36
تأكد_يساوي(لوجندر(5, 7), 6, "الخمسة ليست باقياً تربيعياً")
# apl-source:37
تأكد_يساوي(لوجندر(6, 7), 6, "الستة ليست باقياً تربيعياً")
# apl-source:38
