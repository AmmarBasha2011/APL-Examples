
# apl-source:1
# مثال 632 — مخصص ذاكرة بأول ملائم
# apl-source:2
# First-fit allocator
# apl-source:3
# Demonstrates: malloc، كتل، دمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/632-allocator-first-fit.apl
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
# محاكي مخصص ذاكرة: أول ملائم مع دمج الحر
# apl-source:25
# Demonstrates: كتل حرة ومشغولة, أول ملائم, دمج الجيران
# apl-source:26
# هكذا تدير malloc الذاكرة
# apl-source:27

# apl-source:28
def أنشئ_ذاكرة(حجم):
  # apl-source:29
  return [{"بداية": 0, "حجم": حجم, "حر": True}]
# apl-source:30

# apl-source:31
def خصص(ذاكرة, حجم):
  # apl-source:32
  for كتلة in ذاكرة:
    # apl-source:33
    if كتلة["حر"] and كتلة["حجم"] >= حجم:
      # apl-source:34
      بداية = كتلة["بداية"]
      # apl-source:35
      if كتلة["حجم"] > حجم:
        # apl-source:36
        ذاكرة.insert(ذاكرة.index(كتلة) + 1, {"بداية": بداية + حجم, "حجم": كتلة["حجم"] - حجم, "حر": True})
        # apl-source:37
        كتلة["حجم"] = حجم
      # apl-source:38
      كتلة["حر"] = False
      # apl-source:39
      return بداية
  # apl-source:40
  return -1
# apl-source:41

# apl-source:42
def حرر(ذاكرة, بداية):
  # apl-source:43
  for كتلة in ذاكرة:
    # apl-source:44
    if كتلة["بداية"] == بداية:
      # apl-source:45
      كتلة["حر"] = True
  # apl-source:46
  ذاكرة2 = []
  # apl-source:47
  for كتلة in ذاكرة:
    # apl-source:48
    if len(ذاكرة2) > 0 and ذاكرة2[len(ذاكرة2) - 1]["حر"] and كتلة["حر"]:
      # apl-source:49
      ذاكرة2[len(ذاكرة2) - 1]["حجم"] = ذاكرة2[len(ذاكرة2) - 1]["حجم"] + كتلة["حجم"]
    # apl-source:50
    else:
      # apl-source:51
      ذاكرة2.append(كتلة)
  # apl-source:52
  return ذاكرة2
# apl-source:53

# apl-source:54
ذاكرة = أنشئ_ذاكرة(100)
# apl-source:55
أ = خصص(ذاكرة, 30)
# apl-source:56
ب = خصص(ذاكرة, 20)
# apl-source:57
ج = خصص(ذاكرة, 50)
# apl-source:58
تأكد_يساوي([أ, ب, ج], [0, 30, 50], "عناوين متتالية")
# apl-source:59
تأكد_يساوي(خصص(ذاكرة, 10), -1, "لا مكان")
# apl-source:60
ذاكرة = حرر(ذاكرة, 30)
# apl-source:61
تأكد_يساوي(خصص(ذاكرة, 10), 30, "إعادة استخدام الحر")
# apl-source:62
ذاكرة = حرر(ذاكرة, 0)
# apl-source:63
ذاكرة = حرر(ذاكرة, 50)
# apl-source:64
ذاكرة = حرر(ذاكرة, 30)
# apl-source:65
تأكد_يساوي(خصص(ذاكرة, 90), 0, "دمج الجيران كلها")
# apl-source:66
print("كتل:", len(ذاكرة))
# apl-source:67
