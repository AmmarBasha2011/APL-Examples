
# apl-source:1
# مثال 1132 — ثيران وأبقار
# apl-source:2
# Bulls and cows
# apl-source:3
# Demonstrates: عد تطابق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1132-bulls-and-cows.apl
# apl-source:6

# apl-source:7
# الثور رقم في مكانه الصحيح
# apl-source:8
# والبقرة رقم صحيح في مكان خاطئ
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
def قيم(سر, تخمين):
  # apl-source:19
  ثيران = 0
  # apl-source:20
  عد_سر = [0] * 10
  # apl-source:21
  عد_تخ = [0] * 10
  # apl-source:22
  for ع in range(len(سر)):
    # apl-source:23
    if سر[ع] == تخمين[ع]:
      # apl-source:24
      ثيران = ثيران + 1
    # apl-source:25
    else:
      # apl-source:26
      عد_سر[int(سر[ع])] = عد_سر[int(سر[ع])] + 1
      # apl-source:27
      عد_تخ[int(تخمين[ع])] = عد_تخ[int(تخمين[ع])] + 1
  # apl-source:28
  ابقار = 0
  # apl-source:29
  for ر in range(10):
    # apl-source:30
    ابقار = ابقار + min(عد_سر[ر], عد_تخ[ر])
  # apl-source:31
  return [ثيران, ابقار]
# apl-source:32

# apl-source:33
تأكد_يساوي(قيم("1807", "7810"), [1, 3], "مثال أول")
# apl-source:34
تأكد_يساوي(قيم("1123", "0111"), [1, 1], "تكرار")
# apl-source:35
تأكد_يساوي(قيم("1234", "1234"), [4, 0], "تطابق كامل")
# apl-source:36
تأكد_يساوي(قيم("1234", "5678"), [0, 0], "لا تطابق")
# apl-source:37
