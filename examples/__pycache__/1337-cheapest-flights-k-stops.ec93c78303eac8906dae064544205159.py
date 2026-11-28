
# apl-source:1
# مثال 1337 — أرخص رحلات بتوقفات
# apl-source:2
# Cheapest flights within K stops
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1337-cheapest-flights-k-stops.apl
# apl-source:6

# apl-source:7
# نكرر الاسترخاء عدد التوقفات زائد واحد مرة
# apl-source:8
# نستخدم نسخة من المسافات في كل جولة
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
def ارخص_رحلة(ن, رحلات, من_, الى, ك):
  # apl-source:19
  كبير = 1000000000
  # apl-source:20
  سعر = [كبير] * ن
  # apl-source:21
  سعر[من_] = 0
  # apl-source:22
  for جولة in range(ك + 1):
    # apl-source:23
    جديد = سعر[:]
    # apl-source:24
    for ر in رحلات:
      # apl-source:25
      if سعر[ر[0]] < كبير:
        # apl-source:26
        if سعر[ر[0]] + ر[2] < جديد[ر[1]]:
          # apl-source:27
          جديد[ر[1]] = سعر[ر[0]] + ر[2]
    # apl-source:28
    سعر = جديد
  # apl-source:29
  if سعر[الى] == كبير:
    # apl-source:30
    return -1
  # apl-source:31
  return سعر[الى]
# apl-source:32

# apl-source:33
ر = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# apl-source:34
تأكد_يساوي(ارخص_رحلة(4, ر, 0, 3, 1), 700, "توقف واحد")
# apl-source:35
تأكد_يساوي(ارخص_رحلة(4, ر, 0, 3, 2), 400, "توقفان")
# apl-source:36
تأكد_يساوي(ارخص_رحلة(3, [[0,1,5]], 0, 2, 1), -1, "لا طريق")
# apl-source:37
