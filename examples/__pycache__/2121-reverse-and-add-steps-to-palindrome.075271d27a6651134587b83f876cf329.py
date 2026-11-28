
# apl-source:1
# مثال 2121 — عدد خطوات العكس والجمع حتى التماثل
# apl-source:2
# Reverse and add steps
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2121-reverse-and-add-steps-to-palindrome.apl
# apl-source:6

# apl-source:7
# # 89 يحتاج 24 خطوة
# apl-source:8
# # 56 يحتاج خطوة واحدة
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
def خطوات(ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  while str(ن) != str(ن)[::-1]:
    # apl-source:21
    ن = ن + int(str(ن)[::-1])
    # apl-source:22
    عدد = عدد + 1
  # apl-source:23
  return عدد
# apl-source:24

# apl-source:25
تأكد_يساوي(خطوات(56), 1, "٥٦")
# apl-source:26
تأكد_يساوي(خطوات(87), 4, "٨٧")
# apl-source:27
تأكد_يساوي(خطوات(11), 0, "١١")
# apl-source:28
تأكد_يساوي(خطوات(89), 24, "٨٩")
# apl-source:29
