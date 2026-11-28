
# apl-source:1
# مثال 1170 — أقصر متناظرة
# apl-source:2
# Shortest palindrome by prepending
# apl-source:3
# Demonstrates: بادئة متناظرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1170-shortest-palindrome.apl
# apl-source:6

# apl-source:7
# نبحث عن أطول بادئة متناظرة
# apl-source:8
# ونعكس الباقي ونضعه في المقدمة
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
def اقصر_متناظرة(س):
  # apl-source:19
  for ع in range(len(س), 0, -1):
    # apl-source:20
    ب = س[:ع]
    # apl-source:21
    if ب == ب[::-1]:
      # apl-source:22
      return س[ع:][::-1] + س
  # apl-source:23
  return س
# apl-source:24

# apl-source:25
تأكد_يساوي(اقصر_متناظرة("aacecaaa"), "aaacecaaa", "مثال أول")
# apl-source:26
تأكد_يساوي(اقصر_متناظرة("abcd"), "dcbabcd", "مثال ثان")
# apl-source:27
تأكد_يساوي(اقصر_متناظرة(""), "", "فارغة")
# apl-source:28
تأكد_يساوي(اقصر_متناظرة("aba"), "aba", "متناظرة اصلاً")
# apl-source:29
