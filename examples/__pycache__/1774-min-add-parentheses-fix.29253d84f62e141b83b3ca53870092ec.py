
# apl-source:1
# مثال 1774 — أقل أقواس للإصلاح
# apl-source:2
# Minimum parentheses to add for validity
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1774-min-add-parentheses-fix.apl
# apl-source:6

# apl-source:7
# نعد المفتوح المعلق
# apl-source:8
# كل إغلاق بلا فتح يحتاج إضافة
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
def أقل_إضافات(س):
  # apl-source:19
  مفتوح = 0
  # apl-source:20
  إضافات = 0
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
        إضافات = إضافات + 1
  # apl-source:29
  return إضافات + مفتوح
# apl-source:30

# apl-source:31
تأكد_يساوي(أقل_إضافات("())"), 1, "واحد")
# apl-source:32
تأكد_يساوي(أقل_إضافات("((("), 3, "ثلاثة")
# apl-source:33
تأكد_يساوي(أقل_إضافات("()"), 0, "صحيحة")
# apl-source:34
تأكد_يساوي(أقل_إضافات(")("), 2, "معكوسة")
# apl-source:35
