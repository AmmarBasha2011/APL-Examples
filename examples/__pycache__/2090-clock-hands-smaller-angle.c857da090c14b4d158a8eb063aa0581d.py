
# apl-source:1
# مثال 2090 — الزاوية الصغرى بين عقربي الساعة
# apl-source:2
# Clock hands angle
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2090-clock-hands-smaller-angle.apl
# apl-source:6

# apl-source:7
# # نحسب الفرق المطلق
# apl-source:8
# # ونأخذ الأصغر من الزاوية ومتممتها
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
def زاوية(س, د):
  # apl-source:19
  ا = abs(30 * (س % 12) - 5.5 * د)
  # apl-source:20
  return min(ا, 360 - ا)
# apl-source:21

# apl-source:22
تأكد_يساوي(زاوية(3, 0), 90, "الثالثة")
# apl-source:23
تأكد_يساوي(زاوية(12, 0), 0, "الثانية عشرة")
# apl-source:24
تأكد_يساوي(زاوية(6, 0), 180, "السادسة")
# apl-source:25
تأكد_يساوي(زاوية(3, 15), 7.5, "٣:١٥")
# apl-source:26
تأكد_يساوي(زاوية(12, 30), 165, "١٢:٣٠")
# apl-source:27
