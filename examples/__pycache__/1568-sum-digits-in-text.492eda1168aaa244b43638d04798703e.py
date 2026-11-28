
# apl-source:1
# مثال 1568 — مجموع أرقام نص
# apl-source:2
# Sum of digits inside text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1568-sum-digits-in-text.apl
# apl-source:6

# apl-source:7
# نتجاهل ما ليس رقماً
# apl-source:8
# نحول الرقم من نص إلى عدد
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
def مجموع_أرقام_النص(نص_):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح.isdigit():
      # apl-source:22
      مجموع = مجموع + int(ح)
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
تأكد_يساوي(مجموع_أرقام_النص("a1b2c3"), 6, "ثلاثة أرقام")
# apl-source:26
تأكد_يساوي(مجموع_أرقام_النص("no digits"), 0, "بلا أرقام")
# apl-source:27
تأكد_يساوي(مجموع_أرقام_النص("room 404"), 8, "غرفة")
# apl-source:28
