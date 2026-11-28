
# apl-source:1
# مثال 1159 — نماذج الحروف
# apl-source:2
# Word pattern signature
# apl-source:3
# Demonstrates: توقيع نمطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1159-isomorphic-groups.apl
# apl-source:6

# apl-source:7
# نستبدل كل حرف برقم ظهوره الأول
# apl-source:8
# فتتطابق الكلمات ذات النمط الواحد
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
def توقيع(ك):
  # apl-source:19
  ارقام = {}
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ح in ك:
    # apl-source:22
    if ح not in ارقام:
      # apl-source:23
      ارقام[ح] = len(ارقام)
    # apl-source:24
    ناتج = ناتج + [ارقام[ح]]
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
def مطابقة(كلمات, نمط):
  # apl-source:28
  ن = توقيع(نمط)
  # apl-source:29
  ناتج = []
  # apl-source:30
  for ك in كلمات:
    # apl-source:31
    if توقيع(ك) == ن:
      # apl-source:32
      ناتج = ناتج + [ك]
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(توقيع("abb"), [0, 1, 1], "توقيع")
# apl-source:36
تأكد_يساوي(مطابقة(["abc","deq","mee","aqq","dkd","ccc"], "abb"), ["mee", "aqq"], "مثال أول")
# apl-source:37
تأكد_يساوي(مطابقة(["aa","ab"], "cc"), ["aa"], "حرفان")
# apl-source:38
