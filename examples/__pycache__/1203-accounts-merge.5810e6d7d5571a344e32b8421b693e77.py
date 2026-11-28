
# apl-source:1
# مثال 1203 — دمج الحسابات
# apl-source:2
# Accounts merge by shared email
# apl-source:3
# Demonstrates: اتحاد وبحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1203-accounts-merge.apl
# apl-source:6

# apl-source:7
# نوحد الحسابات التي تتشارك أي بريد
# apl-source:8
# ثم نجمع بريد كل مجموعة ونرتبه
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
def جذر(اب, س):
  # apl-source:19
  while اب[س] != س:
    # apl-source:20
    اب[س] = اب[اب[س]]
    # apl-source:21
    س = اب[س]
  # apl-source:22
  return س
# apl-source:23

# apl-source:24
def ادمج_حسابات(حسابات):
  # apl-source:25
  اب = list(range(len(حسابات)))
  # apl-source:26
  مالك = {}
  # apl-source:27
  for ع in range(len(حسابات)):
    # apl-source:28
    for بريد in حسابات[ع][1:]:
      # apl-source:29
      if بريد in مالك:
        # apl-source:30
        اب[جذر(اب, ع)] = جذر(اب, مالك[بريد])
      # apl-source:31
      else:
        # apl-source:32
        مالك[بريد] = ع
  # apl-source:33
  مجموعات = {}
  # apl-source:34
  for بريد in مالك:
    # apl-source:35
    ر = جذر(اب, مالك[بريد])
    # apl-source:36
    if ر not in مجموعات:
      # apl-source:37
      مجموعات[ر] = []
    # apl-source:38
    مجموعات[ر] = مجموعات[ر] + [بريد]
  # apl-source:39
  ناتج = []
  # apl-source:40
  for ر in sorted(list(مجموعات)):
    # apl-source:41
    ناتج = ناتج + [[حسابات[ر][0]] + sorted(مجموعات[ر])]
  # apl-source:42
  return ناتج
# apl-source:43

# apl-source:44
ح = [["John","a@x","b@x"],["John","b@x","c@x"],["Mary","m@x"],["John","j@x"]]
# apl-source:45
تأكد_يساوي(ادمج_حسابات(ح), [["John","a@x","b@x","c@x"],["Mary","m@x"],["John","j@x"]], "مثال أول")
# apl-source:46
