
# apl-source:1
# مثال 1167 — مطابقة تعبير
# apl-source:2
# Regular expression matching dot star
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1167-regex-matching-dp.apl
# apl-source:6

# apl-source:7
# النقطة تطابق أي حرف
# apl-source:8
# والنجمة تكرر العنصر السابق صفراً أو أكثر
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
def تطابق_تعبير(س, ن):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(len(س) + 1):
    # apl-source:21
    د = د + [[False] * (len(ن) + 1)]
  # apl-source:22
  د[0][0] = True
  # apl-source:23
  for ج in range(2, len(ن) + 1):
    # apl-source:24
    if ن[ج - 1] == "*":
      # apl-source:25
      د[0][ج] = د[0][ج - 2]
  # apl-source:26
  for ع in range(1, len(س) + 1):
    # apl-source:27
    for ج in range(1, len(ن) + 1):
      # apl-source:28
      if ن[ج - 1] == "*":
        # apl-source:29
        صفر = د[ع][ج - 2]
        # apl-source:30
        ازيد = False
        # apl-source:31
        if (ن[ج - 2] == ".") or (ن[ج - 2] == س[ع - 1]):
          # apl-source:32
          ازيد = د[ع - 1][ج]
        # apl-source:33
        د[ع][ج] = صفر or ازيد
      # apl-source:34
      elif (ن[ج - 1] == ".") or (ن[ج - 1] == س[ع - 1]):
        # apl-source:35
        د[ع][ج] = د[ع - 1][ج - 1]
  # apl-source:36
  return د[len(س)][len(ن)]
# apl-source:37

# apl-source:38
تأكد_يساوي(تطابق_تعبير("aa", "a"), False, "قصير")
# apl-source:39
تأكد_يساوي(تطابق_تعبير("aa", "a*"), True, "نجمة")
# apl-source:40
تأكد_يساوي(تطابق_تعبير("ab", ".*"), True, "نقطة نجمة")
# apl-source:41
تأكد_يساوي(تطابق_تعبير("aab", "c*a*b"), True, "نجمة صفرية")
# apl-source:42
تأكد_يساوي(تطابق_تعبير("mississippi", "mis*is*p*."), False, "طويل")
# apl-source:43
