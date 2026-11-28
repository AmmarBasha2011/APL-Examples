
# apl-source:1
# مثال 1439 — مربع صالح
# apl-source:2
# Valid square from four points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1439-valid-square-points.apl
# apl-source:6

# apl-source:7
# نحسب مربعات المسافات الست
# apl-source:8
# أربع متساوية وموجبة واثنتان ضعفها
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
def مربع_صالح(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for ي in range(4):
    # apl-source:21
    for ك in range(ي + 1, 4):
      # apl-source:22
      فس = ن[ي][0] - ن[ك][0]
      # apl-source:23
      فص = ن[ي][1] - ن[ك][1]
      # apl-source:24
      م = م + [فس * فس + فص * فص]
  # apl-source:25
  م = sorted(م)
  # apl-source:26
  return (م[0] > 0) and (م[0] == م[3]) and (م[4] == م[5]) and (م[4] == 2 * م[0])
# apl-source:27

# apl-source:28
تأكد_يساوي(مربع_صالح([[0,0],[1,1],[1,0],[0,1]]), True, "مربع")
# apl-source:29
تأكد_يساوي(مربع_صالح([[0,0],[1,1],[1,0],[0,12]]), False, "ليس مربعاً")
# apl-source:30
تأكد_يساوي(مربع_صالح([[1,0],[-1,0],[0,1],[0,-1]]), True, "مائل")
# apl-source:31
