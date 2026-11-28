
# apl-source:1
# مثال 1080 — الخانة رقم ن
# apl-source:2
# Nth digit of the infinite integer sequence
# apl-source:3
# Demonstrates: عد الخانات بالمجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1080-nth-digit.apl
# apl-source:6

# apl-source:7
# الأعداد بخانة واحدة تسع خانات وبخانتين مئة وثمانون وهكذا
# apl-source:8
# نقفز بالمجموعات ثم نحدد العدد والخانة
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
def خانة(ن):
  # apl-source:19
  ط = 1
  # apl-source:20
  عدد_ = 9
  # apl-source:21
  بداية = 1
  # apl-source:22
  while ن > (ط * عدد_):
    # apl-source:23
    ن = ن - (ط * عدد_)
    # apl-source:24
    ط = ط + 1
    # apl-source:25
    عدد_ = عدد_ * 10
    # apl-source:26
    بداية = بداية * 10
  # apl-source:27
  رقم = بداية + ((ن - 1) // ط)
  # apl-source:28
  return int(str(رقم)[(ن - 1) % ط])
# apl-source:29

# apl-source:30
تأكد_يساوي(خانة(3), 3, "الثالثة")
# apl-source:31
تأكد_يساوي(خانة(11), 0, "الحادية عشرة")
# apl-source:32
تأكد_يساوي(خانة(15), 2, "الخامسة عشرة")
# apl-source:33
تأكد_يساوي(خانة(10), 1, "العاشرة")
# apl-source:34
