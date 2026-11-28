
# apl-source:1
# مثال 1663 — هل العدد خالٍ من المربعات
# apl-source:2
# Square free number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1663-square-free-check.apl
# apl-source:6

# apl-source:7
# نجرب القسمة على ك تربيعاً
# apl-source:8
# إن انقسم فليس خالياً
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
def خالٍ_من_المربعات(ن):
  # apl-source:19
  ك = 2
  # apl-source:20
  while ك * ك <= ن:
    # apl-source:21
    if ن % (ك * ك) == 0:
      # apl-source:22
      return False
    # apl-source:23
    ك = ك + 1
  # apl-source:24
  return True
# apl-source:25

# apl-source:26
تأكد_يساوي(خالٍ_من_المربعات(10), True, "عشرة")
# apl-source:27
تأكد_يساوي(خالٍ_من_المربعات(12), False, "اثنا عشر")
# apl-source:28
تأكد_يساوي(خالٍ_من_المربعات(30), True, "ثلاثون")
# apl-source:29
تأكد_يساوي(خالٍ_من_المربعات(50), False, "خمسون")
# apl-source:30
