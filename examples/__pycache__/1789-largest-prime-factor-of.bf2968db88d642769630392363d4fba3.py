
# apl-source:1
# مثال 1789 — أكبر عامل أولي
# apl-source:2
# Largest prime factor
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1789-largest-prime-factor-of.apl
# apl-source:6

# apl-source:7
# كل عامل ينزع كاملاً
# apl-source:8
# الباقي أكبر من الواحد أولي
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
def أكبر_عامل(ن):
  # apl-source:19
  أكبر_حالي = 1
  # apl-source:20
  ك = 2
  # apl-source:21
  while ك * ك <= ن:
    # apl-source:22
    while ن % ك == 0:
      # apl-source:23
      أكبر_حالي = ك
      # apl-source:24
      ن = ن // ك
    # apl-source:25
    ك = ك + 1
  # apl-source:26
  if ن > 1:
    # apl-source:27
    أكبر_حالي = ن
  # apl-source:28
  return أكبر_حالي
# apl-source:29

# apl-source:30
تأكد_يساوي(أكبر_عامل(13195), 29, "كلاسيكي")
# apl-source:31
تأكد_يساوي(أكبر_عامل(97), 97, "أولي")
# apl-source:32
تأكد_يساوي(أكبر_عامل(64), 2, "قوة اثنين")
# apl-source:33
