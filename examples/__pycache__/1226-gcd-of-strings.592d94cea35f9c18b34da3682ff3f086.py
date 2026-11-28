
# apl-source:1
# مثال 1226 — قاسم نصين
# apl-source:2
# Greatest common divisor of strings
# apl-source:3
# Demonstrates: قاسم مشترك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1226-gcd-of-strings.apl
# apl-source:6

# apl-source:7
# لو لم يتطابق الدمجان بالترتيبين فلا قاسم
# apl-source:8
# وإلا القاسم طوله هو gcd الطولين
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
def قاسم(أ, ب):
  # apl-source:19
  if (أ + ب) != (ب + أ):
    # apl-source:20
    return ""
  # apl-source:21
  س = len(أ)
  # apl-source:22
  ص = len(ب)
  # apl-source:23
  while ص > 0:
    # apl-source:24
    ت = س % ص
    # apl-source:25
    س = ص
    # apl-source:26
    ص = ت
  # apl-source:27
  return أ[:س]
# apl-source:28

# apl-source:29
تأكد_يساوي(قاسم("ABCABC", "ABC"), "ABC", "مثال أول")
# apl-source:30
تأكد_يساوي(قاسم("ABABAB", "ABAB"), "AB", "مثال ثان")
# apl-source:31
تأكد_يساوي(قاسم("LEET", "CODE"), "", "لا قاسم")
# apl-source:32
تأكد_يساوي(قاسم("AAAA", "AA"), "AA", "تكرار")
# apl-source:33
