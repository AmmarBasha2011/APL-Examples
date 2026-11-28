
# apl-source:1
# مثال 1288 — أقصر متتالية شاملة
# apl-source:2
# Shortest common supersequence length
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1288-shortest-supersequence.apl
# apl-source:6

# apl-source:7
# الطول هو مجموع الطولين ناقص أطول متتالية مشتركة
# apl-source:8
# نحسبها بجدول
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
def اطول_مشتركة(أ, ب):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(len(أ) + 1):
    # apl-source:21
    د = د + [[0] * (len(ب) + 1)]
  # apl-source:22
  for ع in range(1, len(أ) + 1):
    # apl-source:23
    for ج in range(1, len(ب) + 1):
      # apl-source:24
      if أ[ع - 1] == ب[ج - 1]:
        # apl-source:25
        د[ع][ج] = د[ع - 1][ج - 1] + 1
      # apl-source:26
      else:
        # apl-source:27
        د[ع][ج] = max(د[ع - 1][ج], د[ع][ج - 1])
  # apl-source:28
  return د[len(أ)][len(ب)]
# apl-source:29

# apl-source:30
def اقصر_شاملة(أ, ب):
  # apl-source:31
  return len(أ) + len(ب) - اطول_مشتركة(أ, ب)
# apl-source:32

# apl-source:33
تأكد_يساوي(اقصر_شاملة("abac", "cab"), 5, "مثال أول")
# apl-source:34
تأكد_يساوي(اقصر_شاملة("geek", "eke"), 5, "مثال ثان")
# apl-source:35
تأكد_يساوي(اقصر_شاملة("abc", "abc"), 3, "متطابقان")
# apl-source:36
تأكد_يساوي(اقصر_شاملة("", "xyz"), 3, "فارغ")
# apl-source:37
