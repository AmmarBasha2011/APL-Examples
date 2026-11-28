
# apl-source:1
# مثال 1151 — دورة مربعات الأرقام
# apl-source:2
# Digit squares cycle length
# apl-source:3
# Demonstrates: كشف دورة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1151-squares-of-digits-cycle.apl
# apl-source:6

# apl-source:7
# نكرر جمع مربعات الأرقام
# apl-source:8
# ونسجل الأعداد المرئية حتى يتكرر أحدها
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
def تالي(ن):
  # apl-source:19
  مج = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ر = ن % 10
    # apl-source:22
    مج = مج + ر * ر
    # apl-source:23
    ن = ن // 10
  # apl-source:24
  return مج
# apl-source:25

# apl-source:26
def طول_الدورة(ن):
  # apl-source:27
  مرئي = []
  # apl-source:28
  while ن not in مرئي:
    # apl-source:29
    مرئي = مرئي + [ن]
    # apl-source:30
    ن = تالي(ن)
  # apl-source:31
  return len(مرئي) - مرئي.index(ن)
# apl-source:32

# apl-source:33
تأكد_يساوي(طول_الدورة(1), 1, "واحد ثابت")
# apl-source:34
تأكد_يساوي(طول_الدورة(19), 1, "سعيد")
# apl-source:35
تأكد_يساوي(طول_الدورة(4), 8, "دورة الثمانية")
# apl-source:36
تأكد_يساوي(طول_الدورة(2), 8, "يدخل الدورة")
# apl-source:37
