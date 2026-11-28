
# apl-source:1
# مثال 619 — تفقيط المبالغ
# apl-source:2
# Amount to Arabic words
# apl-source:3
# Demonstrates: تفقيط، كلمات عربية، فواتير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/619-tafqeet.apl
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
# تفقيط: تحويل المبلغ إلى كلمات عربية
# apl-source:25
# Demonstrates: جداول أرقام, قواعد التركيب, واو العطف
# apl-source:26
# أساس فواتير وشيكات مكتوبة بالحروف
# apl-source:27

# apl-source:28
آحاد = ["", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", "عشرة", "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر", "خمسة عشر", "ستة عشر", "سبعة عشر", "ثمانية عشر", "تسعة عشر"]
# apl-source:29
عشرات = ["", "عشرة", "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون"]
# apl-source:30
مئات = ["", "مائة", "مائتان", "ثلاثمائة", "أربعمائة", "خمسمائة", "ستمائة", "سبعمائة", "ثمانمائة", "تسعمائة"]
# apl-source:31

# apl-source:32
def ثلاثة_أرقام(ن):
  # apl-source:33
  أجزاء = []
  # apl-source:34
  م = ن // 100
  # apl-source:35
  باقي = ن % 100
  # apl-source:36
  if م > 0:
    # apl-source:37
    أجزاء.append(مئات[م])
  # apl-source:38
  if باقي > 0:
    # apl-source:39
    if باقي < 20:
      # apl-source:40
      أجزاء.append(آحاد[باقي])
    # apl-source:41
    else:
      # apl-source:42
      أ = باقي % 10
      # apl-source:43
      ع = باقي // 10
      # apl-source:44
      if أ > 0:
        # apl-source:45
        أجزاء.append(آحاد[أ] + " و" + عشرات[ع])
      # apl-source:46
      else:
        # apl-source:47
        أجزاء.append(عشرات[ع])
  # apl-source:48
  return " و".join(أجزاء)
# apl-source:49

# apl-source:50
def تفقيط(ن):
  # apl-source:51
  if ن == 0:
    # apl-source:52
    return "صفر"
  # apl-source:53
  أجزاء = []
  # apl-source:54
  آلاف = ن // 1000
  # apl-source:55
  باقي = ن % 1000
  # apl-source:56
  if آلاف == 1:
    # apl-source:57
    أجزاء.append("ألف")
  # apl-source:58
  if آلاف == 2:
    # apl-source:59
    أجزاء.append("ألفان")
  # apl-source:60
  if آلاف > 2:
    # apl-source:61
    أجزاء.append(ثلاثة_أرقام(آلاف) + " آلاف")
  # apl-source:62
  if باقي > 0:
    # apl-source:63
    أجزاء.append(ثلاثة_أرقام(باقي))
  # apl-source:64
  return " و".join(أجزاء)
# apl-source:65

# apl-source:66
تأكد_يساوي(تفقيط(0), "صفر", "الصفر")
# apl-source:67
تأكد_يساوي(تفقيط(125), "مائة وخمسة وعشرون", "مائة وخمسة وعشرون")
# apl-source:68
تأكد_يساوي(تفقيط(1000), "ألف", "ألف")
# apl-source:69
تأكد_يساوي(تفقيط(2000), "ألفان", "ألفان")
# apl-source:70
تأكد_يساوي(تفقيط(2025), "ألفان وخمسة وعشرون", "ألفان وخمسة وعشرون")
# apl-source:71
تأكد_يساوي(تفقيط(99), "تسعة وتسعون", "تسعة وتسعون")
# apl-source:72
print("2025 =", تفقيط(2025))
# apl-source:73
