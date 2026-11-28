
# apl-source:1
# مثال 1043 — قوة العدد ثلاثة
# apl-source:2
# Power of three check
# apl-source:3
# Demonstrates: قسمة متكررة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1043-power-of-three.apl
# apl-source:6

# apl-source:7
# نقسم على ثلاثة ما دام العدد يقبل القسمة
# apl-source:8
# فلو وصلنا إلى واحد فهو قوة للثلاثة
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
def قوة_ثلاثة(ن):
  # apl-source:19
  if ن < 1:
    # apl-source:20
    return False
  # apl-source:21
  while ن % 3 == 0:
    # apl-source:22
    ن = ن // 3
  # apl-source:23
  return ن == 1
# apl-source:24

# apl-source:25
تأكد_يساوي(قوة_ثلاثة(27), True, "سبعة وعشرون")
# apl-source:26
تأكد_يساوي(قوة_ثلاثة(0), False, "صفر")
# apl-source:27
تأكد_يساوي(قوة_ثلاثة(9), True, "تسعة")
# apl-source:28
تأكد_يساوي(قوة_ثلاثة(45), False, "خمسة وأربعون")
# apl-source:29
تأكد_يساوي(قوة_ثلاثة(1), True, "واحد")
# apl-source:30
