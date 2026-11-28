
# apl-source:1
# مثال 2120 — عدد يساوي مجموع مضروبات أرقامه
# apl-source:2
# Factorion check
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2120-factorion-digit-factorial-sum-check.apl
# apl-source:6

# apl-source:7
# # نحسب مضروب كل رقم
# apl-source:8
# # ونقارن المجموع
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
def مضروب(ن):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  for ك in range(2, ن + 1):
    # apl-source:21
    ناتج = ناتج * ك
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def فاكتوريون(ن):
  # apl-source:25
  مج = 0
  # apl-source:26
  for ر in str(ن):
    # apl-source:27
    مج = مج + مضروب(int(ر))
  # apl-source:28
  return مج == ن
# apl-source:29

# apl-source:30
تأكد_يساوي(فاكتوريون(145), True, "١٤٥")
# apl-source:31
تأكد_يساوي(فاكتوريون(40585), True, "٤٠٥٨٥")
# apl-source:32
تأكد_يساوي(فاكتوريون(100), False, "١٠٠")
# apl-source:33
تأكد_يساوي(فاكتوريون(1), True, "١")
# apl-source:34
تأكد_يساوي(فاكتوريون(2), True, "٢")
# apl-source:35
