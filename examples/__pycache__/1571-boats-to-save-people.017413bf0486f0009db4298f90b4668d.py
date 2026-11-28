
# apl-source:1
# مثال 1571 — قوارب الإنقاذ
# apl-source:2
# Boats to save people
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1571-boats-to-save-people.apl
# apl-source:6

# apl-source:7
# نرتب الأوزان
# apl-source:8
# نزاوج الأخف مع الأثقل إن اتسع القارب
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
def عدد_القوارب(أوزان, حد):
  # apl-source:19
  ق = []
  # apl-source:20
  for و in أوزان:
    # apl-source:21
    ق.append(و)
  # apl-source:22
  ق.sort()
  # apl-source:23
  يسار = 0
  # apl-source:24
  يمين = len(ق) - 1
  # apl-source:25
  قوارب = 0
  # apl-source:26
  while يسار <= يمين:
    # apl-source:27
    if ق[يسار] + ق[يمين] <= حد:
      # apl-source:28
      يسار = يسار + 1
    # apl-source:29
    يمين = يمين - 1
    # apl-source:30
    قوارب = قوارب + 1
  # apl-source:31
  return قوارب
# apl-source:32

# apl-source:33
تأكد_يساوي(عدد_القوارب([1, 2], 3), 1, "قارب")
# apl-source:34
تأكد_يساوي(عدد_القوارب([3, 2, 2, 1], 3), 3, "ثلاثة")
# apl-source:35
تأكد_يساوي(عدد_القوارب([3, 5, 3, 4], 5), 4, "كل شخص منفرداً")
# apl-source:36
