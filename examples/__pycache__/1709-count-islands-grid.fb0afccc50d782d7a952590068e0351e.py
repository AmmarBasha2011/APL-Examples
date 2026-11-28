
# apl-source:1
# مثال 1709 — عدد الجزر في الشبكة
# apl-source:2
# Count islands in a grid
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1709-count-islands-grid.apl
# apl-source:6

# apl-source:7
# نمر على الخلايا
# apl-source:8
# نغمر كل جزيرة بعد عدها
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
def اغمر(شبكة, ص0, س0):
  # apl-source:19
  مكدس = [[ص0, س0]]
  # apl-source:20
  شبكة[ص0][س0] = 0
  # apl-source:21
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:22
  while len(مكدس) > 0:
    # apl-source:23
    ح = مكدس.pop()
    # apl-source:24
    for ا in اتجاهات:
      # apl-source:25
      ي = ح[0] + ا[0]
      # apl-source:26
      ك = ح[1] + ا[1]
      # apl-source:27
      if ي >= 0 and ي < len(شبكة) and ك >= 0 and ك < len(شبكة[0]):
        # apl-source:28
        if شبكة[ي][ك] == 1:
          # apl-source:29
          شبكة[ي][ك] = 0
          # apl-source:30
          مكدس.append([ي, ك])
# apl-source:31

# apl-source:32
def عد_الجزر(شبكة):
  # apl-source:33
  عد = 0
  # apl-source:34
  for ي in range(len(شبكة)):
    # apl-source:35
    for ك in range(len(شبكة[0])):
      # apl-source:36
      if شبكة[ي][ك] == 1:
        # apl-source:37
        عد = عد + 1
        # apl-source:38
        اغمر(شبكة, ي, ك)
  # apl-source:39
  return عد
# apl-source:40

# apl-source:41
تأكد_يساوي(عد_الجزر([[1, 1, 0], [0, 0, 1], [1, 0, 1]]), 3, "ثلاث")
# apl-source:42
تأكد_يساوي(عد_الجزر([[0, 0], [0, 0]]), 0, "بحر")
# apl-source:43
تأكد_يساوي(عد_الجزر([[1, 1], [1, 1]]), 1, "واحدة")
# apl-source:44
