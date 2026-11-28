
# apl-source:1
# مثال 2036 — عد النص الفرعي مع التداخل
# apl-source:2
# Overlapping substring count
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2036-substring-count-overlapping-matches.apl
# apl-source:6

# apl-source:7
# # count العادية لا تعد المتداخلة
# apl-source:8
# # لذلك نقارن عند كل موضع
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
def عد(س, ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  for ك in range(len(س) - len(ن) + 1):
    # apl-source:21
    if س[ك:ك + len(ن)] == ن:
      # apl-source:22
      عدد = عدد + 1
  # apl-source:23
  return عدد
# apl-source:24

# apl-source:25
تأكد_يساوي(عد("aaaa", "aa"), 3, "aa")
# apl-source:26
تأكد_يساوي(عد("abababa", "aba"), 3, "aba")
# apl-source:27
تأكد_يساوي(عد("abc", "d"), 0, "غائب")
# apl-source:28
