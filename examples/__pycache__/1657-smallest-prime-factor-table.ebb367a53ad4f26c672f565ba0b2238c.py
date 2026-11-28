
# apl-source:1
# مثال 1657 — جدول أصغر عامل أولي
# apl-source:2
# Smallest prime factor sieve
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1657-smallest-prime-factor-table.apl
# apl-source:6

# apl-source:7
# نبدأ بكل عدد عاملاً لنفسه
# apl-source:8
# نحدث مضاعفات كل أولي لم يحدث بعد
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
def جدول_العوامل(ن):
  # apl-source:19
  أصغر_عامل = []
  # apl-source:20
  for ع in range(ن + 1):
    # apl-source:21
    أصغر_عامل.append(ع)
  # apl-source:22
  ك = 2
  # apl-source:23
  while ك * ك <= ن:
    # apl-source:24
    if أصغر_عامل[ك] == ك:
      # apl-source:25
      for م in range(ك * ك, ن + 1, ك):
        # apl-source:26
        if أصغر_عامل[م] == م:
          # apl-source:27
          أصغر_عامل[م] = ك
    # apl-source:28
    ك = ك + 1
  # apl-source:29
  return أصغر_عامل
# apl-source:30

# apl-source:31
def حلل(ن, جدول):
  # apl-source:32
  عوامل = []
  # apl-source:33
  while ن > 1:
    # apl-source:34
    عوامل.append(جدول[ن])
    # apl-source:35
    ن = ن // جدول[ن]
  # apl-source:36
  return عوامل
# apl-source:37

# apl-source:38
ج = جدول_العوامل(100)
# apl-source:39
تأكد_يساوي(حلل(84, ج), [2, 2, 3, 7], "أربعة وثمانون")
# apl-source:40
تأكد_يساوي(حلل(97, ج), [97], "أولي")
# apl-source:41
تأكد_يساوي(حلل(1, ج), [], "واحد")
# apl-source:42
