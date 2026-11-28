
# apl-source:1
# مثال 1963 — لعبة الثيران والأبقار
# apl-source:2
# Bulls and cows score
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1963-bulls-and-cows-score-guess.apl
# apl-source:6

# apl-source:7
# # نعد الثيران أولا بمقارنة المواضع
# apl-source:8
# # ثم الأبقار من الأرقام المشتركة المتبقية
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
def نتيجة(سر, تخمين):
  # apl-source:19
  ثيران = 0
  # apl-source:20
  عد_س = {}
  # apl-source:21
  عد_ت = {}
  # apl-source:22
  for ك in range(len(سر)):
    # apl-source:23
    if سر[ك] == تخمين[ك]:
      # apl-source:24
      ثيران = ثيران + 1
    # apl-source:25
    else:
      # apl-source:26
      عد_س[سر[ك]] = عد_س.get(سر[ك], 0) + 1
      # apl-source:27
      عد_ت[تخمين[ك]] = عد_ت.get(تخمين[ك], 0) + 1
  # apl-source:28
  ابقار = 0
  # apl-source:29
  for م in عد_س:
    # apl-source:30
    ابقار = ابقار + min(عد_س[م], عد_ت.get(م, 0))
  # apl-source:31
  return [ثيران, ابقار]
# apl-source:32

# apl-source:33
تأكد_يساوي(نتيجة("1807", "7810"), [1, 3], "كلاسيكي")
# apl-source:34
تأكد_يساوي(نتيجة("1123", "0111"), [1, 1], "مكرر")
# apl-source:35
تأكد_يساوي(نتيجة("1234", "1234"), [4, 0], "فوز")
# apl-source:36
