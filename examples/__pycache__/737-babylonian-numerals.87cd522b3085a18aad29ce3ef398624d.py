
# apl-source:1
# مثال 737 — أرقام بابلية
# apl-source:2
# Babylonian numerals
# apl-source:3
# Demonstrates: أساس 60، خانات، رسم مسماري
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/737-babylonian-numerals.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# الأرقام البابلية: النظام الستيني (أساس 60)
# apl-source:25
# Demonstrates: قسمة متكررة وباقي القسمة, تحويل أساس, رسم كل خانة بالعشرات والآحاد
# apl-source:26
# كل خانة 0..59 ترسم: "<" لكل عشرة و"|" لكل واحد (محاكاة المسمارية)
# apl-source:27

# apl-source:28
def خانات_ستينية(عدد):
  # apl-source:29
  if عدد == 0:
    # apl-source:30
    return [0]
  # apl-source:31
  خانات = []
  # apl-source:32
  باقي = عدد
  # apl-source:33
  while باقي > 0:
    # apl-source:34
    خانات = [باقي % 60] + خانات
    # apl-source:35
    باقي = باقي // 60
  # apl-source:36
  return خانات
# apl-source:37

# apl-source:38
def ارسم_خانة(خانة):
  # apl-source:39
  ناتج = ""
  # apl-source:40
  عشرات = خانة // 10
  # apl-source:41
  آحاد = خانة % 10
  # apl-source:42
  for ي in range(عشرات):
    # apl-source:43
    ناتج = ناتج + "<"
  # apl-source:44
  for ي in range(آحاد):
    # apl-source:45
    ناتج = ناتج + "|"
  # apl-source:46
  return ناتج
# apl-source:47

# apl-source:48
def ارسم(عدد):
  # apl-source:49
  خانات = خانات_ستينية(عدد)
  # apl-source:50
  أجزاء = []
  # apl-source:51
  for خ in خانات:
    # apl-source:52
    أجزاء.append(ارسم_خانة(خ))
  # apl-source:53
  ناتج = ""
  # apl-source:54
  for ي in range(len(أجزاء)):
    # apl-source:55
    if ي > 0:
      # apl-source:56
      ناتج = ناتج + " "
    # apl-source:57
    if أجزاء[ي] == "":
      # apl-source:58
      ناتج = ناتج + "."
    # apl-source:59
    else:
      # apl-source:60
      ناتج = ناتج + أجزاء[ي]
  # apl-source:61
  return ناتج
# apl-source:62

# apl-source:63
def من_ستيني(خانات):
  # apl-source:64
  قيمة = 0
  # apl-source:65
  for خ in خانات:
    # apl-source:66
    قيمة = قيمة * 60 + خ
  # apl-source:67
  return قيمة
# apl-source:68

# apl-source:69
تأكد_يساوي(خانات_ستينية(0), [0], "صفر")
# apl-source:70
تأكد_يساوي(خانات_ستينية(59), [59], "خانة واحدة")
# apl-source:71
تأكد_يساوي(خانات_ستينية(60), [1, 0], "ستون = واحد صفر")
# apl-source:72
تأكد_يساوي(خانات_ستينية(125), [2, 5], "مئة وخمسة وعشرون")
# apl-source:73
تأكد_يساوي(خانات_ستينية(3661), [1, 1, 1], "ثلاث خانات")
# apl-source:74
تأكد_يساوي(خانات_ستينية(7200), [2, 0, 0], "ستون مربع ضعفان")
# apl-source:75

# apl-source:76
تأكد_يساوي(ارسم_خانة(25), "<<|||||", "خمسة وعشرون مرسومة")
# apl-source:77
تأكد_يساوي(ارسم_خانة(9), "|||||||||", "تسعة")
# apl-source:78
تأكد_يساوي(ارسم(125), "|| |||||", "مئة وخمسة وعشرون مرسومة")
# apl-source:79
تأكد_يساوي(ارسم(60), "| .", "صفر كنقطة")
# apl-source:80

# apl-source:81
تأكد_يساوي(من_ستيني([1, 1, 1]), 3661, "قراءة عكسية")
# apl-source:82
تأكد_يساوي(من_ستيني(خانات_ستينية(4242)), 4242, "ذهاب وإياب")
# apl-source:83

# apl-source:84
print("3661 =", ارسم(3661))
# apl-source:85
