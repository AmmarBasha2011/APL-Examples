
# apl-source:1
# مثال 857 — ط بصيغة ماشين
# apl-source:2
# Machin formula
# apl-source:3
# Demonstrates: arctan مركبة، تايلور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/857-machin-pi.apl
# apl-source:6

# apl-source:7
# صيغة ماشين: ط/4 = 4 arctan(1/5) - arctan(1/239)
# apl-source:8
# arctan بمتسلسلة تايلور؛ استخدمت لحساب ط يدوياً لمئة خانة عام 1706
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
def آركتان(س, حدود):
  # apl-source:19
  مجموع = 0.0
  # apl-source:20
  قوة = س
  # apl-source:21
  إشارة = 1.0
  # apl-source:22
  for ك in range(حدود):
    # apl-source:23
    مجموع = مجموع + إشارة * قوة / (2 * ك + 1)
    # apl-source:24
    إشارة = -إشارة
    # apl-source:25
    قوة = قوة * س * س
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
ط = 4.0 * (4.0 * آركتان(0.2, 15) - آركتان(0.0041841004184100415, 5))
# apl-source:29
print("ط بصيغة ماشين:", ط)
# apl-source:30

# apl-source:31
تأكد_يساوي(round(ط, 9), 3.141592654, "تسع خانات عشرية صحيحة")
# apl-source:32

# apl-source:33
# آركتان(1) = ط/4: تحقق مستقل عبر ماشين نفسها
# apl-source:34
ربع_ط = آركتان(1.0, 2000)
# apl-source:35
تأكد_يساوي(round(4.0 * ربع_ط, 2), 3.14, "arctan(1) متقاربة مع الصيغة")
# apl-source:36
