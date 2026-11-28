
# apl-source:1
# مثال 1060 — طرق المجموع المستهدف
# apl-source:2
# Target sum with plus and minus signs
# apl-source:3
# Demonstrates: عد المجموعات الجزئية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1060-target-sum-ways.apl
# apl-source:6

# apl-source:7
# إشارات موجبة للمجموعة س وسالبة للباقي تعطي الهدف
# apl-source:8
# فالمسألة عد المجموعات الجزئية التي مجموعها (الكل + الهدف) / 2
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
def طرق_الهدف(ق, هدف):
  # apl-source:19
  كلي = 0
  # apl-source:20
  for س in ق:
    # apl-source:21
    كلي = كلي + س
  # apl-source:22
  if ((كلي + هدف) < 0) or (((كلي + هدف) % 2) != 0):
    # apl-source:23
    return 0
  # apl-source:24
  حد_جزئي = (كلي + هدف) // 2
  # apl-source:25
  ط = [0] * (حد_جزئي + 1)
  # apl-source:26
  ط[0] = 1
  # apl-source:27
  for س in ق:
    # apl-source:28
    for م in range(حد_جزئي, س - 1, -1):
      # apl-source:29
      ط[م] = ط[م] + ط[م - س]
  # apl-source:30
  return ط[حد_جزئي]
# apl-source:31

# apl-source:32
تأكد_يساوي(طرق_الهدف([1, 1, 1, 1, 1], 3), 5, "خمس طرق")
# apl-source:33
تأكد_يساوي(طرق_الهدف([1], 1), 1, "طريقة")
# apl-source:34
تأكد_يساوي(طرق_الهدف([1], 2), 0, "مستحيل")
# apl-source:35
تأكد_يساوي(طرق_الهدف([1, 2, 3], 0), 2, "ثلاثة")
# apl-source:36
