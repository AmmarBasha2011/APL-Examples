
# apl-source:1
# مثال 1166 — مطابقة بنجوم
# apl-source:2
# Wildcard pattern matching
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1166-wildcard-matching.apl
# apl-source:6

# apl-source:7
# علامة الاستفهام تطابق حرفاً واحداً
# apl-source:8
# والنجمة تطابق أي تسلسل حتى الفارغ
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
def تطابق(س, ن):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(len(س) + 1):
    # apl-source:21
    د = د + [[False] * (len(ن) + 1)]
  # apl-source:22
  د[0][0] = True
  # apl-source:23
  for ج in range(1, len(ن) + 1):
    # apl-source:24
    if ن[ج - 1] == "*":
      # apl-source:25
      د[0][ج] = د[0][ج - 1]
  # apl-source:26
  for ع in range(1, len(س) + 1):
    # apl-source:27
    for ج in range(1, len(ن) + 1):
      # apl-source:28
      if ن[ج - 1] == "*":
        # apl-source:29
        ا = د[ع - 1][ج]
        # apl-source:30
        ب = د[ع][ج - 1]
        # apl-source:31
        د[ع][ج] = ا or ب
      # apl-source:32
      elif (ن[ج - 1] == "?") or (ن[ج - 1] == س[ع - 1]):
        # apl-source:33
        د[ع][ج] = د[ع - 1][ج - 1]
  # apl-source:34
  return د[len(س)][len(ن)]
# apl-source:35

# apl-source:36
تأكد_يساوي(تطابق("aa", "a"), False, "قصير")
# apl-source:37
تأكد_يساوي(تطابق("aa", "*"), True, "نجمة")
# apl-source:38
تأكد_يساوي(تطابق("cb", "?a"), False, "استفهام")
# apl-source:39
تأكد_يساوي(تطابق("adceb", "*a*b"), True, "نجمتان")
# apl-source:40
تأكد_يساوي(تطابق("", "***"), True, "فارغ")
# apl-source:41
