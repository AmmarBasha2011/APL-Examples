
# apl-source:1
# مثال 1430 — حذف الأقواس الخارجية
# apl-source:2
# Remove outermost parentheses
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1430-remove-outer-parentheses.apl
# apl-source:6

# apl-source:7
# نتتبع العمق أثناء المرور
# apl-source:8
# نحتفظ بالقوس إن لم يكن خارجياً
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
def احذف_الخارجية(نص_):
  # apl-source:19
  عمق = 0
  # apl-source:20
  ناتج = ""
  # apl-source:21
  for ح in نص_:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      if عمق > 0:
        # apl-source:24
        ناتج = ناتج + ح
      # apl-source:25
      عمق = عمق + 1
    # apl-source:26
    else:
      # apl-source:27
      عمق = عمق - 1
      # apl-source:28
      if عمق > 0:
        # apl-source:29
        ناتج = ناتج + ح
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(احذف_الخارجية("(()())(())"), "()()()", "مثال أول")
# apl-source:33
تأكد_يساوي(احذف_الخارجية("(()())(())(()(()))"), "()()()()(())", "مثال ثان")
# apl-source:34
تأكد_يساوي(احذف_الخارجية("()()"), "", "بسيط")
# apl-source:35
