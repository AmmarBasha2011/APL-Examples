
# apl-source:1
# مثال 1056 — إيجاد النص الجزئي
# apl-source:2
# Find first occurrence of substring
# apl-source:3
# Demonstrates: نافذة مقارنة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1056-find-substring.apl
# apl-source:6

# apl-source:7
# نمر على كل موضع ممكن ونقارن حرفاً بحرف
# apl-source:8
# ونرجع أول موضع تتطابق عنده الإبرة كلها
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
def اوجد(كومة, ابرة):
  # apl-source:19
  if ابرة == "":
    # apl-source:20
    return 0
  # apl-source:21
  for ع in range((len(كومة) - len(ابرة)) + 1):
    # apl-source:22
    تطابق = True
    # apl-source:23
    for ك in range(len(ابرة)):
      # apl-source:24
      if كومة[ع + ك] != ابرة[ك]:
        # apl-source:25
        تطابق = False
    # apl-source:26
    if تطابق:
      # apl-source:27
      return ع
  # apl-source:28
  return -1
# apl-source:29

# apl-source:30
تأكد_يساوي(اوجد("sadbutsad", "sad"), 0, "في البداية")
# apl-source:31
تأكد_يساوي(اوجد("leetcode", "leeto"), -1, "غير موجودة")
# apl-source:32
تأكد_يساوي(اوجد("hello", "ll"), 2, "في الوسط")
# apl-source:33
تأكد_يساوي(اوجد("abc", ""), 0, "إبرة فارغة")
# apl-source:34
