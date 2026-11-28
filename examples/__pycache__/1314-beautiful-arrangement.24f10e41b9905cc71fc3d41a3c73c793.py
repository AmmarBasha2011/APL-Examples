
# apl-source:1
# مثال 1314 — ترتيب جميل
# apl-source:2
# Beautiful arrangement count
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1314-beautiful-arrangement.apl
# apl-source:6

# apl-source:7
# نضع كل عدد في موضع يحقق الشرط
# apl-source:8
# ونعد الترتيبات الكاملة
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
def عد_من(موضع, ن, مستعمل):
  # apl-source:19
  if موضع > ن:
    # apl-source:20
    return 1
  # apl-source:21
  ع = 0
  # apl-source:22
  for س in range(1, ن + 1):
    # apl-source:23
    if not مستعمل[س]:
      # apl-source:24
      if (س % موضع == 0) or (موضع % س == 0):
        # apl-source:25
        مستعمل[س] = True
        # apl-source:26
        ع = ع + عد_من(موضع + 1, ن, مستعمل)
        # apl-source:27
        مستعمل[س] = False
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
def عد_ترتيبات(ن):
  # apl-source:31
  return عد_من(1, ن, [False] * (ن + 1))
# apl-source:32

# apl-source:33
تأكد_يساوي(عد_ترتيبات(1), 1, "واحد")
# apl-source:34
تأكد_يساوي(عد_ترتيبات(2), 2, "اثنان")
# apl-source:35
تأكد_يساوي(عد_ترتيبات(3), 3, "ثلاثة")
# apl-source:36
تأكد_يساوي(عد_ترتيبات(4), 8, "أربعة")
# apl-source:37
تأكد_يساوي(عد_ترتيبات(6), 36, "ستة")
# apl-source:38
