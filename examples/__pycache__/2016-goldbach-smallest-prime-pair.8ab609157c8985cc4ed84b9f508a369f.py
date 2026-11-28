
# apl-source:1
# مثال 2016 — زوج أولي لغولدباخ
# apl-source:2
# Goldbach prime pair
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2016-goldbach-smallest-prime-pair.apl
# apl-source:6

# apl-source:7
# # نختبر الأوليات بالقسمة
# apl-source:8
# # ونبحث بدءا من أصغر أولي
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
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def غولدباخ(ن):
  # apl-source:29
  for ا in range(2, ن // 2 + 1):
    # apl-source:30
    if اولي(ا) and اولي(ن - ا):
      # apl-source:31
      return [ا, ن - ا]
  # apl-source:32
  return []
# apl-source:33

# apl-source:34
تأكد_يساوي(غولدباخ(28), [5, 23], "٢٨")
# apl-source:35
تأكد_يساوي(غولدباخ(4), [2, 2], "٤")
# apl-source:36
تأكد_يساوي(غولدباخ(100), [3, 97], "١٠٠")
# apl-source:37
تأكد_يساوي(غولدباخ(10), [3, 7], "١٠")
# apl-source:38
