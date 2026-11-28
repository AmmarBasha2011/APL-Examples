
# apl-source:1
# مثال 4722 — أكبر الأعداد المثلثي حتى حد معين
# apl-source:2
# Numbers up to a limit: largest of the triangular ones
# apl-source:3
# Demonstrates: حلقات وشروط وأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4722-numbers-largest-triangular.apl
# apl-source:6

# apl-source:7
# نفحص الأعداد من 1 إلى الحد
# apl-source:8
# ونجمع منها اللي يحقق الشرط
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
def ف(ح):
  # apl-source:19
  ن = []
  # apl-source:20
  for ر in range(1, ح + 1):
    # apl-source:21
    if len([م for م in range(0, ر + 1) if م * (م + 1) // 2 == ر]) == 1:
      # apl-source:22
      ن = ن + [ر]
  # apl-source:23
  if len(ن) == 0:
    # apl-source:24
    return 0
  # apl-source:25
  return max(ن)
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(25), 21, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(67), 66, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(116), 105, "حالة 3")
# apl-source:30
تأكد_يساوي(ف(1), 1, "حالة 4")
# apl-source:31
تأكد_يساوي(ف(0), 0, "حالة 5")
# apl-source:32
