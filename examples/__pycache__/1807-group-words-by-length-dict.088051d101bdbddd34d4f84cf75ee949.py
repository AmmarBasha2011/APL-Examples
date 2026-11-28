
# apl-source:1
# مثال 1807 — تجميع الكلمات حسب الطول
# apl-source:2
# Group words by length
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1807-group-words-by-length-dict.apl
# apl-source:6

# apl-source:7
# المفتاح طول الكلمة نصاً
# apl-source:8
# القيمة قائمة الكلمات
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
def جمّع(كلمات):
  # apl-source:19
  مجموعات = {}
  # apl-source:20
  for ك in كلمات:
    # apl-source:21
    م = str(len(ك))
    # apl-source:22
    if (م in مجموعات) == False:
      # apl-source:23
      مجموعات[م] = []
    # apl-source:24
    مجموعات[م].append(ك)
  # apl-source:25
  return مجموعات
# apl-source:26

# apl-source:27
ن = جمّع(["a", "bb", "c", "dd", "eee"])
# apl-source:28
تأكد_يساوي(ن["1"], ["a", "c"], "طول واحد")
# apl-source:29
تأكد_يساوي(ن["2"], ["bb", "dd"], "طول اثنين")
# apl-source:30
تأكد_يساوي(ن["3"], ["eee"], "طول ثلاثة")
# apl-source:31
