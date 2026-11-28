
# apl-source:1
# مثال 2143 — عدد النصوص الفرعية المختلفة
# apl-source:2
# Distinct substrings count
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2143-count-distinct-substrings-small-string.apl
# apl-source:6

# apl-source:7
# # نجرب كل بداية ونهاية
# apl-source:8
# # للنصوص القصيرة فقط
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
def مختلفة(س):
  # apl-source:19
  م = {}
  # apl-source:20
  for ا in range(len(س)):
    # apl-source:21
    for ب in range(ا + 1, len(س) + 1):
      # apl-source:22
      م[س[ا:ب]] = 1
  # apl-source:23
  return len(م)
# apl-source:24

# apl-source:25
تأكد_يساوي(مختلفة("abc"), 6, "abc")
# apl-source:26
تأكد_يساوي(مختلفة("aaa"), 3, "aaa")
# apl-source:27
تأكد_يساوي(مختلفة("abab"), 7, "abab")
# apl-source:28
