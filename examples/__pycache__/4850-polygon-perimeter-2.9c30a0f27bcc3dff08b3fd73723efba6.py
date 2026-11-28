
# apl-source:1
# مثال 4850 — محيط مضلع منتظم عدد أضلاعه 2
# apl-source:2
# Perimeter of regular 2-gon
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4850-polygon-perimeter-2.apl
# apl-source:6

# apl-source:7
# المحيط = عدد الأضلاع × طول الضلع
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ض):
  # apl-source:18
  return 2 * ض
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(1), 2, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(5), 10, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(12), 24, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(7), 14, "حالة 4")
# apl-source:24
