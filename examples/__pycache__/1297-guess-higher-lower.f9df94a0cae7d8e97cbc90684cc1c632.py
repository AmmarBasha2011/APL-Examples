
# apl-source:1
# مثال 1297 — خمن أعلى أم أقل
# apl-source:2
# Guess number higher or lower
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1297-guess-higher-lower.apl
# apl-source:6

# apl-source:7
# كل تخمين يخبرنا بالاتجاه
# apl-source:8
# فنقسم المدى نصفين
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
def خمن(ن, سر):
  # apl-source:19
  يسار = 1
  # apl-source:20
  يمين = ن
  # apl-source:21
  محاولات = 0
  # apl-source:22
  while يسار <= يمين:
    # apl-source:23
    وسط = (يسار + يمين) // 2
    # apl-source:24
    محاولات = محاولات + 1
    # apl-source:25
    if وسط == سر:
      # apl-source:26
      return محاولات
    # apl-source:27
    elif وسط < سر:
      # apl-source:28
      يسار = وسط + 1
    # apl-source:29
    else:
      # apl-source:30
      يمين = وسط - 1
  # apl-source:31
  return -1
# apl-source:32

# apl-source:33
تأكد_يساوي(خمن(10, 6) <= 4, True, "عشرة")
# apl-source:34
تأكد_يساوي(خمن(1, 1), 1, "واحد")
# apl-source:35
تأكد_يساوي(خمن(1000, 1) <= 10, True, "الحد الأدنى")
# apl-source:36
تأكد_يساوي(خمن(1000, 1000) <= 10, True, "الحد الأعلى")
# apl-source:37
