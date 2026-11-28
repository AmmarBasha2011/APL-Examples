
# apl-source:1
# مثال 1550 — قطر المكعب
# apl-source:2
# Cube space diagonal
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1550-cube-space-diagonal.apl
# apl-source:6

# apl-source:7
# القطر = الضلع × جذر ثلاثة
# apl-source:8
# نربع ونضرب بثلاثة ثم نجذر
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
def قطر_المكعب(ضلع):
  # apl-source:19
  return (3 * ضلع * ضلع) ** 0.5
# apl-source:20

# apl-source:21
تأكد_يساوي(قطر_المكعب(0), 0.0, "صفر")
# apl-source:22
تأكد_يساوي(قطر_المكعب(2) > 3.46, True, "ضلع اثنان")
# apl-source:23
تأكد_يساوي(قطر_المكعب(10) > 17.3, True, "أكبر من 17.3")
# apl-source:24
تأكد_يساوي(قطر_المكعب(10) < 17.4, True, "أصغر من 17.4")
# apl-source:25
