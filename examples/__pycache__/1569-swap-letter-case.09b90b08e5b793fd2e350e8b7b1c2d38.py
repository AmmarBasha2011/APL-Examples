
# apl-source:1
# مثال 1569 — عكس حالة الأحرف
# apl-source:2
# Swap letter case
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1569-swap-letter-case.apl
# apl-source:6

# apl-source:7
# نفحص كل حرف
# apl-source:8
# نقلب حالته إن كان حرفاً
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
def اعكس_الحالة(نص_):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح.isupper():
      # apl-source:22
      ناتج = ناتج + ح.lower()
    # apl-source:23
    elif ح.islower():
      # apl-source:24
      ناتج = ناتج + ح.upper()
    # apl-source:25
    else:
      # apl-source:26
      ناتج = ناتج + ح
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(اعكس_الحالة("Hello World"), "hELLO wORLD", "جملة")
# apl-source:30
تأكد_يساوي(اعكس_الحالة("A1b2"), "a1B2", "أرقام")
# apl-source:31
تأكد_يساوي(اعكس_الحالة(""), "", "فارغ")
# apl-source:32
