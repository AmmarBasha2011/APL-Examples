
# apl-source:1
# مثال 2073 — ملء مصفوفة حلزونية
# apl-source:2
# Spiral matrix fill
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2073-spiral-matrix-fill-n-by-n.apl
# apl-source:6

# apl-source:7
# # أربع حدود تضيق بعد كل ضلع
# apl-source:8
# # نملأ من الخارج للداخل
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
def حلزون(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    م = م + [[0] * ن]
  # apl-source:22
  اعلى = 0
  # apl-source:23
  اسفل = ن - 1
  # apl-source:24
  يسار = 0
  # apl-source:25
  يمين = ن - 1
  # apl-source:26
  ع = 1
  # apl-source:27
  while اعلى <= اسفل and يسار <= يمين:
    # apl-source:28
    for ك in range(يسار, يمين + 1):
      # apl-source:29
      م[اعلى][ك] = ع
      # apl-source:30
      ع = ع + 1
    # apl-source:31
    اعلى = اعلى + 1
    # apl-source:32
    for ك in range(اعلى, اسفل + 1):
      # apl-source:33
      م[ك][يمين] = ع
      # apl-source:34
      ع = ع + 1
    # apl-source:35
    يمين = يمين - 1
    # apl-source:36
    if اعلى <= اسفل:
      # apl-source:37
      for ك in range(يمين, يسار - 1, -1):
        # apl-source:38
        م[اسفل][ك] = ع
        # apl-source:39
        ع = ع + 1
      # apl-source:40
      اسفل = اسفل - 1
    # apl-source:41
    if يسار <= يمين:
      # apl-source:42
      for ك in range(اسفل, اعلى - 1, -1):
        # apl-source:43
        م[ك][يسار] = ع
        # apl-source:44
        ع = ع + 1
      # apl-source:45
      يسار = يسار + 1
  # apl-source:46
  return م
# apl-source:47

# apl-source:48
تأكد_يساوي(حلزون(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]], "٣")
# apl-source:49
تأكد_يساوي(حلزون(1), [[1]], "١")
# apl-source:50
تأكد_يساوي(حلزون(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]], "٤")
# apl-source:51
