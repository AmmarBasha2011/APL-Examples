
# apl-source:1
# مثال 2138 — مسافة هامنج بين نصين
# apl-source:2
# Hamming distance strings
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2138-hamming-distance-between-two-strings.apl
# apl-source:6

# apl-source:7
# # نقارن حرفا بحرف
# apl-source:8
# # 3 بين karolin وkathrin
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
def مسافة(ا, ب):
  # apl-source:19
  عدد = 0
  # apl-source:20
  for ك in range(len(ا)):
    # apl-source:21
    if ا[ك] != ب[ك]:
      # apl-source:22
      عدد = عدد + 1
  # apl-source:23
  return عدد
# apl-source:24

# apl-source:25
تأكد_يساوي(مسافة("karolin", "kathrin"), 3, "حروف")
# apl-source:26
تأكد_يساوي(مسافة("1011101", "1001001"), 2, "ثنائي")
# apl-source:27
تأكد_يساوي(مسافة("", ""), 0, "فارغ")
# apl-source:28
