
# apl-source:1
# مثال 1406 — الثبات الضربي
# apl-source:2
# Multiplicative persistence
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1406-multiplicative-persistence.apl
# apl-source:6

# apl-source:7
# نضرب أرقام العدد ونكرر
# apl-source:8
# نعد الخطوات حتى رقم واحد
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
def ثبات(ن):
  # apl-source:19
  خطوات = 0
  # apl-source:20
  while ن >= 10:
    # apl-source:21
    ض = 1
    # apl-source:22
    for ح in str(ن):
      # apl-source:23
      ض = ض * int(ح)
    # apl-source:24
    ن = ض
    # apl-source:25
    خطوات = خطوات + 1
  # apl-source:26
  return خطوات
# apl-source:27

# apl-source:28
تأكد_يساوي(ثبات(4), 0, "رقم واحد")
# apl-source:29
تأكد_يساوي(ثبات(39), 3, "تسعة وثلاثون")
# apl-source:30
تأكد_يساوي(ثبات(999), 4, "تسعمئة وتسعة وتسعون")
# apl-source:31
تأكد_يساوي(ثبات(77), 4, "سبعة وسبعون")
# apl-source:32
