
# apl-source:1
# مثال 2085 — تقريب القروش لأقرب خمسة
# apl-source:2
# Round cents to nearest five
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2085-round-cents-to-nearest-five.apl
# apl-source:6

# apl-source:7
# # التقريب يميل للأعلى عند النصف
# apl-source:8
# # مثل تقريب أسعار النقد
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
def قرب(ق):
  # apl-source:19
  return (ق + 2) // 5 * 5
# apl-source:20

# apl-source:21
تأكد_يساوي(قرب(123), 125, "١٢٣")
# apl-source:22
تأكد_يساوي(قرب(122), 120, "١٢٢")
# apl-source:23
تأكد_يساوي(قرب(125), 125, "١٢٥")
# apl-source:24
تأكد_يساوي(قرب(0), 0, "صفر")
# apl-source:25
