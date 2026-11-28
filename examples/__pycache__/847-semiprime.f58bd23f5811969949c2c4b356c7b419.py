
# apl-source:1
# مثال 847 — شبه الأولية
# apl-source:2
# Semiprimes
# apl-source:3
# Demonstrates: جداء أوليين بالضبط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/847-semiprime.apl
# apl-source:6

# apl-source:7
# شبه الأولية: جداء أوليين اثنين بالضبط (مع تكرارهما)
# apl-source:8
# أساس أمن RSA: مفككها صعب عند كبرها
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
def عدد_العوامل_الأولية(عدد):
  # apl-source:19
  ن = عدد
  # apl-source:20
  عد = 0
  # apl-source:21
  قاسم = 2
  # apl-source:22
  while قاسم * قاسم <= ن:
    # apl-source:23
    while ن % قاسم == 0:
      # apl-source:24
      عد = عد + 1
      # apl-source:25
      ن = ن // قاسم
    # apl-source:26
    قاسم = قاسم + 1
  # apl-source:27
  if ن > 1:
    # apl-source:28
    عد = عد + 1
  # apl-source:29
  return عد
# apl-source:30

# apl-source:31
شبه = []
# apl-source:32
for ن in range(2, 51):
  # apl-source:33
  if عدد_العوامل_الأولية(ن) == 2:
    # apl-source:34
    شبه = شبه + [ن]
# apl-source:35

# apl-source:36
print("شبه الأولية حتى 50:", شبه)
# apl-source:37

# apl-source:38
تأكد_يساوي(len(شبه), 17, "سبعة عشر حتى 50")
# apl-source:39
تأكد_يساوي(شبه[0], 4, "الأول 4 = 2*2")
# apl-source:40
تأكد_يساوي(شبه[16], 49, "الأخير 49 = 7*7")
# apl-source:41

# apl-source:42
# المربعات الأولية تدخل أيضاً لأن التكرار مسموح
# apl-source:43
تأكد_يساوي(عدد_العوامل_الأولية(25), 2, "25 = 5*5 شبه أولي")
# apl-source:44
تأكد_يساوي(عدد_العوامل_الأولية(27), 3, "27 = 3*3*3 ليس شبه أولي")
# apl-source:45
