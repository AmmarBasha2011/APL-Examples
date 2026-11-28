
# apl-source:1
# مثال 4810 — تجميع الكلمات حسب الحرف الأخير (مجموع الأطوال)
# apl-source:2
# Group words by last letter: total length
# apl-source:3
# Demonstrates: قواميس وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4810-group-by-last-total-len.apl
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
      د[ك] = د[ك] + len(خ)
    # apl-source:24
    else:
      # apl-source:25
      د[ك] = len(خ)
  # apl-source:26
  return د
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {"e": 8, "b": 3, "t": 10, "r": 4, "g": 3}, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {"n": 7, "r": 4, "y": 3, "s": 4}, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {"e": 12, "o": 3, "r": 4, "x": 3}, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {"i": 4, "e": 8, "n": 5, "k": 4}, "حالة 4")
# apl-source:32
