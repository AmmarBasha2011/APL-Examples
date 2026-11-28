
# apl-source:1
# مثال 1899 — عدد أسطر التفاف الكلمات
# apl-source:2
# Word wrap line count
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1899-word-wrap-line-count.apl
# apl-source:6

# apl-source:7
# نضيف الكلمة للسطر إن اتسع
# apl-source:8
# وإلا نبدأ سطرا جديدا
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
def اسطر(نص, عرض):
  # apl-source:19
  كلمات = نص.split(" ")
  # apl-source:20
  عد = 1
  # apl-source:21
  طولي = 0
  # apl-source:22
  for ك in كلمات:
    # apl-source:23
    if طولي == 0:
      # apl-source:24
      طولي = len(ك)
    # apl-source:25
    elif طولي + 1 + len(ك) <= عرض:
      # apl-source:26
      طولي = طولي + 1 + len(ك)
    # apl-source:27
    else:
      # apl-source:28
      عد = عد + 1
      # apl-source:29
      طولي = len(ك)
  # apl-source:30
  return عد
# apl-source:31

# apl-source:32
تأكد_يساوي(اسطر("the quick brown fox jumps", 10), 3, "ثلاثة أسطر")
# apl-source:33
تأكد_يساوي(اسطر("a b c", 20), 1, "سطر واحد")
# apl-source:34
تأكد_يساوي(اسطر("aa bb cc", 2), 3, "كلمة لكل سطر")
# apl-source:35
