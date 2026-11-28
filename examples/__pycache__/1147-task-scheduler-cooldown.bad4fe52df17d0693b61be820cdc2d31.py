
# apl-source:1
# مثال 1147 — جدولة مهام
# apl-source:2
# Task scheduler with cooldown
# apl-source:3
# Demonstrates: جشع بعدّ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1147-task-scheduler-cooldown.apl
# apl-source:6

# apl-source:7
# المهمة الأكثر تكراراً تحدد الإطار
# apl-source:8
# ونملأ الفراغات بباقي المهام
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
def وقت_التنفيذ(مهام, تبريد):
  # apl-source:19
  عد = {}
  # apl-source:20
  for م in مهام:
    # apl-source:21
    عد[م] = عد.get(م, 0) + 1
  # apl-source:22
  اقصى = 0
  # apl-source:23
  for ك in عد:
    # apl-source:24
    if عد[ك] > اقصى:
      # apl-source:25
      اقصى = عد[ك]
  # apl-source:26
  كم_اقصى = 0
  # apl-source:27
  for ك in عد:
    # apl-source:28
    if عد[ك] == اقصى:
      # apl-source:29
      كم_اقصى = كم_اقصى + 1
  # apl-source:30
  اطار = (اقصى - 1) * (تبريد + 1) + كم_اقصى
  # apl-source:31
  return max(اطار, len(مهام))
# apl-source:32

# apl-source:33
تأكد_يساوي(وقت_التنفيذ(["A","A","A","B","B","B"], 2), 8, "مثال أول")
# apl-source:34
تأكد_يساوي(وقت_التنفيذ(["A","A","A","B","B","B"], 0), 6, "بلا تبريد")
# apl-source:35
تأكد_يساوي(وقت_التنفيذ(["A","A","A","A","B"], 3), 13, "مهمة مهيمنة")
# apl-source:36
تأكد_يساوي(وقت_التنفيذ(["A","B","C"], 5), 3, "كلها مختلفة")
# apl-source:37
