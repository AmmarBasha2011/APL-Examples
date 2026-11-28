
# apl-source:1
# مثال 1083 — رقم عمود إكسل
# apl-source:2
# Excel column title to number
# apl-source:3
# Demonstrates: نظام عد بأساس 26
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1083-excel-title-number.apl
# apl-source:6

# apl-source:7
# كل حرف رقمه من 1 إلى 26
# apl-source:8
# ننتقل من اليسار فنضرب المجموع في 26 ونضيف الحرف
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
def رقم_عمود(اسم):
  # apl-source:19
  حروف = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # apl-source:20
  ناتج = 0
  # apl-source:21
  for ح in اسم:
    # apl-source:22
    ف = 0
    # apl-source:23
    while حروف[ف] != ح:
      # apl-source:24
      ف = ف + 1
    # apl-source:25
    ناتج = (ناتج * 26) + (ف + 1)
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(رقم_عمود("A"), 1, "الأول")
# apl-source:29
تأكد_يساوي(رقم_عمود("AB"), 28, "AB")
# apl-source:30
تأكد_يساوي(رقم_عمود("ZY"), 701, "ZY")
# apl-source:31
تأكد_يساوي(رقم_عمود("Z"), 26, "الأخير")
# apl-source:32
