
# apl-source:1
# مثال 1192 — تصميم تويتر
# apl-source:2
# Design a mini twitter feed
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1192-design-twitter.apl
# apl-source:6

# apl-source:7
# نخزن التغريدات بوقت متزايد
# apl-source:8
# والخلاصة هي أحدث تغريدات المستخدم ومن يتابعهم
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
class تويتر:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.ساعة = 0
    # apl-source:21
    ذات.تغريدات = []
    # apl-source:22
    ذات.متابعون = {}
# apl-source:23

  # apl-source:24
  def نشر(ذات, مستخدم, رقم):
    # apl-source:25
    ذات.ساعة = ذات.ساعة + 1
    # apl-source:26
    ذات.تغريدات = ذات.تغريدات + [[ذات.ساعة, مستخدم, رقم]]
# apl-source:27

  # apl-source:28
  def تابع(ذات, أ, ب):
    # apl-source:29
    if أ not in ذات.متابعون:
      # apl-source:30
      ذات.متابعون[أ] = []
    # apl-source:31
    if ب not in ذات.متابعون[أ]:
      # apl-source:32
      ذات.متابعون[أ] = ذات.متابعون[أ] + [ب]
# apl-source:33

  # apl-source:34
  def الغ_متابعة(ذات, أ, ب):
    # apl-source:35
    if أ in ذات.متابعون:
      # apl-source:36
      if ب in ذات.متابعون[أ]:
        # apl-source:37
        ذات.متابعون[أ].remove(ب)
# apl-source:38

  # apl-source:39
  def خلاصة(ذات, مستخدم):
    # apl-source:40
    مسموح = [مستخدم] + ذات.متابعون.get(مستخدم, [])
    # apl-source:41
    ناتج = []
    # apl-source:42
    ع = len(ذات.تغريدات) - 1
    # apl-source:43
    while (ع >= 0) and (len(ناتج) < 10):
      # apl-source:44
      if ذات.تغريدات[ع][1] in مسموح:
        # apl-source:45
        ناتج = ناتج + [ذات.تغريدات[ع][2]]
      # apl-source:46
      ع = ع - 1
    # apl-source:47
    return ناتج
# apl-source:48

# apl-source:49
ت = تويتر()
# apl-source:50
ت.نشر(1, 5)
# apl-source:51
تأكد_يساوي(ت.خلاصة(1), [5], "تغريدتي")
# apl-source:52
ت.تابع(1, 2)
# apl-source:53
ت.نشر(2, 6)
# apl-source:54
تأكد_يساوي(ت.خلاصة(1), [6, 5], "مع متابعة")
# apl-source:55
ت.الغ_متابعة(1, 2)
# apl-source:56
تأكد_يساوي(ت.خلاصة(1), [5], "بعد الإلغاء")
# apl-source:57
for ع in range(12):
  # apl-source:58
  ت.نشر(3, 100 + ع)
# apl-source:59
تأكد_يساوي(len(ت.خلاصة(3)), 10, "عشر تغريدات فقط")
# apl-source:60
