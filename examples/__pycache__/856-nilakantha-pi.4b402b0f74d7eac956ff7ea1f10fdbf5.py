
# apl-source:1
# مثال 856 — ط بنيلاكانتا
# apl-source:2
# Nilakantha series
# apl-source:3
# Demonstrates: كسور ثلاثية متناوبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/856-nilakantha-pi.apl
# apl-source:6

# apl-source:7
# متسلسلة نيلاكانتا: ط = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
# apl-source:8
# أسرع بكثير من لايبنتز: مئة حد تكفي لخمس خانات
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
def ط_نيلاكانتا(حدود):
  # apl-source:19
  مجموع = 3.0
  # apl-source:20
  إشارة = 1.0
  # apl-source:21
  أ = 2
  # apl-source:22
  for _ in range(حدود):
    # apl-source:23
    مجموع = مجموع + إشارة * 4.0 / (أ * (أ + 1) * (أ + 2))
    # apl-source:24
    إشارة = -إشارة
    # apl-source:25
    أ = أ + 2
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
ط = ط_نيلاكانتا(100)
# apl-source:29
print("ط بعد 100 حد:", ط)
# apl-source:30

# apl-source:31
تأكد_يساوي(round(ط, 5), 3.14159, "خمس خانات صحيحة")
# apl-source:32
تأكد_يساوي(round(ط, 7), 3.1415924, "سبع خانات صحيحة")
# apl-source:33

# apl-source:34
# قارن بالتقارب البطيء للايبنتز: أول حد من نيلاكانتا يعطي 3.1666
# apl-source:35
ط1 = ط_نيلاكانتا(1)
# apl-source:36
تأكد_يساوي(round(ط1, 4), 3.1667, "حد واحد: 3 + 4/24")
# apl-source:37
