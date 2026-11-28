import time
# apl-source:1
# مثال 1922 — وقت انتظار طابور التذاكر
# apl-source:2
# Ticket queue wait time
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1922-ticket-queue-wait-time.apl
# apl-source:6

# apl-source:7
# من يريد أكثر يعود لآخر الطابور
# apl-source:8
# نعد الثواني حتى ينتهي شخص معين
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
def وقت(تذاكر, ك):
  # apl-source:19
  كلي = 0
  # apl-source:20
  for ي in range(len(تذاكر)):
    # apl-source:21
    if ي <= ك:
      # apl-source:22
      كلي = كلي + min(تذاكر[ي], تذاكر[ك])
    # apl-source:23
    else:
      # apl-source:24
      كلي = كلي + min(تذاكر[ي], تذاكر[ك] - 1)
  # apl-source:25
  return كلي
# apl-source:26

# apl-source:27
تأكد_يساوي(وقت([2, 3, 2], 2), 6, "الثالث")
# apl-source:28
تأكد_يساوي(وقت([5, 1, 1, 1], 0), 8, "الأول")
# apl-source:29
تأكد_يساوي(وقت([1], 0), 1, "واحد")
# apl-source:30
