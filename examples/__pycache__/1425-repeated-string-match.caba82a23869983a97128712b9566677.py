
# apl-source:1
# مثال 1425 — تكرار نص للمطابقة
# apl-source:2
# Repeated string match
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1425-repeated-string-match.apl
# apl-source:6

# apl-source:7
# نكرر حتى يصبح الطول كافياً
# apl-source:8
# ونجرب تكراراً إضافياً واحداً
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
def اقل_تكرار(أ, ب):
  # apl-source:19
  ممتد = أ
  # apl-source:20
  عدد = 1
  # apl-source:21
  while len(ممتد) < len(ب):
    # apl-source:22
    ممتد = ممتد + أ
    # apl-source:23
    عدد = عدد + 1
  # apl-source:24
  if ب in ممتد:
    # apl-source:25
    return عدد
  # apl-source:26
  ممتد = ممتد + أ
  # apl-source:27
  if ب in ممتد:
    # apl-source:28
    return عدد + 1
  # apl-source:29
  return -1
# apl-source:30

# apl-source:31
تأكد_يساوي(اقل_تكرار("abcd", "cdabcdab"), 3, "ثلاث")
# apl-source:32
تأكد_يساوي(اقل_تكرار("a", "aa"), 2, "اثنتان")
# apl-source:33
تأكد_يساوي(اقل_تكرار("abc", "wxyz"), -1, "مستحيل")
# apl-source:34
