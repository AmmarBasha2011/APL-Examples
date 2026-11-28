
# apl-source:1
# مثال 4868 — محيط مضلع منتظم عدد أضلاعه 8
# apl-source:2
# Perimeter of regular 8-gon
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4868-polygon-perimeter-8.apl
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
  return 8 * ض
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(1), 8, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(5), 40, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(12), 96, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(7), 56, "حالة 4")
# apl-source:24
