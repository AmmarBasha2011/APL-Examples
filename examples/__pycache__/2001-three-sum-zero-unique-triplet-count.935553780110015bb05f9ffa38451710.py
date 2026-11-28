
# apl-source:1
# مثال 2001 — عدد الثلاثيات الفريدة مجموعها صفر
# apl-source:2
# Unique zero-sum triplets
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2001-three-sum-zero-unique-triplet-count.apl
# apl-source:6

# apl-source:7
# # نتخطى القيم المكررة لتفادي التكرار
# apl-source:8
# # ونعد الثلاثيات
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
def ثلاثيات(ق):
  # apl-source:19
  ق = sorted(ق)
  # apl-source:20
  عدد = 0
  # apl-source:21
  for ك in range(len(ق)):
    # apl-source:22
    if ك == 0 or ق[ك] != ق[ك - 1]:
      # apl-source:23
      ي = ك + 1
      # apl-source:24
      ل = len(ق) - 1
      # apl-source:25
      while ي < ل:
        # apl-source:26
        م = ق[ك] + ق[ي] + ق[ل]
        # apl-source:27
        if م == 0:
          # apl-source:28
          عدد = عدد + 1
          # apl-source:29
          ي = ي + 1
          # apl-source:30
          ل = ل - 1
          # apl-source:31
          while ي < ل and ق[ي] == ق[ي - 1]:
            # apl-source:32
            ي = ي + 1
          # apl-source:33
          while ي < ل and ق[ل] == ق[ل + 1]:
            # apl-source:34
            ل = ل - 1
        # apl-source:35
        elif م < 0:
          # apl-source:36
          ي = ي + 1
        # apl-source:37
        else:
          # apl-source:38
          ل = ل - 1
  # apl-source:39
  return عدد
# apl-source:40

# apl-source:41
تأكد_يساوي(ثلاثيات([-1, 0, 1, 2, -1, -4]), 2, "ثنتان")
# apl-source:42
تأكد_يساوي(ثلاثيات([0, 0, 0, 0]), 1, "أصفار")
# apl-source:43
تأكد_يساوي(ثلاثيات([1, 2]), 0, "قصيرة")
# apl-source:44
