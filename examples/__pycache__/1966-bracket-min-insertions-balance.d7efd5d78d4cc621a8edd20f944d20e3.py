
# apl-source:1
# مثال 1966 — أقل إضافات لتوازن الأقواس
# apl-source:2
# Minimum insertions to balance
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1966-bracket-min-insertions-balance.apl
# apl-source:6

# apl-source:7
# # نتتبع عدد الفتحات المفتوحة
# apl-source:8
# # إغلاق بلا فتح يحتاج إضافة فتحة
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
def اضافات(س):
  # apl-source:19
  مفتوح = 0
  # apl-source:20
  ناقص = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      مفتوح = مفتوح + 1
    # apl-source:24
    else:
      # apl-source:25
      if مفتوح > 0:
        # apl-source:26
        مفتوح = مفتوح - 1
      # apl-source:27
      else:
        # apl-source:28
        ناقص = ناقص + 1
  # apl-source:29
  return مفتوح + ناقص
# apl-source:30

# apl-source:31
تأكد_يساوي(اضافات("())"), 1, "إغلاق زائد")
# apl-source:32
تأكد_يساوي(اضافات("((("), 3, "فتحات")
# apl-source:33
تأكد_يساوي(اضافات("()))(("), 4, "مختلط")
# apl-source:34
تأكد_يساوي(اضافات(""), 0, "فارغ")
# apl-source:35
