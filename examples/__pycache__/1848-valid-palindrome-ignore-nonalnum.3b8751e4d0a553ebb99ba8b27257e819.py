
# apl-source:1
# مثال 1848 — متناظر مع تجاهل الرموز
# apl-source:2
# Palindrome ignoring non-alphanumeric
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1848-valid-palindrome-ignore-nonalnum.apl
# apl-source:6

# apl-source:7
# مؤشر من كل طرف
# apl-source:8
# نقارن بعد التحويل لحروف صغيرة
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
def متناظر(س):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(س) - 1
  # apl-source:21
  while ي < ج:
    # apl-source:22
    if (س[ي].isalpha() or س[ي].isdigit()) == False:
      # apl-source:23
      ي = ي + 1
    # apl-source:24
    elif (س[ج].isalpha() or س[ج].isdigit()) == False:
      # apl-source:25
      ج = ج - 1
    # apl-source:26
    else:
      # apl-source:27
      if س[ي].lower() != س[ج].lower():
        # apl-source:28
        return False
      # apl-source:29
      ي = ي + 1
      # apl-source:30
      ج = ج - 1
  # apl-source:31
  return True
# apl-source:32

# apl-source:33
تأكد_يساوي(متناظر("A man, a plan, a canal: Panama"), True, "كلاسيكي")
# apl-source:34
تأكد_يساوي(متناظر("race a car"), False, "ليس متناظراً")
# apl-source:35
تأكد_يساوي(متناظر(""), True, "فارغ")
# apl-source:36
