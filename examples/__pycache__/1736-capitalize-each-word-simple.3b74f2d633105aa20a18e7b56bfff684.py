
# apl-source:1
# مثال 1736 — تكبير أول كل كلمة
# apl-source:2
# Capitalize first letter of each word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1736-capitalize-each-word-simple.apl
# apl-source:6

# apl-source:7
# نقسم بالمسافة
# apl-source:8
# نربط الكلمات بعد التكبير
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
def كبّر(س):
  # apl-source:19
  كلمات = س.split(" ")
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ك in كلمات:
    # apl-source:22
    if len(ك) > 0:
      # apl-source:23
      ناتج.append(ك[0].upper() + ك[1:])
    # apl-source:24
    else:
      # apl-source:25
      ناتج.append(ك)
  # apl-source:26
  return " ".join(ناتج)
# apl-source:27

# apl-source:28
تأكد_يساوي(كبّر("hello big world"), "Hello Big World", "ثلاث")
# apl-source:29
تأكد_يساوي(كبّر("a"), "A", "حرف")
# apl-source:30
تأكد_يساوي(كبّر("Ab cd"), "Ab Cd", "بعضها كبير")
# apl-source:31
