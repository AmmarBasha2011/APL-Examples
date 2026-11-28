
# apl-source:1
# مثال 1917 — لعبة نيم الموقف الرابح
# apl-source:2
# Nim game winning position
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1917-nim-game-winning-position.apl
# apl-source:6

# apl-source:7
# نحسب xor لأحجام الأكوام
# apl-source:8
# صفر يعني أن الدور الحالي خاسر
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
def رابح(اكوام):
  # apl-source:19
  س = 0
  # apl-source:20
  for ك in اكوام:
    # apl-source:21
    س = س ^ ك
  # apl-source:22
  return س != 0
# apl-source:23

# apl-source:24
تأكد_يساوي(رابح([3, 4, 5]), True, "٣ ٤ ٥")
# apl-source:25
تأكد_يساوي(رابح([1, 2, 3]), False, "١ ٢ ٣")
# apl-source:26
تأكد_يساوي(رابح([7]), True, "كومة واحدة")
# apl-source:27
تأكد_يساوي(رابح([2, 2]), False, "متساويان")
# apl-source:28
