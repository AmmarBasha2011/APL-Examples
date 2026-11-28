
# apl-source:1
# مثال 1816 — كلمات بحرف أول كبير
# apl-source:2
# Count capitalized words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1816-title-case-length-check.apl
# apl-source:6

# apl-source:7
# نفحص أول حرف
# apl-source:8
# نستخدم isupper
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
def عد_الكبيرة(س):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ك in س.split(" "):
    # apl-source:21
    if len(ك) > 0:
      # apl-source:22
      if ك[0].isupper():
        # apl-source:23
        عد = عد + 1
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
تأكد_يساوي(عد_الكبيرة("Hello big World"), 2, "كلمتان")
# apl-source:27
تأكد_يساوي(عد_الكبيرة("all small"), 0, "صغيرة")
# apl-source:28
تأكد_يساوي(عد_الكبيرة("A B C"), 3, "ثلاث")
# apl-source:29
