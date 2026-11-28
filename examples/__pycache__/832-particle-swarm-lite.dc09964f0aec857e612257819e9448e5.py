
# apl-source:1
# مثال 832 — سرب الجسيمات
# apl-source:2
# Particle swarm
# apl-source:3
# Demonstrates: قصور ومعرفة واجتماع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/832-particle-swarm-lite.apl
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
# سرب جسيمات PSO: سرعة بقصور وذاكرة فردية وجماعية
# apl-source:25
# Demonstrates: مكونات قصور ومعرفي واجتماعي, أفضل شخصي وعام, LCG حتمي
# apl-source:26

# apl-source:27
def هدف(س):
  # apl-source:28
  return (س - 2) * (س - 2)
# apl-source:29

# apl-source:30
def سرب(دورات):
  # apl-source:31
  بذرة = 999
  # apl-source:32
  مواقع = [-5.0, 7.0]
  # apl-source:33
  سرعات = []
  # apl-source:34
  for ي in range(2):
    # apl-source:35
    بذرة = (بذرة * 1103515245 + 12345) % 2147483648
    # apl-source:36
    سرعات.append(بذرة / 2147483648.0 * 2 - 1)
  # apl-source:37
  شخصي = [مواقع[0], مواقع[1]]
  # apl-source:38
  قيم_شخصي = [هدف(مواقع[0]), هدف(مواقع[1])]
  # apl-source:39
  أفضل_عام = مواقع[0]
  # apl-source:40
  قيمة_عام = قيم_شخصي[0]
  # apl-source:41
  if قيم_شخصي[1] < قيمة_عام:
    # apl-source:42
    أفضل_عام = مواقع[1]
    # apl-source:43
    قيمة_عام = قيم_شخصي[1]
  # apl-source:44
  for دورة in range(دورات):
    # apl-source:45
    for ي in range(2):
      # apl-source:46
      بذرة = (بذرة * 1103515245 + 12345) % 2147483648
      # apl-source:47
      عشوائي1 = بذرة / 2147483648.0
      # apl-source:48
      بذرة = (بذرة * 1103515245 + 12345) % 2147483648
      # apl-source:49
      عشوائي2 = بذرة / 2147483648.0
      # apl-source:50
      سرعات[ي] = 0.7 * سرعات[ي] + 1.4 * عشوائي1 * (شخصي[ي] - مواقع[ي]) + 1.4 * عشوائي2 * (أفضل_عام - مواقع[ي])
      # apl-source:51
      مواقع[ي] = مواقع[ي] + سرعات[ي]
      # apl-source:52
      قيمة = هدف(مواقع[ي])
      # apl-source:53
      if قيمة < قيم_شخصي[ي]:
        # apl-source:54
        شخصي[ي] = مواقع[ي]
        # apl-source:55
        قيم_شخصي[ي] = قيمة
      # apl-source:56
      if قيمة < قيمة_عام:
        # apl-source:57
        أفضل_عام = مواقع[ي]
        # apl-source:58
        قيمة_عام = قيمة
  # apl-source:59
  return [أفضل_عام, قيمة_عام]
# apl-source:60

# apl-source:61
نتيجة = سرب(30)
# apl-source:62
تأكد_يساوي(round(نتيجة[0], 4), 2.0021, "موقع الأمثل")
# apl-source:63
تأكد_يساوي(round(نتيجة[1], 6), 0.000004, "قيمة الأمثل")
# apl-source:64
نتيجة2 = سرب(5)
# apl-source:65
تأكد_يساوي(نتيجة2[1] < 4.0 == False, False, "خمس دورات تقرب")
# apl-source:66
