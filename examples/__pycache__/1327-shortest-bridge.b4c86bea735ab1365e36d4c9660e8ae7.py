
# apl-source:1
# مثال 1327 — أقصر جسر
# apl-source:2
# Shortest bridge between islands
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1327-shortest-bridge.apl
# apl-source:6

# apl-source:7
# نحدد الجزيرة الأولى بالعمق
# apl-source:8
# ثم نتوسع منها بالعرض حتى نلمس الثانية
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
def جسر(ش):
  # apl-source:19
  ن = len(ش)
  # apl-source:20
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:21
  حدود = []
  # apl-source:22
  بداية = []
  # apl-source:23
  for ص in range(ن):
    # apl-source:24
    for ج in range(ن):
      # apl-source:25
      if (ش[ص][ج] == 1) and (len(بداية) == 0):
        # apl-source:26
        بداية = [ص, ج]
  # apl-source:27
  مكدس = [بداية]
  # apl-source:28
  ش[بداية[0]][بداية[1]] = 2
  # apl-source:29
  while len(مكدس) > 0:
    # apl-source:30
    ق = مكدس.pop()
    # apl-source:31
    حدود = حدود + [[ق[0], ق[1], 0]]
    # apl-source:32
    for د in اتجاهات:
      # apl-source:33
      ر = ق[0] + د[0]
      # apl-source:34
      ك = ق[1] + د[1]
      # apl-source:35
      if (ر >= 0) and (ر < ن) and (ك >= 0) and (ك < ن):
        # apl-source:36
        if ش[ر][ك] == 1:
          # apl-source:37
          ش[ر][ك] = 2
          # apl-source:38
          مكدس = مكدس + [[ر, ك]]
  # apl-source:39
  ع = 0
  # apl-source:40
  while ع < len(حدود):
    # apl-source:41
    ص = حدود[ع][0]
    # apl-source:42
    ج = حدود[ع][1]
    # apl-source:43
    خ = حدود[ع][2]
    # apl-source:44
    ع = ع + 1
    # apl-source:45
    for د in اتجاهات:
      # apl-source:46
      ر = ص + د[0]
      # apl-source:47
      ك = ج + د[1]
      # apl-source:48
      if (ر >= 0) and (ر < ن) and (ك >= 0) and (ك < ن):
        # apl-source:49
        if ش[ر][ك] == 1:
          # apl-source:50
          return خ
        # apl-source:51
        if ش[ر][ك] == 0:
          # apl-source:52
          ش[ر][ك] = 2
          # apl-source:53
          حدود = حدود + [[ر, ك, خ + 1]]
  # apl-source:54
  return -1
# apl-source:55

# apl-source:56
تأكد_يساوي(جسر([[0,1],[1,0]]), 1, "خطوة")
# apl-source:57
تأكد_يساوي(جسر([[0,1,0],[0,0,0],[0,0,1]]), 2, "خطوتان")
# apl-source:58
تأكد_يساوي(جسر([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]), 1, "حلقة")
# apl-source:59
