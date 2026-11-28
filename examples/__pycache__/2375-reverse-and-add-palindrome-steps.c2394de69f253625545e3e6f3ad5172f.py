
# apl-source:1
# مثال 2375 — انعكاس وجمع حتى التناظر
# apl-source:2
# Reverse and add steps
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2375-reverse-and-add-palindrome-steps.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  خ = 0
  # apl-source:20
  while str(ن) != str(ن)[::-1]:
    # apl-source:21
    ن = ن + int(str(ن)[::-1])
    # apl-source:22
    خ = خ + 1
  # apl-source:23
  return خ
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(11), 0, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(56), 1, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(57), 2, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(89), 24, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(10), 1, "حالة 5")
# apl-source:30
