
# apl-source:1
# مثال 4748 — خطوات متتالية كولاتز (3ن+1) بحد أقصى
# apl-source:2
# Collatz-style steps with 3n+1 (capped at 60)
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4748-collatz-3n-plus-1.apl
# apl-source:6

# apl-source:7
# لو العدد زوجي نقسمه على 2
# apl-source:8
# وغير كده نضربه ونضيف ثابت، وبحد أقصى 60 خطوة
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
def ف(ن):
  # apl-source:19
  ع = 0
  # apl-source:20
  while ن != 1 and ع < 60:
    # apl-source:21
    if ن % 2 == 0:
      # apl-source:22
      ن = ن // 2
    # apl-source:23
    else:
      # apl-source:24
      ن = ن * 3 + 1
    # apl-source:25
    ع = ع + 1
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(6), 8, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(7), 16, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(27), 60, "حالة 4")
# apl-source:32
تأكد_يساوي(ف(11), 14, "حالة 5")
# apl-source:33
