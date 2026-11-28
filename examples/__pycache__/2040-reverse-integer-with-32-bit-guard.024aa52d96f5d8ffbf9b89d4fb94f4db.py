
# apl-source:1
# مثال 2040 — عكس أرقام العدد مع حد 32 بت
# apl-source:2
# Reverse integer 32-bit guard
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2040-reverse-integer-with-32-bit-guard.apl
# apl-source:6

# apl-source:7
# # نحفظ الإشارة ونعكس القيمة المطلقة
# apl-source:8
# # ونفحص الحد الأعلى
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
def اعكس(ن):
  # apl-source:19
  اشارة = 1
  # apl-source:20
  if ن < 0:
    # apl-source:21
    اشارة = -1
    # apl-source:22
    ن = -ن
  # apl-source:23
  م = 0
  # apl-source:24
  while ن > 0:
    # apl-source:25
    م = م * 10 + ن % 10
    # apl-source:26
    ن = ن // 10
  # apl-source:27
  if م > 2147483647:
    # apl-source:28
    return 0
  # apl-source:29
  return اشارة * م
# apl-source:30

# apl-source:31
تأكد_يساوي(اعكس(123), 321, "موجب")
# apl-source:32
تأكد_يساوي(اعكس(-123), -321, "سالب")
# apl-source:33
تأكد_يساوي(اعكس(120), 21, "صفر في النهاية")
# apl-source:34
تأكد_يساوي(اعكس(1534236469), 0, "تجاوز")
# apl-source:35
