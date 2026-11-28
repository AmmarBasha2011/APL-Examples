
# apl-source:1
# مثال 1400 — عدد مثلثي بقواسم كثيرة
# apl-source:2
# First triangle number with many divisors
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1400-triangle-number-divisors.apl
# apl-source:6

# apl-source:7
# العدد المثلثي ن(ن+1)/2
# apl-source:8
# نعد القواسم حتى الجذر
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
def عد_القواسم(ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  ع = 1
  # apl-source:21
  while ع * ع <= ن:
    # apl-source:22
    if ن % ع == 0:
      # apl-source:23
      عدد = عدد + 1
      # apl-source:24
      if ع * ع != ن:
        # apl-source:25
        عدد = عدد + 1
    # apl-source:26
    ع = ع + 1
  # apl-source:27
  return عدد
# apl-source:28

# apl-source:29
def اول_مثلثي(اكثر_من):
  # apl-source:30
  ن = 1
  # apl-source:31
  ع = 1
  # apl-source:32
  while عد_القواسم(ع) <= اكثر_من:
    # apl-source:33
    ن = ن + 1
    # apl-source:34
    ع = ع + ن
  # apl-source:35
  return ع
# apl-source:36

# apl-source:37
تأكد_يساوي(اول_مثلثي(1), 3, "أكثر من واحد")
# apl-source:38
تأكد_يساوي(اول_مثلثي(3), 6, "أكثر من ثلاثة")
# apl-source:39
تأكد_يساوي(اول_مثلثي(5), 28, "أكثر من خمسة")
# apl-source:40
