
# apl-source:1
# مثال 827 — الزواج المستقر
# apl-source:2
# Gale-Shapley
# apl-source:3
# Demonstrates: قبول مؤجل، قوائم تفضيل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/827-gale-shapley.apl
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
# زواج مستقر بقبول مؤجل: الرجال يعرضون والنساء يخترن الأفضل
# apl-source:25
# Demonstrates: قوائم تفضيل, خطوبة قابلة للاستبدال, استقرار مضمون
# apl-source:26

# apl-source:27
عروض_رجال = [["س", "ل", "م"], ["ل", "س", "م"], ["س", "م", "ل"]]
# apl-source:28
تفضيل_نساء = [["ب", "أ", "ج"], ["أ", "ب", "ج"], ["أ", "ج", "ب"]]
# apl-source:29
رجال = ["أ", "ب", "ج"]
# apl-source:30
نساء = ["س", "ل", "م"]
# apl-source:31

# apl-source:32
def زواج():
  # apl-source:33
  خطوبة = [-1, -1, -1]
  # apl-source:34
  تالي = [0, 0, 0]
  # apl-source:35
  أحرار = [0, 1, 2]
  # apl-source:36
  while len(أحرار) > 0:
    # apl-source:37
    رجل = أحرار.pop(0)
    # apl-source:38
    امرأة = نساء.index(عروض_رجال[رجل][تالي[رجل]])
    # apl-source:39
    تالي[رجل] = تالي[رجل] + 1
    # apl-source:40
    if خطوبة[امرأة] == -1:
      # apl-source:41
      خطوبة[امرأة] = رجل
    # apl-source:42
    else:
      # apl-source:43
      حالي = خطوبة[امرأة]
      # apl-source:44
      if تفضيل_نساء[امرأة].index(رجال[رجل]) < تفضيل_نساء[امرأة].index(رجال[حالي]):
        # apl-source:45
        خطوبة[امرأة] = رجل
        # apl-source:46
        أحرار.append(حالي)
      # apl-source:47
      else:
        # apl-source:48
        أحرار.append(رجل)
  # apl-source:49
  ناتج = []
  # apl-source:50
  for ي in range(3):
    # apl-source:51
    ناتج.append([رجال[خطوبة[ي]], نساء[ي]])
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
نتيجة = زواج()
# apl-source:55
تأكد_يساوي(نتيجة, [["أ", "س"], ["ب", "ل"], ["ج", "م"]], "الزواج المستقر")
# apl-source:56
تأكد_يساوي(len(نتيجة), 3, "ثلاثة أزواج")
# apl-source:57
