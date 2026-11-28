
# apl-source:1
# مثال 1511 — الفائدة البسيطة
# apl-source:2
# Simple interest total
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1511-simple-interest-total.apl
# apl-source:6

# apl-source:7
# الفائدة = الأصل × النسبة × السنوات
# apl-source:8
# النسبة بالمئة
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
def المبلغ_بفائدة_بسيطة(أصل, نسبة, سنوات):
  # apl-source:19
  return أصل + أصل * نسبة * سنوات / 100
# apl-source:20

# apl-source:21
تأكد_يساوي(المبلغ_بفائدة_بسيطة(1000, 5, 2), 1100.0, "سنتان")
# apl-source:22
تأكد_يساوي(المبلغ_بفائدة_بسيطة(200, 10, 1), 220.0, "سنة")
# apl-source:23
تأكد_يساوي(المبلغ_بفائدة_بسيطة(500, 0, 5), 500.0, "بلا فائدة")
# apl-source:24
