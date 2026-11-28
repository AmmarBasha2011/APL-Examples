
# apl-source:1
# مثال 1233 — كوكو والموز
# apl-source:2
# Koko eating bananas
# apl-source:3
# Demonstrates: بحث ثنائي على الجواب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1233-koko-bananas.apl
# apl-source:6

# apl-source:7
# نبحث ثنائياً عن السرعة
# apl-source:8
# والساعات اللازمة مجموع سقف قسمة كل كومة على السرعة
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
def ساعات(اكوام, سرعة):
  # apl-source:19
  مج = 0
  # apl-source:20
  for ك in اكوام:
    # apl-source:21
    مج = مج + (ك + سرعة - 1) // سرعة
  # apl-source:22
  return مج
# apl-source:23

# apl-source:24
def اقل_سرعة(اكوام, ساعات_):
  # apl-source:25
  يسار = 1
  # apl-source:26
  يمين = 1
  # apl-source:27
  for ك in اكوام:
    # apl-source:28
    if ك > يمين:
      # apl-source:29
      يمين = ك
  # apl-source:30
  while يسار < يمين:
    # apl-source:31
    وسط = (يسار + يمين) // 2
    # apl-source:32
    if ساعات(اكوام, وسط) <= ساعات_:
      # apl-source:33
      يمين = وسط
    # apl-source:34
    else:
      # apl-source:35
      يسار = وسط + 1
  # apl-source:36
  return يسار
# apl-source:37

# apl-source:38
تأكد_يساوي(اقل_سرعة([3,6,7,11], 8), 4, "مثال أول")
# apl-source:39
تأكد_يساوي(اقل_سرعة([30,11,23,4,20], 5), 30, "خمس ساعات")
# apl-source:40
تأكد_يساوي(اقل_سرعة([30,11,23,4,20], 6), 23, "ست ساعات")
# apl-source:41
