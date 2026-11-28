import time
# apl-source:1
# مثال 1740 — زمن إنهاء المهام بالتناوب
# apl-source:2
# Round robin completion times
# apl-source:3
# Demonstrates: جدولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1740-round-robin-turnaround-time.apl
# apl-source:6

# apl-source:7
# نكرر على المهام بحصة ثابتة
# apl-source:8
# نسجل زمن انتهاء كل مهمة
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
def تناوب(مهام, حصة):
  # apl-source:19
  باقي = مهام + []
  # apl-source:20
  انتهاء = []
  # apl-source:21
  for ك in range(len(مهام)):
    # apl-source:22
    انتهاء.append(0)
  # apl-source:23
  زمن = 0
  # apl-source:24
  متبقي = len(مهام)
  # apl-source:25
  while متبقي > 0:
    # apl-source:26
    for ك in range(len(باقي)):
      # apl-source:27
      if باقي[ك] > 0:
        # apl-source:28
        خطوة = min(حصة, باقي[ك])
        # apl-source:29
        زمن = زمن + خطوة
        # apl-source:30
        باقي[ك] = باقي[ك] - خطوة
        # apl-source:31
        if باقي[ك] == 0:
          # apl-source:32
          انتهاء[ك] = زمن
          # apl-source:33
          متبقي = متبقي - 1
  # apl-source:34
  return انتهاء
# apl-source:35

# apl-source:36
تأكد_يساوي(تناوب([5, 3, 1], 2), [9, 8, 5], "ثلاث مهام")
# apl-source:37
تأكد_يساوي(تناوب([4], 4), [4], "مهمة")
# apl-source:38
