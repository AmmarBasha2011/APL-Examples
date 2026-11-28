
# apl-source:1
# مثال 1750 — أكبر مجموع صف أو عمود
# apl-source:2
# Max row or column sum
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1750-matrix-row-column-max-sums.apl
# apl-source:6

# apl-source:7
# نجمع كل صف وكل عمود
# apl-source:8
# نأخذ الأكبر
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
def أكبر_مجموع(م):
  # apl-source:19
  أفضل = 0
  # apl-source:20
  for ي in range(len(م)):
    # apl-source:21
    مجموع = 0
    # apl-source:22
    for ك in range(len(م[0])):
      # apl-source:23
      مجموع = مجموع + م[ي][ك]
    # apl-source:24
    أفضل = max(أفضل, مجموع)
  # apl-source:25
  for ك in range(len(م[0])):
    # apl-source:26
    مجموع = 0
    # apl-source:27
    for ي in range(len(م)):
      # apl-source:28
      مجموع = مجموع + م[ي][ك]
    # apl-source:29
    أفضل = max(أفضل, مجموع)
  # apl-source:30
  return أفضل
# apl-source:31

# apl-source:32
تأكد_يساوي(أكبر_مجموع([[1, 2], [3, 4]]), 7, "عمود")
# apl-source:33
تأكد_يساوي(أكبر_مجموع([[5, 5], [0, 0]]), 10, "صف")
# apl-source:34
