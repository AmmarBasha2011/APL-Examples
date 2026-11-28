
# apl-source:1
# مثال 1183 — فك النص المتداخل
# apl-source:2
# Decode nested repeated string
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1183-decode-string-nested.apl
# apl-source:6

# apl-source:7
# نخزن النص والعدد عند كل قوس فتح
# apl-source:8
# وعند الإغلاق نكرر ونلصق بما قبله
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
  مكدس = []
  # apl-source:20
  حالي = ""
  # apl-source:21
  رقم = 0
  # apl-source:22
  for ح in س:
    # apl-source:23
    if ح.isdigit():
      # apl-source:24
      رقم = رقم * 10 + int(ح)
    # apl-source:25
    elif ح == "[":
      # apl-source:26
      مكدس = مكدس + [[حالي, رقم]]
      # apl-source:27
      حالي = ""
      # apl-source:28
      رقم = 0
    # apl-source:29
    elif ح == "]":
      # apl-source:30
      خ = مكدس.pop()
      # apl-source:31
      حالي = خ[0] + حالي * خ[1]
    # apl-source:32
    else:
      # apl-source:33
      حالي = حالي + ح
  # apl-source:34
  return حالي
# apl-source:35

# apl-source:36
تأكد_يساوي(فك("3[a]2[bc]"), "aaabcbc", "مثال أول")
# apl-source:37
تأكد_يساوي(فك("3[a2[c]]"), "accaccacc", "متداخل")
# apl-source:38
تأكد_يساوي(فك("2[abc]3[cd]ef"), "abcabccdcdcdef", "مع ذيل")
# apl-source:39
تأكد_يساوي(فك("abc"), "abc", "بلا تكرار")
# apl-source:40
تأكد_يساوي(فك("10[x]"), "xxxxxxxxxx", "رقمان")
# apl-source:41
