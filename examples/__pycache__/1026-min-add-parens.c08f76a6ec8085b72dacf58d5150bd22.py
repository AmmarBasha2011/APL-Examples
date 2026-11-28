
# apl-source:1
# مثال 1026 — أقل أقواس للإضافة
# apl-source:2
# Minimum add to make parentheses valid
# apl-source:3
# Demonstrates: عداد رصيد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1026-min-add-parens.apl
# apl-source:6

# apl-source:7
# نعد الأقواس المفتوحة غير المغلقة
# apl-source:8
# كل قوس إغلاق بلا رفيق يحتاج قوس فتح إضافياً
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
def اقل_اضافة(نص_):
  # apl-source:19
  مفتوح = 0
  # apl-source:20
  ناقص = 0
  # apl-source:21
  for ح in نص_:
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
تأكد_يساوي(اقل_اضافة("())"), 1, "إغلاق زائد")
# apl-source:32
تأكد_يساوي(اقل_اضافة("((("), 3, "فتح زائد")
# apl-source:33
تأكد_يساوي(اقل_اضافة("()"), 0, "متوازن")
# apl-source:34
تأكد_يساوي(اقل_اضافة("()))(("), 4, "مختلط")
# apl-source:35
