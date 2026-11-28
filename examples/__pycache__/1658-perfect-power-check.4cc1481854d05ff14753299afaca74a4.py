
# apl-source:1
# مثال 1658 — هل العدد قوة كاملة
# apl-source:2
# Perfect power check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1658-perfect-power-check.apl
# apl-source:6

# apl-source:7
# نجرب الأسس من 2
# apl-source:8
# ونجرب الأساسات حتى يتجاوز العدد
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
def قوة_كاملة(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return True
  # apl-source:21
  for أ in range(2, ن):
    # apl-source:22
    if أ * أ > ن:
      # apl-source:23
      return False
    # apl-source:24
    ق = أ * أ
    # apl-source:25
    while ق < ن:
      # apl-source:26
      ق = ق * أ
    # apl-source:27
    if ق == ن:
      # apl-source:28
      return True
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(قوة_كاملة(16), True, "ستة عشر")
# apl-source:32
تأكد_يساوي(قوة_كاملة(27), True, "سبعة وعشرون")
# apl-source:33
تأكد_يساوي(قوة_كاملة(18), False, "ثمانية عشر")
# apl-source:34
تأكد_يساوي(قوة_كاملة(1), True, "واحد")
# apl-source:35
