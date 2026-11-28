
# apl-source:1
# مثال 1089 — نمط جزئي مكرر
# apl-source:2
# Repeated substring pattern
# apl-source:3
# Demonstrates: تجربة الأطوال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1089-repeated-substring.apl
# apl-source:6

# apl-source:7
# نجرب كل طول يقسم طول النص
# apl-source:8
# ونتحقق أن تكرار البادئة بهذا الطول يعيد النص
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
def مكرر(نص_):
  # apl-source:19
  ن = len(نص_)
  # apl-source:20
  for ط in range(1, (ن // 2) + 1):
    # apl-source:21
    if (ن % ط == 0) and ((نص_[:ط] * (ن // ط)) == نص_):
      # apl-source:22
      return True
  # apl-source:23
  return False
# apl-source:24

# apl-source:25
تأكد_يساوي(مكرر("abab"), True, "abab")
# apl-source:26
تأكد_يساوي(مكرر("aba"), False, "aba")
# apl-source:27
تأكد_يساوي(مكرر("abcabcabcabc"), True, "أربع مرات")
# apl-source:28
تأكد_يساوي(مكرر("a"), False, "حرف")
# apl-source:29
