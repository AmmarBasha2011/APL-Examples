
# apl-source:1
# مثال 1795 — رقم عمود إكسل من اسمه
# apl-source:2
# Excel column number from title
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1795-excel-column-number-from-title.apl
# apl-source:6

# apl-source:7
# كل حرف رقم من 1 إلى 26
# apl-source:8
# نضرب المجموع بـ 26 كل مرة
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
def رقم_العمود(س):
  # apl-source:19
  أبجد = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # apl-source:20
  ناتج = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    ناتج = ناتج * 26 + أبجد.find(ح) + 1
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(رقم_العمود("A"), 1, "A")
# apl-source:26
تأكد_يساوي(رقم_العمود("AB"), 28, "AB")
# apl-source:27
تأكد_يساوي(رقم_العمود("ZY"), 701, "ZY")
# apl-source:28
