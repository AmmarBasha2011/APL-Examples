
# apl-source:1
# مثال 1915 — أقل تكلفة لإسناد المهام بالبتات
# apl-source:2
# Min cost assignment with bit masks
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1915-bit-dp-min-cost-assignment.apl
# apl-source:6

# apl-source:7
# نسند للعامل ك مهمة غير مستعملة
# apl-source:8
# نختار أقل تكلفة لكل قناع
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
def اسناد(تكلفة):
  # apl-source:19
  ن = len(تكلفة)
  # apl-source:20
  كبير = 1000000
  # apl-source:21
  كل = (1 << ن) - 1
  # apl-source:22
  د = []
  # apl-source:23
  for م in range(كل + 1):
    # apl-source:24
    د = د + [كبير]
  # apl-source:25
  د[0] = 0
  # apl-source:26
  for م in range(كل + 1):
    # apl-source:27
    ع = 0
    # apl-source:28
    for ت in range(ن):
      # apl-source:29
      if (م & (1 << ت)) != 0:
        # apl-source:30
        ع = ع + 1
    # apl-source:31
    if ع < ن and د[م] < كبير:
      # apl-source:32
      for ت in range(ن):
        # apl-source:33
        if (م & (1 << ت)) == 0:
          # apl-source:34
          جديد = د[م] + تكلفة[ع][ت]
          # apl-source:35
          if جديد < د[م | (1 << ت)]:
            # apl-source:36
            د[م | (1 << ت)] = جديد
  # apl-source:37
  return د[كل]
# apl-source:38

# apl-source:39
تأكد_يساوي(اسناد([[9, 2, 7], [6, 4, 3], [5, 8, 1]]), 9, "ثلاثة")
# apl-source:40
تأكد_يساوي(اسناد([[1, 2], [2, 1]]), 2, "اثنان")
# apl-source:41
تأكد_يساوي(اسناد([[5]]), 5, "واحد")
# apl-source:42
