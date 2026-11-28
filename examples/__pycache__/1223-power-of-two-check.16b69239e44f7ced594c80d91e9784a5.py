
# apl-source:1
# مثال 1223 — قوة العدد اثنين
# apl-source:2
# Power of two and four check
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1223-power-of-two-check.apl
# apl-source:6

# apl-source:7
# القوة اثنين فيها بت واحد
# apl-source:8
# والقوة أربعة بتها في موضع زوجي
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
def قوة_اثنين(ن):
  # apl-source:19
  return (ن > 0) and ((ن & (ن - 1)) == 0)
# apl-source:20

# apl-source:21
def قوة_اربعة(ن):
  # apl-source:22
  if not قوة_اثنين(ن):
    # apl-source:23
    return False
  # apl-source:24
  return (ن & 0x55555555) != 0
# apl-source:25

# apl-source:26
تأكد_يساوي(قوة_اثنين(1), True, "واحد")
# apl-source:27
تأكد_يساوي(قوة_اثنين(16), True, "ستة عشر")
# apl-source:28
تأكد_يساوي(قوة_اثنين(18), False, "ثمانية عشر")
# apl-source:29
تأكد_يساوي(قوة_اثنين(0), False, "صفر")
# apl-source:30
تأكد_يساوي(قوة_اربعة(16), True, "أربعة")
# apl-source:31
تأكد_يساوي(قوة_اربعة(8), False, "ثمانية")
# apl-source:32
تأكد_يساوي(قوة_اربعة(64), True, "أربع وستون")
# apl-source:33
