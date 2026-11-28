
# apl-source:1
# مثال 1448 — نظرية بيك
# apl-source:2
# Interior lattice points by Pick theorem
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1448-pick-theorem-interior.apl
# apl-source:6

# apl-source:7
# نحسب ضعف المساحة بصيغة الحذاء
# apl-source:8
# ثم نحسب نقاط الحدود بالقاسم المشترك
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
def قاسم(أ, ب):
  # apl-source:19
  if أ < 0:
    # apl-source:20
    أ = -أ
  # apl-source:21
  if ب < 0:
    # apl-source:22
    ب = -ب
  # apl-source:23
  while ب != 0:
    # apl-source:24
    ت = أ % ب
    # apl-source:25
    أ = ب
    # apl-source:26
    ب = ت
  # apl-source:27
  return أ
# apl-source:28

# apl-source:29
def نقاط_داخلية(نقاط):
  # apl-source:30
  ن = len(نقاط)
  # apl-source:31
  ضعف_المساحة = 0
  # apl-source:32
  حدود = 0
  # apl-source:33
  for ع in range(ن):
    # apl-source:34
    أ = نقاط[ع]
    # apl-source:35
    ب = نقاط[(ع + 1) % ن]
    # apl-source:36
    ضعف_المساحة = ضعف_المساحة + أ[0] * ب[1] - ب[0] * أ[1]
    # apl-source:37
    حدود = حدود + قاسم(ب[0] - أ[0], ب[1] - أ[1])
  # apl-source:38
  if ضعف_المساحة < 0:
    # apl-source:39
    ضعف_المساحة = -ضعف_المساحة
  # apl-source:40
  return (ضعف_المساحة - حدود + 2) // 2
# apl-source:41

# apl-source:42
تأكد_يساوي(نقاط_داخلية([[0,0],[4,0],[4,4],[0,4]]), 9, "مربع")
# apl-source:43
تأكد_يساوي(نقاط_داخلية([[0,0],[4,0],[0,4]]), 3, "مثلث")
# apl-source:44
تأكد_يساوي(نقاط_داخلية([[0,0],[1,0],[1,1],[0,1]]), 0, "مربع صغير")
# apl-source:45
