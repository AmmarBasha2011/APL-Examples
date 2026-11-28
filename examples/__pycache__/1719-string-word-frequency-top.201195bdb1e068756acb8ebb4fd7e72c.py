
# apl-source:1
# مثال 1719 — الكلمة الأكثر تكراراً
# apl-source:2
# Most frequent word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1719-string-word-frequency-top.apl
# apl-source:6

# apl-source:7
# نقسم النص بالمسافات
# apl-source:8
# نحتفظ بأعلى عدد
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
def أكثر_كلمة(س):
  # apl-source:19
  عدد = {}
  # apl-source:20
  for ك in س.split(" "):
    # apl-source:21
    عدد[ك] = عدد.get(ك, 0) + 1
  # apl-source:22
  أفضل = ""
  # apl-source:23
  أعلى = 0
  # apl-source:24
  for ك in س.split(" "):
    # apl-source:25
    if عدد[ك] > أعلى:
      # apl-source:26
      أعلى = عدد[ك]
      # apl-source:27
      أفضل = ك
  # apl-source:28
  return أفضل
# apl-source:29

# apl-source:30
تأكد_يساوي(أكثر_كلمة("a b a c b a"), "a", "الأولى")
# apl-source:31
تأكد_يساوي(أكثر_كلمة("x y"), "x", "تعادل")
# apl-source:32
تأكد_يساوي(أكثر_كلمة("hi"), "hi", "كلمة")
# apl-source:33
