
# apl-source:1
# مثال 1182 — محاكاة كويكبات
# apl-source:2
# Asteroid collision stack variant
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1182-asteroid-field-sim.apl
# apl-source:6

# apl-source:7
# الموجب يتحرك يميناً والسالب يساراً
# apl-source:8
# يتصادمان فقط حين يقابل سالب موجباً
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
def تصادم(ك):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for س in ك:
    # apl-source:21
    حي = True
    # apl-source:22
    while حي and (س < 0) and (len(مكدس) > 0) and (مكدس[-1] > 0):
      # apl-source:23
      if مكدس[-1] < -س:
        # apl-source:24
        مكدس.pop()
      # apl-source:25
      elif مكدس[-1] == -س:
        # apl-source:26
        مكدس.pop()
        # apl-source:27
        حي = False
      # apl-source:28
      else:
        # apl-source:29
        حي = False
    # apl-source:30
    if حي:
      # apl-source:31
      مكدس = مكدس + [س]
  # apl-source:32
  return مكدس
# apl-source:33

# apl-source:34
تأكد_يساوي(تصادم([5,10,-5]), [5,10], "ينجو الأكبر")
# apl-source:35
تأكد_يساوي(تصادم([8,-8]), [], "تعادل")
# apl-source:36
تأكد_يساوي(تصادم([10,2,-5]), [10], "ينجو الأول")
# apl-source:37
تأكد_يساوي(تصادم([-2,-1,1,2]), [-2,-1,1,2], "لا تصادم")
# apl-source:38
