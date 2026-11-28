
# apl-source:1
# مثال 1539 — تجميع الكلمات حسب الطول
# apl-source:2
# Group words by length
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1539-group-words-by-length.apl
# apl-source:6

# apl-source:7
# الطول هو المفتاح
# apl-source:8
# القيمة قائمة تتسع للكلمات
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
def جمّع_بالطول(كلمات):
  # apl-source:19
  مجموعات = {}
  # apl-source:20
  for ك in كلمات:
    # apl-source:21
    ط = len(ك)
    # apl-source:22
    if ط in مجموعات:
      # apl-source:23
      مجموعات[ط].append(ك)
    # apl-source:24
    else:
      # apl-source:25
      مجموعات[ط] = [ك]
  # apl-source:26
  return مجموعات
# apl-source:27

# apl-source:28
تأكد_يساوي(جمّع_بالطول(["ab", "cd", "e"]), {2: ["ab", "cd"], 1: ["e"]}, "طولان")
# apl-source:29
تأكد_يساوي(جمّع_بالطول([]), {}, "فارغ")
# apl-source:30
