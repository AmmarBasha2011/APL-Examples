
# apl-source:1
# مثال 989 — تدفق أدنى كلفة
# apl-source:2
# Min-cost flow
# apl-source:3
# Demonstrates: أقصر مسار متعاقب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/989-min-cost-flow.apl
# apl-source:6

# apl-source:7
# تدفق أدنى كلفة: إرسال وحدتين بأرخص مسارات متاحة
# apl-source:8
# خوارزمية أقصر مسار تعاقبي على الشبكة المتبقية
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
سعة = [[0, 2, 1, 0], [0, 0, 1, 1], [0, 0, 0, 2], [0, 0, 0, 0]]
# apl-source:19
كلفة = [[0, 1, 4, 0], [0, 0, 1, 3], [0, 0, 0, 1], [0, 0, 0, 0]]
# apl-source:20
for ع in range(4):
  # apl-source:21
  for م in range(4):
    # apl-source:22
    كلفة[م][ع] = 0 - كلفة[ع][م]
# apl-source:23

# apl-source:24
تدفق = 0
# apl-source:25
كلفة_كلية = 0
# apl-source:26
هدف = 2
# apl-source:27
while تدفق < هدف:
  # apl-source:28
  مسافات = [999999, 999999, 999999, 999999]
  # apl-source:29
  والد = [-1, -1, -1, -1]
  # apl-source:30
  مسافات[0] = 0
  # apl-source:31
  for جولة in range(4):
    # apl-source:32
    for ع in range(4):
      # apl-source:33
      if مسافات[ع] < 999999:
        # apl-source:34
        for م in range(4):
          # apl-source:35
          if سعة[ع][م] > 0:
            # apl-source:36
            if مسافات[م] > (مسافات[ع] + كلفة[ع][م]):
              # apl-source:37
              مسافات[م] = مسافات[ع] + كلفة[ع][م]
              # apl-source:38
              والد[م] = ع
  # apl-source:39
  if والد[3] == -1:
    # apl-source:40
    تدفق = هدف
  # apl-source:41
  else:
    # apl-source:42
    ف = هدف - تدفق
    # apl-source:43
    عقدة = 3
    # apl-source:44
    while عقدة != 0:
      # apl-source:45
      if سعة[والد[عقدة]][عقدة] < ف:
        # apl-source:46
        ف = سعة[والد[عقدة]][عقدة]
      # apl-source:47
      عقدة = والد[عقدة]
    # apl-source:48
    عقدة = 3
    # apl-source:49
    while عقدة != 0:
      # apl-source:50
      سعة[والد[عقدة]][عقدة] = سعة[والد[عقدة]][عقدة] - ف
      # apl-source:51
      سعة[عقدة][والد[عقدة]] = سعة[عقدة][والد[عقدة]] + ف
      # apl-source:52
      عقدة = والد[عقدة]
    # apl-source:53
    تدفق = تدفق + ف
    # apl-source:54
    كلفة_كلية = كلفة_كلية + (ف * مسافات[3])
# apl-source:55

# apl-source:56
تأكد_يساوي(تدفق, 2, "وحدتان مرسلتان")
# apl-source:57
تأكد_يساوي(كلفة_كلية, 7, "الكلفة الدنيا")
# apl-source:58
