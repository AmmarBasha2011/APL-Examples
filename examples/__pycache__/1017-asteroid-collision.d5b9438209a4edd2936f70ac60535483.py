
# apl-source:1
# مثال 1017 — تصادم الكويكبات
# apl-source:2
# Asteroid collision
# apl-source:3
# Demonstrates: مكدس وإشارة الاتجاه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1017-asteroid-collision.apl
# apl-source:6

# apl-source:7
# الإشارة الموجبة تتجه يميناً والسالبة يساراً
# apl-source:8
# يتصادمان فقط حين يكون الأيمن موجباً والتالي سالباً والأكبر ينجو
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
def تصادم(كويكبات):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ك in كويكبات:
    # apl-source:21
    حي = True
    # apl-source:22
    while حي and (ك < 0) and (len(مكدس) > 0) and (مكدس[len(مكدس) - 1] > 0):
      # apl-source:23
      قمة = مكدس[len(مكدس) - 1]
      # apl-source:24
      if قمة < -ك:
        # apl-source:25
        مكدس.pop()
      # apl-source:26
      elif قمة == -ك:
        # apl-source:27
        مكدس.pop()
        # apl-source:28
        حي = False
      # apl-source:29
      else:
        # apl-source:30
        حي = False
    # apl-source:31
    if حي:
      # apl-source:32
      مكدس = مكدس + [ك]
  # apl-source:33
  return مكدس
# apl-source:34

# apl-source:35
تأكد_يساوي(تصادم([5, 10, -5]), [5, 10], "الصغير ينفجر")
# apl-source:36
تأكد_يساوي(تصادم([8, -8]), [], "تساوٍ")
# apl-source:37
تأكد_يساوي(تصادم([10, 2, -5]), [10], "ينجو الأكبر")
# apl-source:38
تأكد_يساوي(تصادم([-2, -1, 1, 2]), [-2, -1, 1, 2], "متباعدة")
# apl-source:39
