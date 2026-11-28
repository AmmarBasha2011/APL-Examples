
# apl-source:1
# مثال 1510 — فك ضغط التكرار
# apl-source:2
# Run length decode
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1510-run-length-decode-string.apl
# apl-source:6

# apl-source:7
# نقرأ الرقم ثم الحرف
# apl-source:8
# نكرر الحرف بقدر الرقم
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
def فك_الضغط(نص_):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  رقم = ""
  # apl-source:21
  for ح in نص_:
    # apl-source:22
    if ح.isdigit():
      # apl-source:23
      رقم = رقم + ح
    # apl-source:24
    else:
      # apl-source:25
      if رقم == "":
        # apl-source:26
        ناتج = ناتج + ح
      # apl-source:27
      else:
        # apl-source:28
        ناتج = ناتج + ح * int(رقم)
      # apl-source:29
      رقم = ""
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(فك_الضغط("3a2b"), "aaabb", "بسيط")
# apl-source:33
تأكد_يساوي(فك_الضغط("a3b"), "abbb", "حرف مفرد")
# apl-source:34
تأكد_يساوي(فك_الضغط("10x"), "xxxxxxxxxx", "رقمان")
# apl-source:35
