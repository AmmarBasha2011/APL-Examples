
# apl-source:1
# مثال 874 — مسيرة جارفيس
# apl-source:2
# Jarvis march
# apl-source:3
# Demonstrates: تغليف الهدية بالالتفاف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/874-jarvis-march.apl
# apl-source:6

# apl-source:7
# مسيرة جارفيس (تغليف الهدية): غلاف محدب بالالتفاف حول أقصى نقطة
# apl-source:8
# أبطأ من مسح غراهام نظرياً لكنه أبسط ومناسب للأغلفة الصغيرة
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
def جداء_متقاطع(مبدا, أول, ثان):
  # apl-source:19
  return (أول[0] - مبدا[0]) * (ثان[1] - مبدا[1]) - (أول[1] - مبدا[1]) * (ثان[0] - مبدا[0])
# apl-source:20

# apl-source:21
def جارفيس(نقاط):
  # apl-source:22
  # أدنى نقطة (ص ثم س)
  # apl-source:23
  بداية = نقاط[0]
  # apl-source:24
  for ن in نقاط:
    # apl-source:25
    if ن[1] < بداية[1] or (ن[1] == بداية[1] and ن[0] < بداية[0]):
      # apl-source:26
      بداية = ن
  # apl-source:27
  غلاف = [بداية]
  # apl-source:28
  حالية = بداية
  # apl-source:29
  while 1 == 1:
    # apl-source:30
    تالية = نقاط[0]
    # apl-source:31
    if تالية == حالية:
      # apl-source:32
      تالية = نقاط[1]
    # apl-source:33
    for ن in نقاط:
      # apl-source:34
      if جداء_متقاطع(حالية, تالية, ن) < 0:
        # apl-source:35
        تالية = ن
    # apl-source:36
    حالية = تالية
    # apl-source:37
    if حالية == بداية:
      # apl-source:38
      return غلاف
    # apl-source:39
    غلاف = غلاف + [حالية]
# apl-source:40

# apl-source:41
نقاط = [[0, 0], [1, 1], [2, 0], [2, 2], [0, 2], [1, 0]]
# apl-source:42
غلاف = جارفيس(نقاط)
# apl-source:43
print("الغلاف:", غلاف)
# apl-source:44

# apl-source:45
تأكد_يساوي(len(غلاف), 4, "أربع زوايا")
# apl-source:46
تأكد_يساوي(غلاف[0][0], 0, "تبدأ من أدنى نقطة")
# apl-source:47
تأكد_يساوي(غلاف[1][0], 2, "ثم أقصى اليمين أسفل")
# apl-source:48

# apl-source:49
# النقاط الداخلية (1,1) و(1,0) مستبعدة... (1,0) على الحافة: الالتفاف الصارم يتخطاها
# apl-source:50
موجود_11 = False
# apl-source:51
for ن in غلاف:
  # apl-source:52
  if ن[0] == 1 and ن[1] == 1:
    # apl-source:53
    موجود_11 = 1 == 1
# apl-source:54
تأكد_يساوي(موجود_11, False, "النقطة الداخلية مستبعدة")
# apl-source:55
