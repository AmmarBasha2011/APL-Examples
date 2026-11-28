
# apl-source:1
# مثال 5116 — سعر متدرج بحد 6
# apl-source:2
# Tiered price with cutoff 6
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5116-tier-price-6.apl
# apl-source:6

# apl-source:7
# أول 6 وحدات بسعر 3 والباقي بسعر 2
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
def ف(ن):
  # apl-source:18
  if ن <= 6:
    # apl-source:19
    return ن * 3
  # apl-source:20
  return 6 * 3 + (ن - 6) * 2
# apl-source:21

# apl-source:22
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:23
تأكد_يساوي(ف(1), 3, "حالة 2")
# apl-source:24
تأكد_يساوي(ف(6), 18, "حالة 3")
# apl-source:25
تأكد_يساوي(ف(11), 28, "حالة 4")
# apl-source:26
تأكد_يساوي(ف(18), 42, "حالة 5")
# apl-source:27
