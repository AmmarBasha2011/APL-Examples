
# apl-source:1
# مثال 1461 — ضريبة بشرائح الدخل
# apl-source:2
# Income tax by brackets
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1461-income-tax-brackets.apl
# apl-source:6

# apl-source:7
# كل جزء من الدخل يخضع لنسبته
# apl-source:8
# النسب هنا بالمئة
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
def الضريبة(دخل):
  # apl-source:19
  حدود = [[1000, 0], [3000, 10], [6000, 20], [100000000, 30]]
  # apl-source:20
  سابق = 0
  # apl-source:21
  ضريبة = 0
  # apl-source:22
  for ح in حدود:
    # apl-source:23
    if دخل > سابق:
      # apl-source:24
      جزء = min(دخل, ح[0]) - سابق
      # apl-source:25
      ضريبة = ضريبة + جزء * ح[1] / 100
    # apl-source:26
    سابق = ح[0]
  # apl-source:27
  return ضريبة
# apl-source:28

# apl-source:29
تأكد_يساوي(الضريبة(500), 0.0, "معفى")
# apl-source:30
تأكد_يساوي(الضريبة(2000), 100.0, "شريحة ثانية")
# apl-source:31
تأكد_يساوي(الضريبة(5000), 600.0, "شريحة ثالثة")
# apl-source:32
تأكد_يساوي(الضريبة(8000), 1400.0, "شريحة رابعة")
# apl-source:33
