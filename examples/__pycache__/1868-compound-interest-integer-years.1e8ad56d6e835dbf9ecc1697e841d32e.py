
# apl-source:1
# مثال 1868 — الفائدة المركبة بأعداد صحيحة
# apl-source:2
# Compound interest with integer percent
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1868-compound-interest-integer-years.apl
# apl-source:6

# apl-source:7
# القسمة الصحيحة تبقي الأعداد دقيقة
# apl-source:8
# نكرر عدد السنوات
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
def رصيد_بعد(رأس, نسبة, سنوات):
  # apl-source:19
  for ك in range(سنوات):
    # apl-source:20
    رأس = رأس + رأس * نسبة // 100
  # apl-source:21
  return رأس
# apl-source:22

# apl-source:23
تأكد_يساوي(رصيد_بعد(1000, 10, 1), 1100, "سنة")
# apl-source:24
تأكد_يساوي(رصيد_بعد(1000, 10, 2), 1210, "سنتان")
# apl-source:25
تأكد_يساوي(رصيد_بعد(500, 0, 5), 500, "بلا فائدة")
# apl-source:26
