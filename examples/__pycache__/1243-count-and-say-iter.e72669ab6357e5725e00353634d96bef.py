
# apl-source:1
# مثال 1243 — عد وقل
# apl-source:2
# Count and say iterative
# apl-source:3
# Demonstrates: تجميع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1243-count-and-say-iter.apl
# apl-source:6

# apl-source:7
# كل حد يصف الحد السابق بعدد التكرار ثم الرقم
# apl-source:8
# نجمع الأرقام المتتالية المتشابهة
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
def تالي(س):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  ع = 0
  # apl-source:21
  while ع < len(س):
    # apl-source:22
    ك = ع
    # apl-source:23
    while (ك < len(س)) and (س[ك] == س[ع]):
      # apl-source:24
      ك = ك + 1
    # apl-source:25
    ناتج = ناتج + str(ك - ع) + س[ع]
    # apl-source:26
    ع = ك
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def الحد(ن):
  # apl-source:30
  س = "1"
  # apl-source:31
  for ع in range(ن - 1):
    # apl-source:32
    س = تالي(س)
  # apl-source:33
  return س
# apl-source:34

# apl-source:35
تأكد_يساوي(الحد(1), "1", "الأول")
# apl-source:36
تأكد_يساوي(الحد(4), "1211", "الرابع")
# apl-source:37
تأكد_يساوي(الحد(5), "111221", "الخامس")
# apl-source:38
تأكد_يساوي(الحد(6), "312211", "السادس")
# apl-source:39
