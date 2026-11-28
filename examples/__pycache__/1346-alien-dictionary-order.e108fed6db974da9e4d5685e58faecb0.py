
# apl-source:1
# مثال 1346 — ترتيب قاموس غريب
# apl-source:2
# Alien dictionary order
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1346-alien-dictionary-order.apl
# apl-source:6

# apl-source:7
# نقارن كل كلمتين متجاورتين لنجد أول حرف مختلف
# apl-source:8
# ثم نرتب الحروف طوبولوجياً
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
def ترتيب_الحروف(كلمات):
  # apl-source:19
  تالي = {}
  # apl-source:20
  دخل = {}
  # apl-source:21
  for ك in كلمات:
    # apl-source:22
    for ح in ك:
      # apl-source:23
      if ح not in تالي:
        # apl-source:24
        تالي[ح] = []
        # apl-source:25
        دخل[ح] = 0
  # apl-source:26
  for ع in range(len(كلمات) - 1):
    # apl-source:27
    أ = كلمات[ع]
    # apl-source:28
    ب = كلمات[ع + 1]
    # apl-source:29
    if (len(أ) > len(ب)) and (أ[:len(ب)] == ب):
      # apl-source:30
      return ""
    # apl-source:31
    for ج in range(min(len(أ), len(ب))):
      # apl-source:32
      if أ[ج] != ب[ج]:
        # apl-source:33
        if ب[ج] not in تالي[أ[ج]]:
          # apl-source:34
          تالي[أ[ج]] = تالي[أ[ج]] + [ب[ج]]
          # apl-source:35
          دخل[ب[ج]] = دخل[ب[ج]] + 1
  # apl-source:36
  طابور = []
  # apl-source:37
  for ح in تالي:
    # apl-source:38
    if دخل[ح] == 0:
      # apl-source:39
      طابور = طابور + [ح]
  # apl-source:40
  ناتج = ""
  # apl-source:41
  ع = 0
  # apl-source:42
  while ع < len(طابور):
    # apl-source:43
    ح = طابور[ع]
    # apl-source:44
    ع = ع + 1
    # apl-source:45
    ناتج = ناتج + ح
    # apl-source:46
    for ت in تالي[ح]:
      # apl-source:47
      دخل[ت] = دخل[ت] - 1
      # apl-source:48
      if دخل[ت] == 0:
        # apl-source:49
        طابور = طابور + [ت]
  # apl-source:50
  if len(ناتج) != len(تالي):
    # apl-source:51
    return ""
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
تأكد_يساوي(ترتيب_الحروف(["wrt","wrf","er","ett","rftt"]), "wertf", "مثال أول")
# apl-source:55
تأكد_يساوي(ترتيب_الحروف(["z","x"]), "zx", "حرفان")
# apl-source:56
تأكد_يساوي(ترتيب_الحروف(["z","x","z"]), "", "دورة")
# apl-source:57
