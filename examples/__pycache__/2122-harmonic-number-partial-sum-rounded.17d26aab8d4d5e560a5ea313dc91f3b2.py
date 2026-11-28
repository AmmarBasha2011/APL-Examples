
# apl-source:1
# مثال 2122 — مجموع المتسلسلة التوافقية
# apl-source:2
# Harmonic number partial sum
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2122-harmonic-number-partial-sum-rounded.apl
# apl-source:6

# apl-source:7
# # نقرب الناتج
# apl-source:8
# # H(4) = 25/12
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
def توافقي(ن):
  # apl-source:19
  مج = 0.0
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    مج = مج + 1 / ك
  # apl-source:22
  return مج
# apl-source:23

# apl-source:24
تأكد_يساوي(round(توافقي(1), 4), 1.0, "H١")
# apl-source:25
تأكد_يساوي(round(توافقي(4), 4), 2.0833, "H٤")
# apl-source:26
تأكد_يساوي(round(توافقي(10), 3), 2.929, "H١٠")
# apl-source:27
