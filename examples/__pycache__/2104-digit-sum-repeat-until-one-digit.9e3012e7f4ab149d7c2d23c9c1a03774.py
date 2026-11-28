
# apl-source:1
# مثال 2104 — الجذر الرقمي بالتكرار
# apl-source:2
# Digital root by repeated digit sum
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2104-digit-sum-repeat-until-one-digit.apl
# apl-source:6

# apl-source:7
# # نجمع أرقام العدد
# apl-source:8
# # ونكرر على الناتج
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
def جذر_رقمي(ن):
  # apl-source:19
  while ن >= 10:
    # apl-source:20
    مج = 0
    # apl-source:21
    for ر in str(ن):
      # apl-source:22
      مج = مج + int(ر)
    # apl-source:23
    ن = مج
  # apl-source:24
  return ن
# apl-source:25

# apl-source:26
تأكد_يساوي(جذر_رقمي(38), 2, "٣٨")
# apl-source:27
تأكد_يساوي(جذر_رقمي(0), 0, "صفر")
# apl-source:28
تأكد_يساوي(جذر_رقمي(9999), 9, "٩٩٩٩")
# apl-source:29
