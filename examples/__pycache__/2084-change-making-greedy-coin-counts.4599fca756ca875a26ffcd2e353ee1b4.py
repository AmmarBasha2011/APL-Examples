
# apl-source:1
# مثال 2084 — عدد القطع في الباقي
# apl-source:2
# Greedy coin change counts
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2084-change-making-greedy-coin-counts.apl
# apl-source:6

# apl-source:7
# # الفئات 100 و25 و10 و5 و1
# apl-source:8
# # الجشع صحيح لهذه الفئات
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
def باقي(مبلغ):
  # apl-source:19
  فئات = [100, 25, 10, 5, 1]
  # apl-source:20
  عدد = []
  # apl-source:21
  for ف in فئات:
    # apl-source:22
    عدد = عدد + [مبلغ // ف]
    # apl-source:23
    مبلغ = مبلغ % ف
  # apl-source:24
  return عدد
# apl-source:25

# apl-source:26
تأكد_يساوي(باقي(289), [2, 3, 1, 0, 4], "٢٨٩")
# apl-source:27
تأكد_يساوي(باقي(0), [0, 0, 0, 0, 0], "صفر")
# apl-source:28
تأكد_يساوي(باقي(99), [0, 3, 2, 0, 4], "٩٩")
# apl-source:29
