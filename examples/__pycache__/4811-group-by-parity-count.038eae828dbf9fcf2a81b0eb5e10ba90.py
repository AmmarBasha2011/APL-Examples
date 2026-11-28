
# apl-source:1
# مثال 4811 — تجميع الكلمات حسب زوجية الطول (عدد الكلمات)
# apl-source:2
# Group words by length parity: count
# apl-source:3
# Demonstrates: قواميس وتجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4811-group-by-parity-count.apl
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
    ك = len(خ) % 2
    # apl-source:22
    if ك in د:
      # apl-source:23
      د[ك] = د[ك] + 1
    # apl-source:24
    else:
      # apl-source:25
      د[ك] = 1
  # apl-source:26
  return د
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {1: 6, 0: 1}, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {1: 2, 0: 3}, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {1: 4, 0: 2}, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {0: 4, 1: 1}, "حالة 4")
# apl-source:32
