
# apl-source:1
# مثال 4848 — سعر بعد خصم 75%
# apl-source:2
# Price after 75 percent discount
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4848-discount-75.apl
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
  return س * (25) // 100
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(100), 25, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(250), 62, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(999), 249, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(40), 10, "حالة 4")
# apl-source:24
