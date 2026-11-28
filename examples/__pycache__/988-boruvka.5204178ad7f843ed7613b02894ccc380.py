
# apl-source:1
# مثال 988 — خوارزمية بوروفكا
# apl-source:2
# Boruvka MST
# apl-source:3
# Demonstrates: دمج مكونات بأرخص حافة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/988-boruvka.apl
# apl-source:6

# apl-source:7
# خوارزمية بوروفكا: شجرة امتداد دنيا بدمج المكونات على جولات
# apl-source:8
# كل مكوّن يختار أرخص حافة خارجة في الجولة الواحدة
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
حواف = [[0, 1, 4], [0, 2, 2], [1, 2, 1], [1, 3, 5], [2, 3, 8], [2, 4, 10]]
# apl-source:19
والد = [0, 1, 2, 3, 4]
# apl-source:20

# apl-source:21
def جذر(س):
  # apl-source:22
  while والد[س] != س:
    # apl-source:23
    والد[س] = والد[والد[س]]
    # apl-source:24
    س = والد[س]
  # apl-source:25
  return س
# apl-source:26

# apl-source:27
مكونات = 5
# apl-source:28
كلفة = 0
# apl-source:29
عدد_مختارة = 0
# apl-source:30
while مكونات > 1:
  # apl-source:31
  أرخص = [999, 999, 999, 999, 999]
  # apl-source:32
  حافة_أرخص = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
  # apl-source:33
  for ح in حواف:
    # apl-source:34
    ج1 = جذر(ح[0])
    # apl-source:35
    ج2 = جذر(ح[1])
    # apl-source:36
    if ج1 != ج2:
      # apl-source:37
      if ح[2] < أرخص[ج1]:
        # apl-source:38
        أرخص[ج1] = ح[2]
        # apl-source:39
        حافة_أرخص[ج1] = ح
      # apl-source:40
      if ح[2] < أرخص[ج2]:
        # apl-source:41
        أرخص[ج2] = ح[2]
        # apl-source:42
        حافة_أرخص[ج2] = ح
  # apl-source:43
  for ج in range(5):
    # apl-source:44
    if أرخص[ج] != 999:
      # apl-source:45
      ح = حافة_أرخص[ج]
      # apl-source:46
      ج1 = جذر(ح[0])
      # apl-source:47
      ج2 = جذر(ح[1])
      # apl-source:48
      if ج1 != ج2:
        # apl-source:49
        والد[ج1] = ج2
        # apl-source:50
        كلفة = كلفة + ح[2]
        # apl-source:51
        عدد_مختارة = عدد_مختارة + 1
        # apl-source:52
        مكونات = مكونات - 1
# apl-source:53

# apl-source:54
تأكد_يساوي(كلفة, 18, "كلفة الشجرة الدنيا")
# apl-source:55
تأكد_يساوي(عدد_مختارة, 4, "أربع حواف")
# apl-source:56
