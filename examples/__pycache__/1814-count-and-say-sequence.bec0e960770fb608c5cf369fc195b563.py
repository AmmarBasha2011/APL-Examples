
# apl-source:1
# مثال 1814 — متتالية عد وقل
# apl-source:2
# Count and say sequence
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1814-count-and-say-sequence.apl
# apl-source:6

# apl-source:7
# نقرأ المجموعات المتتالية
# apl-source:8
# نكتب العدد ثم الرقم
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
def صف(س):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  ك = 0
  # apl-source:21
  while ك < len(س):
    # apl-source:22
    ي = ك
    # apl-source:23
    while ي < len(س) and س[ي] == س[ك]:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    ناتج = ناتج + str(ي - ك) + س[ك]
    # apl-source:26
    ك = ي
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def عد_وقل(ن):
  # apl-source:30
  س = "1"
  # apl-source:31
  for ك in range(ن - 1):
    # apl-source:32
    س = صف(س)
  # apl-source:33
  return س
# apl-source:34

# apl-source:35
تأكد_يساوي(عد_وقل(1), "1", "الأول")
# apl-source:36
تأكد_يساوي(عد_وقل(4), "1211", "الرابع")
# apl-source:37
تأكد_يساوي(عد_وقل(6), "312211", "السادس")
# apl-source:38
