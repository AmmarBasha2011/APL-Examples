
# apl-source:1
# مثال 1739 — جدولة المهام بأقرب موعد
# apl-source:2
# Earliest deadline first lateness
# apl-source:3
# Demonstrates: جدولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1739-job-scheduling-earliest-deadline.apl
# apl-source:6

# apl-source:7
# كل مهمة مدة وموعد
# apl-source:8
# نجمع الزمن ونقارنه بالموعد
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
def أقصى_تأخير(مهام):
  # apl-source:19
  م = []
  # apl-source:20
  for ع in مهام:
    # apl-source:21
    م.append([ع[1], ع[0]])
  # apl-source:22
  م.sort()
  # apl-source:23
  زمن = 0
  # apl-source:24
  أقصى = 0
  # apl-source:25
  for ع in م:
    # apl-source:26
    زمن = زمن + ع[1]
    # apl-source:27
    if زمن - ع[0] > أقصى:
      # apl-source:28
      أقصى = زمن - ع[0]
  # apl-source:29
  return أقصى
# apl-source:30

# apl-source:31
تأكد_يساوي(أقصى_تأخير([[3, 6], [2, 4], [1, 2]]), 0, "بلا تأخير")
# apl-source:32
تأكد_يساوي(أقصى_تأخير([[4, 3], [4, 3]]), 5, "تأخير")
# apl-source:33
تأكد_يساوي(أقصى_تأخير([]), 0, "فارغة")
# apl-source:34
