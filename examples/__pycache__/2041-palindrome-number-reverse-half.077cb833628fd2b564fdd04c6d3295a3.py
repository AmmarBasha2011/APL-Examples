
# apl-source:1
# مثال 2041 — عدد متماثل بعكس النصف
# apl-source:2
# Palindrome number half reverse
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2041-palindrome-number-reverse-half.apl
# apl-source:6

# apl-source:7
# # نتوقف حين يصبح المعكوس أكبر من الباقي
# apl-source:8
# # العدد السالب أو المنتهي بصفر لا يكون متماثلا
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
def متماثل(ن):
  # apl-source:19
  if ن < 0 or (ن % 10 == 0 and ن != 0):
    # apl-source:20
    return False
  # apl-source:21
  م = 0
  # apl-source:22
  while ن > م:
    # apl-source:23
    م = م * 10 + ن % 10
    # apl-source:24
    ن = ن // 10
  # apl-source:25
  return ن == م or ن == م // 10
# apl-source:26

# apl-source:27
تأكد_يساوي(متماثل(121), True, "١٢١")
# apl-source:28
تأكد_يساوي(متماثل(-121), False, "سالب")
# apl-source:29
تأكد_يساوي(متماثل(10), False, "١٠")
# apl-source:30
تأكد_يساوي(متماثل(12321), True, "فردي")
# apl-source:31
تأكد_يساوي(متماثل(0), True, "صفر")
# apl-source:32
