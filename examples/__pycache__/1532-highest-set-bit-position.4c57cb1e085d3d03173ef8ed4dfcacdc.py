
# apl-source:1
# مثال 1532 — موضع أعلى بت
# apl-source:2
# Highest set bit position
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1532-highest-set-bit-position.apl
# apl-source:6

# apl-source:7
# نزيح لليمين حتى يصير العدد صفراً
# apl-source:8
# عدد الإزاحات ناقص واحد هو الموضع
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
def أعلى_بت(ن):
  # apl-source:19
  if ن <= 0:
    # apl-source:20
    return -1
  # apl-source:21
  موضع = -1
  # apl-source:22
  while ن > 0:
    # apl-source:23
    ن = ن >> 1
    # apl-source:24
    موضع = موضع + 1
  # apl-source:25
  return موضع
# apl-source:26

# apl-source:27
تأكد_يساوي(أعلى_بت(1), 0, "واحد")
# apl-source:28
تأكد_يساوي(أعلى_بت(8), 3, "ثمانية")
# apl-source:29
تأكد_يساوي(أعلى_بت(255), 7, "255")
# apl-source:30
تأكد_يساوي(أعلى_بت(0), -1, "صفر")
# apl-source:31
