
# apl-source:1
# مثال 1020 — أقل مجموع مسار
# apl-source:2
# Minimum path sum
# apl-source:3
# Demonstrates: برمجة ديناميكية على شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1020-min-path-sum.apl
# apl-source:6

# apl-source:7
# كل خانة لها كلفة والحركة يميناً أو أسفل
# apl-source:8
# كلفة الوصول لخانة هي كلفتها مع أقل كلفة وصول لجارتيها
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
def اقل_مسار(شبكة):
  # apl-source:19
  ص = len(شبكة)
  # apl-source:20
  ع = len(شبكة[0])
  # apl-source:21
  د = []
  # apl-source:22
  for ر in range(ص):
    # apl-source:23
    د = د + [[0] * ع]
  # apl-source:24
  for ر in range(ص):
    # apl-source:25
    for ك in range(ع):
      # apl-source:26
      if (ر == 0) and (ك == 0):
        # apl-source:27
        د[ر][ك] = شبكة[ر][ك]
      # apl-source:28
      elif ر == 0:
        # apl-source:29
        د[ر][ك] = شبكة[ر][ك] + د[ر][ك - 1]
      # apl-source:30
      elif ك == 0:
        # apl-source:31
        د[ر][ك] = شبكة[ر][ك] + د[ر - 1][ك]
      # apl-source:32
      else:
        # apl-source:33
        أقل = د[ر - 1][ك]
        # apl-source:34
        if د[ر][ك - 1] < أقل:
          # apl-source:35
          أقل = د[ر][ك - 1]
        # apl-source:36
        د[ر][ك] = شبكة[ر][ك] + أقل
  # apl-source:37
  return د[ص - 1][ع - 1]
# apl-source:38

# apl-source:39
تأكد_يساوي(اقل_مسار([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7, "ثلاثة في ثلاثة")
# apl-source:40
تأكد_يساوي(اقل_مسار([[1, 2, 3], [4, 5, 6]]), 12, "اثنان في ثلاثة")
# apl-source:41
تأكد_يساوي(اقل_مسار([[5]]), 5, "خانة واحدة")
# apl-source:42
