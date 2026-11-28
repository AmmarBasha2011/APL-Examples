
# apl-source:1
# مثال 2131 — خطوات روتين كابريكار إلى 6174
# apl-source:2
# Kaprekar routine steps
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2131-kaprekar-routine-steps-to-6174.apl
# apl-source:6

# apl-source:7
# # نحافظ على أربع خانات بالأصفار
# apl-source:8
# # 3524 يحتاج 3 خطوات
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
def خطوات(ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  while ن != 6174:
    # apl-source:21
    س = sorted(str(ن).zfill(4))
    # apl-source:22
    ا = int("".join(س))
    # apl-source:23
    س.reverse()
    # apl-source:24
    ب = int("".join(س))
    # apl-source:25
    ن = ب - ا
    # apl-source:26
    عدد = عدد + 1
  # apl-source:27
  return عدد
# apl-source:28

# apl-source:29
تأكد_يساوي(خطوات(3524), 3, "٣٥٢٤")
# apl-source:30
تأكد_يساوي(خطوات(6174), 0, "٦١٧٤")
# apl-source:31
تأكد_يساوي(خطوات(1000), 5, "١٠٠٠")
# apl-source:32
