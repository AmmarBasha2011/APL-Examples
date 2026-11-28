
# apl-source:1
# مثال 4809 — تجميع الكلمات حسب الحرف الأخير (الكلمات)
# apl-source:2
# Group words by last letter: words
# apl-source:3
# Demonstrates: قواميس وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4809-group-by-last-join.apl
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
    ك = خ[len(خ) - 1]
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
تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {"e": ["apple", "axe"], "b": ["bob"], "t": ["cat", "apricot"], "r": ["bear"], "g": ["dog"]}, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {"n": ["sun", "moon"], "r": ["star"], "y": ["sky"], "s": ["mars"]}, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {"e": ["one", "three", "five"], "o": ["two"], "r": ["four"], "x": ["six"]}, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {"i": ["kiwi"], "e": ["lime", "kale"], "n": ["lemon"], "k": ["leek"]}, "حالة 4")
# apl-source:32
