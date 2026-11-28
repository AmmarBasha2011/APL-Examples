
# apl-source:1
# مثال 1656 — حاصل ضرب أرقام العدد
# apl-source:2
# Product of digits
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1656-product-of-digits.apl
# apl-source:6

# apl-source:7
# الصفر في العدد يصفّر الناتج
# apl-source:8
# نفصل الأرقام بالباقي والقسمة
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
def ضرب_الأرقام(ن):
  # apl-source:19
  حاصل = 1
  # apl-source:20
  while ن > 0:
    # apl-source:21
    حاصل = حاصل * (ن % 10)
    # apl-source:22
    ن = ن // 10
  # apl-source:23
  return حاصل
# apl-source:24

# apl-source:25
تأكد_يساوي(ضرب_الأرقام(234), 24, "ثلاثة أرقام")
# apl-source:26
تأكد_يساوي(ضرب_الأرقام(105), 0, "فيه صفر")
# apl-source:27
تأكد_يساوي(ضرب_الأرقام(7), 7, "رقم واحد")
# apl-source:28
