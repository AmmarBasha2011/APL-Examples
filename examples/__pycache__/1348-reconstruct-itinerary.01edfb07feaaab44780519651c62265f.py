
# apl-source:1
# مثال 1348 — إعادة بناء الرحلة
# apl-source:2
# Reconstruct itinerary
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1348-reconstruct-itinerary.apl
# apl-source:6

# apl-source:7
# مسار أويلر يبدأ من JFK
# apl-source:8
# نزور الوجهة الأصغر أولاً ونبني الناتج بالعكس
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
def ارسم_الرحلة(تذاكر):
  # apl-source:19
  مرتبة = sorted(تذاكر)
  # apl-source:20
  مرتبة.reverse()
  # apl-source:21
  وجهات = {}
  # apl-source:22
  for ت in مرتبة:
    # apl-source:23
    if ت[0] not in وجهات:
      # apl-source:24
      وجهات[ت[0]] = []
    # apl-source:25
    وجهات[ت[0]] = وجهات[ت[0]] + [ت[1]]
  # apl-source:26
  مكدس = ["JFK"]
  # apl-source:27
  ناتج = []
  # apl-source:28
  while len(مكدس) > 0:
    # apl-source:29
    اعلى = مكدس[len(مكدس) - 1]
    # apl-source:30
    if (اعلى in وجهات) and (len(وجهات[اعلى]) > 0):
      # apl-source:31
      مكدس = مكدس + [وجهات[اعلى].pop()]
    # apl-source:32
    else:
      # apl-source:33
      ناتج = ناتج + [مكدس.pop()]
  # apl-source:34
  ناتج.reverse()
  # apl-source:35
  return ناتج
# apl-source:36

# apl-source:37
تأكد_يساوي(ارسم_الرحلة([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]), ["JFK","MUC","LHR","SFO","SJC"], "رحلة طويلة")
# apl-source:38
تأكد_يساوي(ارسم_الرحلة([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]), ["JFK","ATL","JFK","SFO","ATL","SFO"], "رحلة بدورة")
# apl-source:39
تأكد_يساوي(ارسم_الرحلة([["JFK","LAX"]]), ["JFK","LAX"], "تذكرة")
# apl-source:40
