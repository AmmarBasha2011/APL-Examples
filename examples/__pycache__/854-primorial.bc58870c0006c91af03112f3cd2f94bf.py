
# apl-source:1
# مثال 854 — البريموريال
# apl-source:2
# Primorial
# apl-source:3
# Demonstrates: جداء الأولية حتى حد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/854-primorial.apl
# apl-source:6

# apl-source:7
# البريموريال: جداء الأعداد الأولية حتى حد معين
# apl-source:8
# نظير المضروب لكن على الأولية فقط: 29# = 6469693230
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
def أولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  if ن < 4:
    # apl-source:22
    return 1 == 1
  # apl-source:23
  if ن % 2 == 0:
    # apl-source:24
    return False
  # apl-source:25
  قاسم = 3
  # apl-source:26
  while قاسم * قاسم <= ن:
    # apl-source:27
    if ن % قاسم == 0:
      # apl-source:28
      return False
    # apl-source:29
    قاسم = قاسم + 2
  # apl-source:30
  return 1 == 1
# apl-source:31

# apl-source:32
def بريموريال(حد):
  # apl-source:33
  جداء = 1
  # apl-source:34
  for ن in range(2, حد + 1):
    # apl-source:35
    if أولي(ن):
      # apl-source:36
      جداء = جداء * ن
  # apl-source:37
  return جداء
# apl-source:38

# apl-source:39
print("7# =", بريموريال(7))
# apl-source:40
print("13# =", بريموريال(13))
# apl-source:41
print("29# =", بريموريال(29))
# apl-source:42

# apl-source:43
تأكد_يساوي(بريموريال(7), 210, "7# = 2*3*5*7")
# apl-source:44
تأكد_يساوي(بريموريال(13), 30030, "13# = 30030")
# apl-source:45
تأكد_يساوي(بريموريال(29), 6469693230, "29# = 6469693230")
# apl-source:46

# apl-source:47
# خاصية: ن# أكبر من أي أولي مربعي صغير مفيد في برهان إقليدس
# apl-source:48
تأكد_يساوي(بريموريال(5) + 1, 31, "5# + 1 = 31 أولي (حجة إقليدس)")
# apl-source:49
