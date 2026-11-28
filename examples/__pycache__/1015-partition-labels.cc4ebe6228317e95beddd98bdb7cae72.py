
# apl-source:1
# مثال 1015 — تقسيم الحروف
# apl-source:2
# Partition labels
# apl-source:3
# Demonstrates: آخر ظهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1015-partition-labels.apl
# apl-source:6

# apl-source:7
# نسجل آخر ظهور لكل حرف
# apl-source:8
# نغلق الجزء عندما يبلغ الفهرس أبعد آخر ظهور في الجزء
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
def اجزاء(نص_):
  # apl-source:19
  اطوال = []
  # apl-source:20
  بداية = 0
  # apl-source:21
  نهاية = 0
  # apl-source:22
  for ع in range(len(نص_)):
    # apl-source:23
    اخر = ع
    # apl-source:24
    for ك in range(ع, len(نص_)):
      # apl-source:25
      if نص_[ك] == نص_[ع]:
        # apl-source:26
        اخر = ك
    # apl-source:27
    if اخر > نهاية:
      # apl-source:28
      نهاية = اخر
    # apl-source:29
    if ع == نهاية:
      # apl-source:30
      اطوال = اطوال + [(ع - بداية) + 1]
      # apl-source:31
      بداية = ع + 1
      # apl-source:32
      نهاية = ع + 1
  # apl-source:33
  return اطوال
# apl-source:34

# apl-source:35
تأكد_يساوي(اجزاء("ababcbacadefegdehijhklij"), [9, 7, 8], "المثال الكلاسيكي")
# apl-source:36
تأكد_يساوي(اجزاء("eccbbbbdec"), [10], "جزء واحد")
# apl-source:37
تأكد_يساوي(اجزاء("abc"), [1, 1, 1], "كل حرف جزء")
# apl-source:38
