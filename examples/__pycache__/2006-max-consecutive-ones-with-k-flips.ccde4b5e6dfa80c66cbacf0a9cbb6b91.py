
# apl-source:1
# مثال 2006 — أطول سلسلة آحاد مع قلب ك أصفار
# apl-source:2
# Max consecutive ones with k flips
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2006-max-consecutive-ones-with-k-flips.apl
# apl-source:6

# apl-source:7
# # نوسع النافذة يمينا ونعد الأصفار
# apl-source:8
# # وإن زادت عن ك ننقص من اليسار
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
def اطول(ق, ك):
  # apl-source:19
  ي = 0
  # apl-source:20
  اصفار = 0
  # apl-source:21
  افضل = 0
  # apl-source:22
  for ل in range(len(ق)):
    # apl-source:23
    if ق[ل] == 0:
      # apl-source:24
      اصفار = اصفار + 1
    # apl-source:25
    while اصفار > ك:
      # apl-source:26
      if ق[ي] == 0:
        # apl-source:27
        اصفار = اصفار - 1
      # apl-source:28
      ي = ي + 1
    # apl-source:29
    افضل = max(افضل, ل - ي + 1)
  # apl-source:30
  return افضل
# apl-source:31

# apl-source:32
تأكد_يساوي(اطول([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6, "ثنتان")
# apl-source:33
تأكد_يساوي(اطول([0, 0, 1, 1], 0), 2, "بلا قلب")
# apl-source:34
تأكد_يساوي(اطول([0, 0, 0], 3), 3, "الكل")
# apl-source:35
