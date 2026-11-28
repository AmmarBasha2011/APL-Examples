
# apl-source:1
# مثال 1256 — طلاء البيوت
# apl-source:2
# Paint house minimum cost
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1256-paint-house.apl
# apl-source:6

# apl-source:7
# نحتفظ بأقل كلفة تنتهي بكل لون
# apl-source:8
# ونختار للبيت التالي أقل كلفة من لونين آخرين
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
def اقل_طلاء(كلف):
  # apl-source:19
  if len(كلف) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  د = list(كلف[0])
  # apl-source:22
  for ع in range(1, len(كلف)):
    # apl-source:23
    جديد = [0, 0, 0]
    # apl-source:24
    for ل in range(3):
      # apl-source:25
      افضل = 1000000000
      # apl-source:26
      for ك in range(3):
        # apl-source:27
        if (ك != ل) and (د[ك] < افضل):
          # apl-source:28
          افضل = د[ك]
      # apl-source:29
      جديد[ل] = كلف[ع][ل] + افضل
    # apl-source:30
    د = جديد
  # apl-source:31
  return min(د[0], min(د[1], د[2]))
# apl-source:32

# apl-source:33
تأكد_يساوي(اقل_طلاء([[17,2,17],[16,16,5],[14,3,19]]), 10, "ثلاثة بيوت")
# apl-source:34
تأكد_يساوي(اقل_طلاء([[7,6,2]]), 2, "بيت")
# apl-source:35
تأكد_يساوي(اقل_طلاء([]), 0, "فارغة")
# apl-source:36
