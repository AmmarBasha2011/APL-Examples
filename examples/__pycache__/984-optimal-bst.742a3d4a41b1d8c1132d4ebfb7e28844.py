
# apl-source:1
# مثال 984 — شجرة البحث المثلى
# apl-source:2
# Optimal BST
# apl-source:3
# Demonstrates: ديناميكية على كل مدى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/984-optimal-bst.apl
# apl-source:6

# apl-source:7
# شجرة البحث المثلى: أدنى كلفة بحث متوقعة بتكرارات الوصول
# apl-source:8
# برمجة ديناميكية على كل المدى الفرعي
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
def أدنى_كلفة(تكرارات):
  # apl-source:19
  ن = len(تكرارات)
  # apl-source:20
  كلفة = []
  # apl-source:21
  for i in range(ن):
    # apl-source:22
    صف = []
    # apl-source:23
    for j in range(ن):
      # apl-source:24
      صف = صف + [0]
    # apl-source:25
    كلفة = كلفة + [صف]
  # apl-source:26
  for i in range(ن):
    # apl-source:27
    كلفة[i][i] = تكرارات[i]
  # apl-source:28
  for مدى in range(2, ن + 1):
    # apl-source:29
    for i in range(0, (ن - مدى) + 1):
      # apl-source:30
      j = (i + مدى) - 1
      # apl-source:31
      مجموع = 0
      # apl-source:32
      for ف in range(i, j + 1):
        # apl-source:33
        مجموع = مجموع + تكرارات[ف]
      # apl-source:34
      أفضل = -1
      # apl-source:35
      for ك in range(i, j + 1):
        # apl-source:36
        يسار = 0
        # apl-source:37
        if ك > i:
          # apl-source:38
          يسار = كلفة[i][ك - 1]
        # apl-source:39
        يمين = 0
        # apl-source:40
        if ك < j:
          # apl-source:41
          يمين = كلفة[ك + 1][j]
        # apl-source:42
        if (أفضل == -1) or ((يسار + يمين) < أفضل):
          # apl-source:43
          أفضل = يسار + يمين
      # apl-source:44
      كلفة[i][j] = أفضل + مجموع
  # apl-source:45
  return كلفة[0][ن - 1]
# apl-source:46

# apl-source:47
تأكد_يساوي(أدنى_كلفة([34, 8, 50]), 142, "مثال كلاسيكي")
# apl-source:48
تأكد_يساوي(أدنى_كلفة([10, 12, 20]), 72, "تكرارات ثلاثة")
# apl-source:49
تأكد_يساوي(أدنى_كلفة([5, 6]), 16, "مفتاحان")
# apl-source:50
