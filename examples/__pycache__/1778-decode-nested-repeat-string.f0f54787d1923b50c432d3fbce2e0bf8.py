
# apl-source:1
# مثال 1778 — فك التكرار المتداخل
# apl-source:2
# Decode nested repeat string
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1778-decode-nested-repeat-string.apl
# apl-source:6

# apl-source:7
# مكدس للنصوص والأعداد
# apl-source:8
# نكرر عند القوس المغلق
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
def فك(س):
  # apl-source:19
  نصوص = []
  # apl-source:20
  أعداد = []
  # apl-source:21
  حالي = ""
  # apl-source:22
  عدد = 0
  # apl-source:23
  for ح in س:
    # apl-source:24
    if ح.isdigit():
      # apl-source:25
      عدد = عدد * 10 + int(ح)
    # apl-source:26
    elif ح == "[":
      # apl-source:27
      نصوص.append(حالي)
      # apl-source:28
      أعداد.append(عدد)
      # apl-source:29
      حالي = ""
      # apl-source:30
      عدد = 0
    # apl-source:31
    elif ح == "]":
      # apl-source:32
      سابق = نصوص.pop()
      # apl-source:33
      حالي = سابق + حالي * أعداد.pop()
    # apl-source:34
    else:
      # apl-source:35
      حالي = حالي + ح
  # apl-source:36
  return حالي
# apl-source:37

# apl-source:38
تأكد_يساوي(فك("3[a]2[bc]"), "aaabcbc", "بسيط")
# apl-source:39
تأكد_يساوي(فك("2[a2[b]]"), "abbabb", "متداخل")
# apl-source:40
تأكد_يساوي(فك("abc"), "abc", "بلا تكرار")
# apl-source:41
