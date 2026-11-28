
# apl-source:1
# مثال 1786 — خطوات كابريكار
# apl-source:2
# Kaprekar routine steps
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1786-kaprekar-routine-steps.apl
# apl-source:6

# apl-source:7
# نرتب أرقام العدد
# apl-source:8
# نكرر حتى نصل 6174
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
def خطوة(ن):
  # apl-source:19
  أرقام = []
  # apl-source:20
  for ك in range(4):
    # apl-source:21
    أرقام.append(ن % 10)
    # apl-source:22
    ن = ن // 10
  # apl-source:23
  أرقام.sort()
  # apl-source:24
  صغير = 0
  # apl-source:25
  for ر in أرقام:
    # apl-source:26
    صغير = صغير * 10 + ر
  # apl-source:27
  أرقام.reverse()
  # apl-source:28
  كبير = 0
  # apl-source:29
  for ر in أرقام:
    # apl-source:30
    كبير = كبير * 10 + ر
  # apl-source:31
  return كبير - صغير
# apl-source:32

# apl-source:33
def عدد_الخطوات(ن):
  # apl-source:34
  عد = 0
  # apl-source:35
  while ن != 6174:
    # apl-source:36
    ن = خطوة(ن)
    # apl-source:37
    عد = عد + 1
  # apl-source:38
  return عد
# apl-source:39

# apl-source:40
تأكد_يساوي(عدد_الخطوات(3524), 3, "ثلاث")
# apl-source:41
تأكد_يساوي(عدد_الخطوات(6174), 0, "الثابت")
# apl-source:42
تأكد_يساوي(عدد_الخطوات(2111), 5, "خمس")
# apl-source:43
