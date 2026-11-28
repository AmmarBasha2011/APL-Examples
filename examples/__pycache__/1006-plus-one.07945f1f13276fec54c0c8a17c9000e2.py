
# apl-source:1
# مثال 1006 — زائد واحد
# apl-source:2
# Plus one on digits
# apl-source:3
# Demonstrates: حمل يمتد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1006-plus-one.apl
# apl-source:6

# apl-source:7
# العدد مخزن أرقاماً في قائمة
# apl-source:8
# الحمل يمتد من اليمين وقد يضيف خانة جديدة
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
def زائد_واحد(أرقام):
  # apl-source:19
  for ع in range(len(أرقام) - 1, -1, -1):
    # apl-source:20
    if أرقام[ع] < 9:
      # apl-source:21
      أرقام[ع] = أرقام[ع] + 1
      # apl-source:22
      return أرقام
    # apl-source:23
    أرقام[ع] = 0
  # apl-source:24
  return [1] + أرقام
# apl-source:25

# apl-source:26
تأكد_يساوي(زائد_واحد([1, 2, 3]), [1, 2, 4], "بلا حمل")
# apl-source:27
تأكد_يساوي(زائد_واحد([1, 2, 9]), [1, 3, 0], "حمل واحد")
# apl-source:28
تأكد_يساوي(زائد_واحد([9, 9]), [1, 0, 0], "خانة جديدة")
# apl-source:29
