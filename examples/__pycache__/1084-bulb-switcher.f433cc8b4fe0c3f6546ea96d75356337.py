
# apl-source:1
# مثال 1084 — مفاتيح المصابيح
# apl-source:2
# Bulb switcher
# apl-source:3
# Demonstrates: المربعات الكاملة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1084-bulb-switcher.apl
# apl-source:6

# apl-source:7
# المصباح يتبدل بعدد قواسمه والمضاء من له قواسم فردية
# apl-source:8
# وهذه خاصية المربعات الكاملة فقط
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
def مضاءة(ن):
  # apl-source:19
  ج = 0
  # apl-source:20
  while ((ج + 1) * (ج + 1)) <= ن:
    # apl-source:21
    ج = ج + 1
  # apl-source:22
  return ج
# apl-source:23

# apl-source:24
def مضاءة_بالمحاكاة(ن):
  # apl-source:25
  حالة = [False] * (ن + 1)
  # apl-source:26
  for جولة in range(1, ن + 1):
    # apl-source:27
    for م in range(جولة, ن + 1, جولة):
      # apl-source:28
      حالة[م] = not حالة[م]
  # apl-source:29
  عدد_ = 0
  # apl-source:30
  for م in range(1, ن + 1):
    # apl-source:31
    if حالة[م]:
      # apl-source:32
      عدد_ = عدد_ + 1
  # apl-source:33
  return عدد_
# apl-source:34

# apl-source:35
تأكد_يساوي(مضاءة(3), 1, "ثلاثة")
# apl-source:36
تأكد_يساوي(مضاءة(0), 0, "صفر")
# apl-source:37
تأكد_يساوي(مضاءة(99), 9, "تسعة وتسعون")
# apl-source:38
تأكد_يساوي(مضاءة_بالمحاكاة(30), مضاءة(30), "المحاكاة تطابق")
# apl-source:39
