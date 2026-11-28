
# apl-source:1
# مثال 1534 — هل العدد قوة للأربعة
# apl-source:2
# Is power of four
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1534-power-of-four-check.apl
# apl-source:6

# apl-source:7
# قوة الأربعة قوة للاثنين أولاً
# apl-source:8
# وبتها المضيء في موضع زوجي
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
def قوة_أربعة(ن):
  # apl-source:19
  if ن <= 0:
    # apl-source:20
    return False
  # apl-source:21
  if ن & (ن - 1) != 0:
    # apl-source:22
    return False
  # apl-source:23
  return ن & 1431655765 != 0
# apl-source:24

# apl-source:25
تأكد_يساوي(قوة_أربعة(16), True, "ستة عشر")
# apl-source:26
تأكد_يساوي(قوة_أربعة(8), False, "ثمانية")
# apl-source:27
تأكد_يساوي(قوة_أربعة(1), True, "واحد")
# apl-source:28
تأكد_يساوي(قوة_أربعة(0), False, "صفر")
# apl-source:29
