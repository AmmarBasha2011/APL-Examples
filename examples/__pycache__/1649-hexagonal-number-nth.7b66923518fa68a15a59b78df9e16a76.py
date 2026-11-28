
# apl-source:1
# مثال 1649 — العدد السداسي رقم ن
# apl-source:2
# Nth hexagonal number
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1649-hexagonal-number-nth.apl
# apl-source:6

# apl-source:7
# الأعداد السداسية تمثل نقاطاً في سداسيات متداخلة
# apl-source:8
# كل عدد سداسي مثلثي أيضاً
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
def سداسي(ن):
  # apl-source:19
  return ن * (2 * ن - 1)
# apl-source:20

# apl-source:21
تأكد_يساوي(سداسي(1), 1, "الأول")
# apl-source:22
تأكد_يساوي(سداسي(2), 6, "الثاني")
# apl-source:23
تأكد_يساوي(سداسي(5), 45, "الخامس")
# apl-source:24
تأكد_يساوي(سداسي(10), 190, "العاشر")
# apl-source:25
