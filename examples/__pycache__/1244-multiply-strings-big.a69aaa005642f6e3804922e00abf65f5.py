
# apl-source:1
# مثال 1244 — ضرب أعداد نصية
# apl-source:2
# Multiply big numbers as digit lists
# apl-source:3
# Demonstrates: ضرب طويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1244-multiply-strings-big.apl
# apl-source:6

# apl-source:7
# نضرب كل رقمين ونجمع في الخانة المناسبة
# apl-source:8
# ثم نمرر الحمل
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
def اضرب(أ, ب):
  # apl-source:19
  if (أ == "0") or (ب == "0"):
    # apl-source:20
    return "0"
  # apl-source:21
  ن = len(أ)
  # apl-source:22
  م = len(ب)
  # apl-source:23
  نتيجة = [0] * (ن + م)
  # apl-source:24
  for ع in range(ن - 1, -1, -1):
    # apl-source:25
    for ج in range(م - 1, -1, -1):
      # apl-source:26
      ح = int(أ[ع]) * int(ب[ج]) + نتيجة[ع + ج + 1]
      # apl-source:27
      نتيجة[ع + ج + 1] = ح % 10
      # apl-source:28
      نتيجة[ع + ج] = نتيجة[ع + ج] + ح // 10
  # apl-source:29
  ناتج = ""
  # apl-source:30
  for ر in نتيجة:
    # apl-source:31
    ناتج = ناتج + str(ر)
  # apl-source:32
  return ناتج.lstrip("0")
# apl-source:33

# apl-source:34
تأكد_يساوي(اضرب("2", "3"), "6", "صغير")
# apl-source:35
تأكد_يساوي(اضرب("123", "456"), "56088", "ثلاثة أرقام")
# apl-source:36
تأكد_يساوي(اضرب("999", "999"), "998001", "تسعات")
# apl-source:37
تأكد_يساوي(اضرب("0", "12345"), "0", "صفر")
# apl-source:38
تأكد_يساوي(اضرب("123456789", "987654321"), str(121932631112635269), "كبير")
# apl-source:39
