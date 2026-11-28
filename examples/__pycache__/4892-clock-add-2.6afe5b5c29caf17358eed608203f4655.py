
# apl-source:1
# مثال 4892 — جمع 2 ساعات على الساعة (نظام 12)
# apl-source:2
# Add 2 hours on 12h clock
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4892-clock-add-2.apl
# apl-source:6

# apl-source:7
# نستخدم باقي القسمة على 12
# apl-source:8
# والصفر نحوله إلى 12
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
def ف(ح):
  # apl-source:19
  ن = (ح + 2) % 12
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 12
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 3, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(5), 7, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(10), 12, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(12), 2, "حالة 4")
# apl-source:28
