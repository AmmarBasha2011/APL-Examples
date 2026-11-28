
# apl-source:1
# مثال 1615 — عدد الجزر في شبكة
# apl-source:2
# Count islands in a grid
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1615-island-count-grid.apl
# apl-source:6

# apl-source:7
# نبدأ من كل واحد لم نزره
# apl-source:8
# نلون كل الجيران بالبحث
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
def عدد_الجزر(شبكة):
  # apl-source:19
  صفوف = len(شبكة)
  # apl-source:20
  if صفوف == 0:
    # apl-source:21
    return 0
  # apl-source:22
  أعمدة = len(شبكة[0])
  # apl-source:23
  زرنا = {}
  # apl-source:24
  جزر = 0
  # apl-source:25
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:26
  for ص in range(صفوف):
    # apl-source:27
    for ع in range(أعمدة):
      # apl-source:28
      مفتاح = str(ص) + "," + str(ع)
      # apl-source:29
      if شبكة[ص][ع] == 1 and (مفتاح in زرنا) == False:
        # apl-source:30
        جزر = جزر + 1
        # apl-source:31
        مكدس = [[ص, ع]]
        # apl-source:32
        زرنا[مفتاح] = True
        # apl-source:33
        while len(مكدس) > 0:
          # apl-source:34
          ح = مكدس.pop()
          # apl-source:35
          for ات in اتجاهات:
            # apl-source:36
            ن_ص = ح[0] + ات[0]
            # apl-source:37
            ن_ع = ح[1] + ات[1]
            # apl-source:38
            if ن_ص >= 0 and ن_ص < صفوف and ن_ع >= 0 and ن_ع < أعمدة:
              # apl-source:39
              مفتاح2 = str(ن_ص) + "," + str(ن_ع)
              # apl-source:40
              if شبكة[ن_ص][ن_ع] == 1 and (مفتاح2 in زرنا) == False:
                # apl-source:41
                زرنا[مفتاح2] = True
                # apl-source:42
                مكدس.append([ن_ص, ن_ع])
  # apl-source:43
  return جزر
# apl-source:44

# apl-source:45
تأكد_يساوي(عدد_الجزر([[1, 1, 0], [0, 1, 0], [0, 0, 1]]), 2, "جزيرتان")
# apl-source:46
تأكد_يساوي(عدد_الجزر([[0, 0], [0, 0]]), 0, "بحر")
# apl-source:47
تأكد_يساوي(عدد_الجزر([[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 5, "خمس")
# apl-source:48
