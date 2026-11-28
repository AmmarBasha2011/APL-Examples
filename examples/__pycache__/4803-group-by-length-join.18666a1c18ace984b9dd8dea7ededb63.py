
# apl-source:1
# مثال 4803 — تجميع الكلمات حسب الطول (الكلمات)
# apl-source:2
# Group words by length: words
# apl-source:3
# Demonstrates: قواميس وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4803-group-by-length-join.apl
# apl-source:6

# apl-source:7
# نمر على الكلمات
# apl-source:8
# ونحدّث القاموس حسب المفتاح
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
def ف(ق):
  # apl-source:19
  د = {}
  # apl-source:20
  for خ in ق:
    # apl-source:21
    ك = len(خ)
    # apl-source:22
    if ك in د:
      # apl-source:23
      د[ك] = د[ك] + [خ]
    # apl-source:24
    else:
      # apl-source:25
      د[ك] = [خ]
  # apl-source:26
  return د
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {5: ["apple"], 3: ["bob", "cat", "dog", "axe"], 7: ["apricot"], 4: ["bear"]}, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {3: ["sun", "sky"], 4: ["moon", "star", "mars"]}, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {3: ["one", "two", "six"], 5: ["three"], 4: ["four", "five"]}, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {4: ["kiwi", "lime", "kale", "leek"], 5: ["lemon"]}, "حالة 4")
# apl-source:32
