
# apl-source:1
# مثال 1025 — الفجوة الثنائية
# apl-source:2
# Binary gap
# apl-source:3
# Demonstrates: فحص بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1025-binary-gap.apl
# apl-source:6

# apl-source:7
# نمر على بتات العدد من اليمين
# apl-source:8
# نقيس أطول مجموعة أصفار محصورة بين بتين واحدين
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
def فجوة(ن):
  # apl-source:19
  أطول = 0
  # apl-source:20
  عد = 0
  # apl-source:21
  بدأ = False
  # apl-source:22
  while ن > 0:
    # apl-source:23
    if ن % 2 == 1:
      # apl-source:24
      if بدأ and (عد > أطول):
        # apl-source:25
        أطول = عد
      # apl-source:26
      بدأ = True
      # apl-source:27
      عد = 0
    # apl-source:28
    else:
      # apl-source:29
      عد = عد + 1
    # apl-source:30
    ن = ن // 2
  # apl-source:31
  return أطول
# apl-source:32

# apl-source:33
تأكد_يساوي(فجوة(9), 2, "1001")
# apl-source:34
تأكد_يساوي(فجوة(529), 4, "1000010001")
# apl-source:35
تأكد_يساوي(فجوة(20), 1, "10100")
# apl-source:36
تأكد_يساوي(فجوة(15), 0, "1111")
# apl-source:37
تأكد_يساوي(فجوة(32), 0, "صفار نهائية فقط")
# apl-source:38
