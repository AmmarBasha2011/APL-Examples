
# apl-source:1
# مثال 1296 — أول إصدار سيئ
# apl-source:2
# First bad version
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1296-data-stream-first-bad.apl
# apl-source:6

# apl-source:7
# الإصدارات بعد السيئ كلها سيئة
# apl-source:8
# فنبحث ثنائياً عن أول سيئ
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
def اول_سيئ(ن, الاول_السيئ):
  # apl-source:19
  يسار = 1
  # apl-source:20
  يمين = ن
  # apl-source:21
  استدعاءات = 0
  # apl-source:22
  while يسار < يمين:
    # apl-source:23
    وسط = (يسار + يمين) // 2
    # apl-source:24
    استدعاءات = استدعاءات + 1
    # apl-source:25
    if وسط >= الاول_السيئ:
      # apl-source:26
      يمين = وسط
    # apl-source:27
    else:
      # apl-source:28
      يسار = وسط + 1
  # apl-source:29
  return [يسار, استدعاءات]
# apl-source:30

# apl-source:31
تأكد_يساوي(اول_سيئ(5, 4)[0], 4, "خمسة")
# apl-source:32
تأكد_يساوي(اول_سيئ(1, 1)[0], 1, "واحد")
# apl-source:33
تأكد_يساوي(اول_سيئ(1000, 777)[0], 777, "ألف")
# apl-source:34
تأكد_يساوي(اول_سيئ(1000, 777)[1] <= 10, True, "عدد قليل من الاستدعاءات")
# apl-source:35
