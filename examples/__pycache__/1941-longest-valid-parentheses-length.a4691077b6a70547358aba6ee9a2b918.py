
# apl-source:1
# مثال 1941 — أطول قوسين صحيحين متتاليين
# apl-source:2
# Longest valid parentheses run
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1941-longest-valid-parentheses-length.apl
# apl-source:6

# apl-source:7
# نبدأ بالموضع -١ في المكدس
# apl-source:8
# عند إغلاق نحسب الطول من آخر موضع
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
def اطول(س):
  # apl-source:19
  مكدس = [-1]
  # apl-source:20
  افضل = 0
  # apl-source:21
  for ك in range(len(س)):
    # apl-source:22
    if س[ك] == "(":
      # apl-source:23
      مكدس = مكدس + [ك]
    # apl-source:24
    else:
      # apl-source:25
      مكدس.pop()
      # apl-source:26
      if len(مكدس) == 0:
        # apl-source:27
        مكدس = مكدس + [ك]
      # apl-source:28
      else:
        # apl-source:29
        افضل = max(افضل, ك - مكدس[len(مكدس) - 1])
  # apl-source:30
  return افضل
# apl-source:31

# apl-source:32
تأكد_يساوي(اطول("(()"), 2, "ناقص")
# apl-source:33
تأكد_يساوي(اطول(")()())"), 4, "وسط")
# apl-source:34
تأكد_يساوي(اطول(""), 0, "فارغ")
# apl-source:35
