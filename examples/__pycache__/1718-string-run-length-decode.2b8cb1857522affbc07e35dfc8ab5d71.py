
# apl-source:1
# مثال 1718 — فك ضغط التكرار المتتالي
# apl-source:2
# Run length decoding
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1718-string-run-length-decode.apl
# apl-source:6

# apl-source:7
# الأرقام تسبق الحرف
# apl-source:8
# نكرر الحرف بقدر العدد
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
def فك_الضغط(س):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  عدد = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح.isdigit():
      # apl-source:23
      عدد = عدد * 10 + int(ح)
    # apl-source:24
    else:
      # apl-source:25
      ناتج = ناتج + ح * عدد
      # apl-source:26
      عدد = 0
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(فك_الضغط("3a2b1c"), "aaabbc", "قصير")
# apl-source:30
تأكد_يساوي(فك_الضغط("10x"), "xxxxxxxxxx", "عشرة")
# apl-source:31
تأكد_يساوي(فك_الضغط(""), "", "فارغ")
# apl-source:32
