
# apl-source:1
# مثال 1394 — أولية دائرية
# apl-source:2
# Circular primes
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1394-circular-primes.apl
# apl-source:6

# apl-source:7
# ندير الأرقام بنقل أول رقم لآخره
# apl-source:8
# كل دوران يجب أن يكون أولياً
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  ع = 2
  # apl-source:22
  while ع * ع <= ن:
    # apl-source:23
    if ن % ع == 0:
      # apl-source:24
      return False
    # apl-source:25
    ع = ع + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def دائري(ن):
  # apl-source:29
  ن_نص = str(ن)
  # apl-source:30
  for ع in range(len(ن_نص)):
    # apl-source:31
    دوران = ن_نص[ع:] + ن_نص[:ع]
    # apl-source:32
    if not اولي(int(دوران)):
      # apl-source:33
      return False
  # apl-source:34
  return True
# apl-source:35

# apl-source:36
def عد_دائرية(حد):
  # apl-source:37
  عدد = 0
  # apl-source:38
  for ن in range(2, حد):
    # apl-source:39
    if دائري(ن):
      # apl-source:40
      عدد = عدد + 1
  # apl-source:41
  return عدد
# apl-source:42

# apl-source:43
تأكد_يساوي(دائري(197), True, "مئة وسبعة وتسعون")
# apl-source:44
تأكد_يساوي(دائري(19), False, "تسعة عشر")
# apl-source:45
تأكد_يساوي(عد_دائرية(100), 13, "أقل من مئة")
# apl-source:46
