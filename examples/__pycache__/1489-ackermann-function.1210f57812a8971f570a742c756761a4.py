
# apl-source:1
# مثال 1489 — دالة أكرمان
# apl-source:2
# Ackermann function
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1489-ackermann-function.apl
# apl-source:6

# apl-source:7
# الحالة الأولى عند m تساوي صفراً
# apl-source:8
# ولكل حالة أخرى استدعاءان متداخلان
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
def أكرمان(م, ن):
  # apl-source:19
  if م == 0:
    # apl-source:20
    return ن + 1
  # apl-source:21
  if ن == 0:
    # apl-source:22
    return أكرمان(م - 1, 1)
  # apl-source:23
  return أكرمان(م - 1, أكرمان(م, ن - 1))
# apl-source:24

# apl-source:25
تأكد_يساوي(أكرمان(0, 5), 6, "صفر")
# apl-source:26
تأكد_يساوي(أكرمان(1, 2), 4, "واحد")
# apl-source:27
تأكد_يساوي(أكرمان(2, 3), 9, "اثنان")
# apl-source:28
