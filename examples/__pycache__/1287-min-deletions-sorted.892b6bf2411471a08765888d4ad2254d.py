
# apl-source:1
# مثال 1287 — أقل حذف للترتيب
# apl-source:2
# Minimum deletions to make sorted
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1287-min-deletions-sorted.apl
# apl-source:6

# apl-source:7
# أقل حذف هو الطول ناقص أطول متتالية متزايدة
# apl-source:8
# نحسب المتتالية ببرمجة ديناميكية
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
def اقل_حذف_ترتيب(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  د = [1] * len(أ)
  # apl-source:22
  for ع in range(len(أ)):
    # apl-source:23
    for ج in range(ع):
      # apl-source:24
      if (أ[ج] <= أ[ع]) and (د[ج] + 1 > د[ع]):
        # apl-source:25
        د[ع] = د[ج] + 1
  # apl-source:26
  اقصى = 0
  # apl-source:27
  for ق in د:
    # apl-source:28
    if ق > اقصى:
      # apl-source:29
      اقصى = ق
  # apl-source:30
  return len(أ) - اقصى
# apl-source:31

# apl-source:32
تأكد_يساوي(اقل_حذف_ترتيب([5,1,2,3,4]), 1, "حذف واحد")
# apl-source:33
تأكد_يساوي(اقل_حذف_ترتيب([5,4,3,2,1]), 4, "معكوسة")
# apl-source:34
تأكد_يساوي(اقل_حذف_ترتيب([1,2,3]), 0, "مرتبة")
# apl-source:35
تأكد_يساوي(اقل_حذف_ترتيب([2,2,1,3]), 1, "متساويات")
# apl-source:36
