
# apl-source:1
# مثال 4900 — جمع 6 ساعات على الساعة (نظام 12)
# apl-source:2
# Add 6 hours on 12h clock
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4900-clock-add-6.apl
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
  ن = (ح + 6) % 12
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 12
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 7, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(5), 11, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(10), 4, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(12), 6, "حالة 4")
# apl-source:28
