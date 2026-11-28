
# apl-source:1
# مثال 1397 — حاصل ضرب متماثل
# apl-source:2
# Largest palindromic product
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1397-palindromic-product.apl
# apl-source:6

# apl-source:7
# نجرب كل الأزواج من الأكبر
# apl-source:8
# ونقارن النص بنص_عكسيه
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
  ن_نص = str(ن)
  # apl-source:20
  نص_عكسي = ""
  # apl-source:21
  for ح in ن_نص:
    # apl-source:22
    نص_عكسي = ح + نص_عكسي
  # apl-source:23
  return ن_نص == نص_عكسي
# apl-source:24

# apl-source:25
def اكبر_حاصل(ارقام):
  # apl-source:26
  ادنى = 10 ** (ارقام - 1)
  # apl-source:27
  اعلى = 10 ** ارقام - 1
  # apl-source:28
  افضل = 0
  # apl-source:29
  for أ in range(اعلى, ادنى - 1, -1):
    # apl-source:30
    for ب in range(أ, ادنى - 1, -1):
      # apl-source:31
      ض = أ * ب
      # apl-source:32
      if ض > افضل:
        # apl-source:33
        if متماثل(ض):
          # apl-source:34
          افضل = ض
  # apl-source:35
  return افضل
# apl-source:36

# apl-source:37
تأكد_يساوي(اكبر_حاصل(1), 9, "رقم واحد")
# apl-source:38
تأكد_يساوي(اكبر_حاصل(2), 9009, "رقمان")
# apl-source:39
تأكد_يساوي(متماثل(12321), True, "متماثل")
# apl-source:40
