
# apl-source:1
# مثال 2135 — تقدير المقاطع بمجموعات العلة
# apl-source:2
# Syllable estimate vowel groups
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2135-syllable-estimate-by-vowel-groups.apl
# apl-source:6

# apl-source:7
# # نمشي على الحروف
# apl-source:8
# # ونعد بداية كل مجموعة
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
def مقاطع(س):
  # apl-source:19
  عدد = 0
  # apl-source:20
  داخل = False
  # apl-source:21
  for ح in س:
    # apl-source:22
    علة = ح in "aeiou"
    # apl-source:23
    if علة and داخل == False:
      # apl-source:24
      عدد = عدد + 1
    # apl-source:25
    داخل = علة
  # apl-source:26
  return عدد
# apl-source:27

# apl-source:28
تأكد_يساوي(مقاطع("banana"), 3, "banana")
# apl-source:29
تأكد_يساوي(مقاطع("queue"), 1, "queue")
# apl-source:30
تأكد_يساوي(مقاطع("education"), 4, "education")
# apl-source:31
تأكد_يساوي(مقاطع("rhythm"), 0, "rhythm")
# apl-source:32
