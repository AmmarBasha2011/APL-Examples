
# apl-source:1
# مثال 971 — التجزئة الجغرافية
# apl-source:2
# Geohash encoding
# apl-source:3
# Demonstrates: تعشيق بتات الطول والعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/971-geohash.apl
# apl-source:6

# apl-source:7
# التجزئة الجغرافية: ترميز خط العرض والطول في سلسلة قصيرة
# apl-source:8
# تعشيق بتات الطول والعرض ثم تجميعها خمساً بخمساً
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
قاعدة = "0123456789bcdefghjkmnpqrstuvwxyz"
# apl-source:19

# apl-source:20
def جيوهاش(عرض, طول_ج, دقة):
  # apl-source:21
  أدنى_عرض = -90
  # apl-source:22
  أقصى_عرض = 90
  # apl-source:23
  أدنى_طول = -180
  # apl-source:24
  أقصى_طول = 180
  # apl-source:25
  بتات = []
  # apl-source:26
  زوجي = 1
  # apl-source:27
  while len(بتات) < (دقة * 5):
    # apl-source:28
    if زوجي == 1:
      # apl-source:29
      وسط = (أدنى_طول + أقصى_طول) / 2
      # apl-source:30
      if طول_ج >= وسط:
        # apl-source:31
        بتات = بتات + [1]
        # apl-source:32
        أدنى_طول = وسط
      # apl-source:33
      else:
        # apl-source:34
        بتات = بتات + [0]
        # apl-source:35
        أقصى_طول = وسط
      # apl-source:36
      زوجي = 0
    # apl-source:37
    else:
      # apl-source:38
      وسط = (أدنى_عرض + أقصى_عرض) / 2
      # apl-source:39
      if عرض >= وسط:
        # apl-source:40
        بتات = بتات + [1]
        # apl-source:41
        أدنى_عرض = وسط
      # apl-source:42
      else:
        # apl-source:43
        بتات = بتات + [0]
        # apl-source:44
        أقصى_عرض = وسط
      # apl-source:45
      زوجي = 1
  # apl-source:46
  ناتج = ""
  # apl-source:47
  for ق in range(0, دقة * 5, 5):
    # apl-source:48
    ف = 0
    # apl-source:49
    for ب in range(5):
      # apl-source:50
      ف = (ف * 2) + بتات[ق + ب]
    # apl-source:51
    ناتج = ناتج + قاعدة[ف]
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
القاهرة = جيوهاش(30.0444, 31.2357, 6)
# apl-source:55
تأكد_يساوي(len(القاهرة), 6, "طول الترميز")
# apl-source:56
تأكد_يساوي(القاهرة[0], "s", "الحرف الأول")
# apl-source:57
تأكد_يساوي(القاهرة[1], "t", "الحرف الثاني")
# apl-source:58
تأكد_يساوي(القاهرة[2], "q", "الحرف الثالث")
# apl-source:59
تأكد_يساوي(القاهرة[3], "4", "الحرف الرابع")
# apl-source:60
تأكد_يساوي(القاهرة[4], "y", "الحرف الخامس")
# apl-source:61
تأكد_يساوي(القاهرة[5], "v", "الحرف السادس")
# apl-source:62
