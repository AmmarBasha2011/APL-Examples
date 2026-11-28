
# apl-source:1
# مثال 1798 — مسافة هامنغ بين عددين
# apl-source:2
# Hamming distance between integers
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1798-hamming-distance-two-numbers.apl
# apl-source:6

# apl-source:7
# نطبق XOR
# apl-source:8
# نعد البتات المضاءة في الناتج
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
def هامنغ(أ, ب):
  # apl-source:19
  ف = أ ^ ب
  # apl-source:20
  عد = 0
  # apl-source:21
  while ف > 0:
    # apl-source:22
    عد = عد + (ف & 1)
    # apl-source:23
    ف = ف >> 1
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
تأكد_يساوي(هامنغ(1, 4), 2, "واحد وأربعة")
# apl-source:27
تأكد_يساوي(هامنغ(7, 7), 0, "متطابقان")
# apl-source:28
تأكد_يساوي(هامنغ(0, 15), 4, "أربعة بتات")
# apl-source:29
