
# apl-source:1
# مثال 1894 — عدد حلول الملكات
# apl-source:2
# Count N-Queens solutions
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1894-n-queens-count-solutions.apl
# apl-source:6

# apl-source:7
# نضع ملكة في كل صف على عمود آمن
# apl-source:8
# نفحص العمود والقطرين
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
def آمن(مواضع, صف, عمود):
  # apl-source:19
  for ص in range(صف):
    # apl-source:20
    ع = مواضع[ص]
    # apl-source:21
    if ع == عمود:
      # apl-source:22
      return False
    # apl-source:23
    if ع - عمود == ص - صف:
      # apl-source:24
      return False
    # apl-source:25
    if عمود - ع == ص - صف:
      # apl-source:26
      return False
  # apl-source:27
  return True
# apl-source:28

# apl-source:29
def ملكات(ن, مواضع):
  # apl-source:30
  صف = len(مواضع)
  # apl-source:31
  if صف == ن:
    # apl-source:32
    return 1
  # apl-source:33
  عد = 0
  # apl-source:34
  for عمود in range(ن):
    # apl-source:35
    if آمن(مواضع, صف, عمود):
      # apl-source:36
      عد = عد + ملكات(ن, مواضع + [عمود])
  # apl-source:37
  return عد
# apl-source:38

# apl-source:39
تأكد_يساوي(ملكات(4, []), 2, "رقعة ٤")
# apl-source:40
تأكد_يساوي(ملكات(5, []), 10, "رقعة ٥")
# apl-source:41
تأكد_يساوي(ملكات(6, []), 4, "رقعة ٦")
# apl-source:42
