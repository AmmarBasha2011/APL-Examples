
# apl-source:1
# مثال 4828 — سعر بعد خصم 25%
# apl-source:2
# Price after 25 percent discount
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4828-discount-25.apl
# apl-source:6

# apl-source:7
# السعر × (100 - الخصم) ÷ 100
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
  return س * (75) // 100
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(100), 75, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(250), 187, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(999), 749, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(40), 30, "حالة 4")
# apl-source:24
