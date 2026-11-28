
# apl-source:1
# مثال 1143 — أقواس بنجمة
# apl-source:2
# Valid parentheses with star
# apl-source:3
# Demonstrates: مدى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1143-star-parentheses.apl
# apl-source:6

# apl-source:7
# نتتبع أدنى وأقصى عدد ممكن للأقواس المفتوحة
# apl-source:8
# والنجمة تغيّر المدى
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
def صالح(س):
  # apl-source:19
  ادنى = 0
  # apl-source:20
  اقصى = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      ادنى = ادنى + 1
      # apl-source:24
      اقصى = اقصى + 1
    # apl-source:25
    elif ح == ")":
      # apl-source:26
      ادنى = ادنى - 1
      # apl-source:27
      اقصى = اقصى - 1
    # apl-source:28
    else:
      # apl-source:29
      ادنى = ادنى - 1
      # apl-source:30
      اقصى = اقصى + 1
    # apl-source:31
    if اقصى < 0:
      # apl-source:32
      return False
    # apl-source:33
    if ادنى < 0:
      # apl-source:34
      ادنى = 0
  # apl-source:35
  return ادنى == 0
# apl-source:36

# apl-source:37
تأكد_يساوي(صالح("()"), True, "عادي")
# apl-source:38
تأكد_يساوي(صالح("(*)"), True, "نجمة وسط")
# apl-source:39
تأكد_يساوي(صالح("(*))"), True, "نجمة تفتح")
# apl-source:40
تأكد_يساوي(صالح(")("), False, "معكوس")
# apl-source:41
تأكد_يساوي(صالح("((*"), False, "ناقصة")
# apl-source:42
تأكد_يساوي(صالح(""), True, "فارغة")
# apl-source:43
