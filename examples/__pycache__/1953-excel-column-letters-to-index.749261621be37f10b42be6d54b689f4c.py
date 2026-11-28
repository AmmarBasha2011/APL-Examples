
# apl-source:1
# مثال 1953 — رقم عمود إكسل من اسمه
# apl-source:2
# Excel column number from title
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1953-excel-column-letters-to-index.apl
# apl-source:6

# apl-source:7
# # لكل حرف نضرب الناتج في 26 ونضيف قيمة الحرف
# apl-source:8
# # قيمة A هي 1
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
def رقم(س):
  # apl-source:19
  ن = 0
  # apl-source:20
  for ح in س:
    # apl-source:21
    ن = ن * 26 + (ord(ح) - 64)
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
تأكد_يساوي(رقم("A"), 1, "A")
# apl-source:25
تأكد_يساوي(رقم("AB"), 28, "AB")
# apl-source:26
تأكد_يساوي(رقم("ZY"), 701, "ZY")
# apl-source:27
تأكد_يساوي(رقم("AAA"), 703, "AAA")
# apl-source:28
