
# apl-source:1
# مثال 1277 — أصغر مدى
# apl-source:2
# Smallest range covering k lists
# apl-source:3
# Demonstrates: نافذة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1277-smallest-range-k-lists.apl
# apl-source:6

# apl-source:7
# ندمج كل الأرقام مع رقم قائمتها
# apl-source:8
# ونطبق نافذة منزلقة تغطي كل القوائم
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
def اصغر_مدى(قوائم):
  # apl-source:19
  ازواج = []
  # apl-source:20
  for ع in range(len(قوائم)):
    # apl-source:21
    for س in قوائم[ع]:
      # apl-source:22
      ازواج = ازواج + [[س, ع]]
  # apl-source:23
  ازواج = sorted(ازواج)
  # apl-source:24
  عد = {}
  # apl-source:25
  يسار = 0
  # apl-source:26
  افضل = [-10 ** 9, 1000000000]
  # apl-source:27
  for يمين in range(len(ازواج)):
    # apl-source:28
    ق = ازواج[يمين][1]
    # apl-source:29
    عد[ق] = عد.get(ق, 0) + 1
    # apl-source:30
    while len(عد) == len(قوائم):
      # apl-source:31
      if ازواج[يمين][0] - ازواج[يسار][0] < افضل[1] - افضل[0]:
        # apl-source:32
        افضل = [ازواج[يسار][0], ازواج[يمين][0]]
      # apl-source:33
      ل = ازواج[يسار][1]
      # apl-source:34
      عد[ل] = عد[ل] - 1
      # apl-source:35
      if عد[ل] == 0:
        # apl-source:36
        عد.pop(ل)
      # apl-source:37
      يسار = يسار + 1
  # apl-source:38
  return افضل
# apl-source:39

# apl-source:40
تأكد_يساوي(اصغر_مدى([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]), [20, 24], "مثال أول")
# apl-source:41
تأكد_يساوي(اصغر_مدى([[1,2,3],[1,2,3],[1,2,3]]), [1, 1], "متطابقة")
# apl-source:42
