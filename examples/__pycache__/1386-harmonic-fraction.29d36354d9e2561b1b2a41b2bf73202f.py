
# apl-source:1
# مثال 1386 — العدد التوافقي ككسر
# apl-source:2
# Harmonic number as exact fraction
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1386-harmonic-fraction.apl
# apl-source:6

# apl-source:7
# نضيف كل مقلوب بكسور صحيحة
# apl-source:8
# ونختزل بالقاسم المشترك الأكبر
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
  while ب != 0:
    # apl-source:20
    ت = أ % ب
    # apl-source:21
    أ = ب
    # apl-source:22
    ب = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def توافقي(ن):
  # apl-source:26
  بسط = 0
  # apl-source:27
  مقام = 1
  # apl-source:28
  for ك in range(1, ن + 1):
    # apl-source:29
    بسط = بسط * ك + مقام
    # apl-source:30
    مقام = مقام * ك
    # apl-source:31
    ق = قاسم(بسط, مقام)
    # apl-source:32
    بسط = بسط // ق
    # apl-source:33
    مقام = مقام // ق
  # apl-source:34
  return [بسط, مقام]
# apl-source:35

# apl-source:36
تأكد_يساوي(توافقي(1), [1, 1], "واحد")
# apl-source:37
تأكد_يساوي(توافقي(4), [25, 12], "أربعة")
# apl-source:38
تأكد_يساوي(توافقي(5), [137, 60], "خمسة")
# apl-source:39
