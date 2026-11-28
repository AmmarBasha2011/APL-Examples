
# apl-source:1
# مثال 1661 — أولي متناظر
# apl-source:2
# Palindromic prime check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1661-palindromic-prime-check.apl
# apl-source:6

# apl-source:7
# نختبر التناظر بقلب النص
# apl-source:8
# ثم نختبر الأولية بالقسمة
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
def أولي_متناظر(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  ن_نص = str(ن)
  # apl-source:22
  معكوس_نص = ""
  # apl-source:23
  for ح in ن_نص:
    # apl-source:24
    معكوس_نص = ح + معكوس_نص
  # apl-source:25
  if معكوس_نص != ن_نص:
    # apl-source:26
    return False
  # apl-source:27
  ك = 2
  # apl-source:28
  while ك * ك <= ن:
    # apl-source:29
    if ن % ك == 0:
      # apl-source:30
      return False
    # apl-source:31
    ك = ك + 1
  # apl-source:32
  return True
# apl-source:33

# apl-source:34
تأكد_يساوي(أولي_متناظر(131), True, "131")
# apl-source:35
تأكد_يساوي(أولي_متناظر(121), False, "121 ليس أولياً")
# apl-source:36
تأكد_يساوي(أولي_متناظر(13), False, "ليس متناظراً")
# apl-source:37
تأكد_يساوي(أولي_متناظر(2), True, "اثنان")
# apl-source:38
