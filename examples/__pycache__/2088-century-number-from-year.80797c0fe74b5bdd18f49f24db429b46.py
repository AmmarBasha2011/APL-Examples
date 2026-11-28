
# apl-source:1
# مثال 2088 — رقم القرن من السنة
# apl-source:2
# Century from year
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2088-century-number-from-year.apl
# apl-source:6

# apl-source:7
# # نضيف 99 ثم نقسم على 100
# apl-source:8
# # السنة 101 بداية القرن الثاني
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
def قرن(س):
  # apl-source:19
  return (س + 99) // 100
# apl-source:20

# apl-source:21
تأكد_يساوي(قرن(1), 1, "١")
# apl-source:22
تأكد_يساوي(قرن(100), 1, "١٠٠")
# apl-source:23
تأكد_يساوي(قرن(101), 2, "١٠١")
# apl-source:24
تأكد_يساوي(قرن(2000), 20, "٢٠٠٠")
# apl-source:25
تأكد_يساوي(قرن(2026), 21, "٢٠٢٦")
# apl-source:26
