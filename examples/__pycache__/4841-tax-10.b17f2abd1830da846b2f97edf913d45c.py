
# apl-source:1
# مثال 4841 — إجمالي مع ضريبة 10%
# apl-source:2
# Total with 10 percent tax
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4841-tax-10.apl
# apl-source:6

# apl-source:7
# الإجمالي = السعر + الضريبة
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(س):
  # apl-source:18
  return س + س * 10 // 100
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(100), 110, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(200), 220, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(1500), 1650, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(80), 88, "حالة 4")
# apl-source:24
