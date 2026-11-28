
# apl-source:1
# مثال 1972 — أطول تتابع في رميات العملة
# apl-source:2
# Longest run of coin flips
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1972-longest-run-in-coin-flips.apl
# apl-source:6

# apl-source:7
# # نزيد العداد إذا طابق الحرف السابق
# apl-source:8
# # وإلا نعيده إلى 1
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
def اطول(س):
  # apl-source:19
  if len(س) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  افضل = 1
  # apl-source:22
  حالي = 1
  # apl-source:23
  for ك in range(1, len(س)):
    # apl-source:24
    if س[ك] == س[ك - 1]:
      # apl-source:25
      حالي = حالي + 1
    # apl-source:26
    else:
      # apl-source:27
      حالي = 1
    # apl-source:28
    افضل = max(افضل, حالي)
  # apl-source:29
  return افضل
# apl-source:30

# apl-source:31
تأكد_يساوي(اطول("HHTHHHT"), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(اطول(""), 0, "فارغ")
# apl-source:33
تأكد_يساوي(اطول("TTTT"), 4, "كلها متشابهة")
# apl-source:34
تأكد_يساوي(اطول("HTHT"), 1, "متناوبة")
# apl-source:35
