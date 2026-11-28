
# apl-source:1
# مثال 1276 — دمج تدفقات
# apl-source:2
# Merge k sorted lists
# apl-source:3
# Demonstrates: دمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1276-merge-sorted-streams.apl
# apl-source:6

# apl-source:7
# نأخذ الأصغر من رؤوس القوائم في كل خطوة
# apl-source:8
# حتى تنفد كلها
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
def ادمج_كل(قوائم):
  # apl-source:19
  مؤشرات = [0] * len(قوائم)
  # apl-source:20
  ناتج = []
  # apl-source:21
  while True:
    # apl-source:22
    افضل = -1
    # apl-source:23
    for ع in range(len(قوائم)):
      # apl-source:24
      if مؤشرات[ع] < len(قوائم[ع]):
        # apl-source:25
        if (افضل == -1) or (قوائم[ع][مؤشرات[ع]] < قوائم[افضل][مؤشرات[افضل]]):
          # apl-source:26
          افضل = ع
    # apl-source:27
    if افضل == -1:
      # apl-source:28
      return ناتج
    # apl-source:29
    ناتج = ناتج + [قوائم[افضل][مؤشرات[افضل]]]
    # apl-source:30
    مؤشرات[افضل] = مؤشرات[افضل] + 1
# apl-source:31

# apl-source:32
تأكد_يساوي(ادمج_كل([[1,4,5],[1,3,4],[2,6]]), [1,1,2,3,4,4,5,6], "ثلاث قوائم")
# apl-source:33
تأكد_يساوي(ادمج_كل([]), [], "لا قوائم")
# apl-source:34
تأكد_يساوي(ادمج_كل([[], [1]]), [1], "فارغة وواحدة")
# apl-source:35
