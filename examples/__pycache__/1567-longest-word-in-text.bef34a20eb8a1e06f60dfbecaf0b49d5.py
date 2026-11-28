
# apl-source:1
# مثال 1567 — أطول كلمة في نص
# apl-source:2
# Longest word in text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1567-longest-word-in-text.apl
# apl-source:6

# apl-source:7
# نقارن الطول بالأطول حتى الآن
# apl-source:8
# نحتفظ بالأولى عند التعادل
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
def أطول_كلمة(نص_):
  # apl-source:19
  أفضل = ""
  # apl-source:20
  for ك in نص_.split():
    # apl-source:21
    if len(ك) > len(أفضل):
      # apl-source:22
      أفضل = ك
  # apl-source:23
  return أفضل
# apl-source:24

# apl-source:25
تأكد_يساوي(أطول_كلمة("the quick brown fox"), "quick", "أول الأطول")
# apl-source:26
تأكد_يساوي(أطول_كلمة("a bb ccc"), "ccc", "ثلاثة")
# apl-source:27
تأكد_يساوي(أطول_كلمة(""), "", "فارغ")
# apl-source:28
