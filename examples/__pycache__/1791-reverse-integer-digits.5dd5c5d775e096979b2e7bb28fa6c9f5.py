
# apl-source:1
# مثال 1791 — عكس أرقام العدد
# apl-source:2
# Reverse integer digits
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1791-reverse-integer-digits.apl
# apl-source:6

# apl-source:7
# نأخذ الرقم الأخير
# apl-source:8
# نضيفه إلى الناتج
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
def اعكس_العدد(ن):
  # apl-source:19
  إشارة = 1
  # apl-source:20
  if ن < 0:
    # apl-source:21
    إشارة = -1
    # apl-source:22
    ن = -ن
  # apl-source:23
  ناتج = 0
  # apl-source:24
  while ن > 0:
    # apl-source:25
    ناتج = ناتج * 10 + ن % 10
    # apl-source:26
    ن = ن // 10
  # apl-source:27
  return إشارة * ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(اعكس_العدد(123), 321, "ثلاثة")
# apl-source:30
تأكد_يساوي(اعكس_العدد(-45), -54, "سالب")
# apl-source:31
تأكد_يساوي(اعكس_العدد(1200), 21, "أصفار")
# apl-source:32
