
# apl-source:1
# مثال 1591 — هل الكلمتان تبديل
# apl-source:2
# Valid anagram by counts
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1591-valid-anagram-counts.apl
# apl-source:6

# apl-source:7
# نعد حروف الأولى
# apl-source:8
# ننقص بحروف الثانية وننظر إن بقي شيء
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
def تبديل(أ, ب):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  عد = {}
  # apl-source:22
  for ح in أ:
    # apl-source:23
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:24
  for ح in ب:
    # apl-source:25
    عد[ح] = عد.get(ح, 0) - 1
    # apl-source:26
    if عد[ح] < 0:
      # apl-source:27
      return False
  # apl-source:28
  return True
# apl-source:29

# apl-source:30
تأكد_يساوي(تبديل("listen", "silent"), True, "تبديل")
# apl-source:31
تأكد_يساوي(تبديل("rat", "car"), False, "ليس تبديلاً")
# apl-source:32
تأكد_يساوي(تبديل("aab", "abb"), False, "تكرار مختلف")
# apl-source:33
