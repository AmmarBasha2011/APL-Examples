
# apl-source:1
# مثال 780 — آلة تورينغ
# apl-source:2
# Turing machine
# apl-source:3
# Demonstrates: شريط ورأس، جدول انتقالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/780-turing-machine.apl
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
# آلة تورينغ: جمع أحادي "111+11=" إلى "11111"
# apl-source:25
# Demonstrates: شريط ورأس, جدول انتقالات, حالة توقف
# apl-source:26

# apl-source:27
def آلة_تورينغ(مدخل, قواعد, بداية, نهاية):
  # apl-source:28
  شريط = []
  # apl-source:29
  for حرف in مدخل:
    # apl-source:30
    شريط.append(حرف)
  # apl-source:31
  for ي in range(20):
    # apl-source:32
    شريط.append(" ")
  # apl-source:33
  موضع = 0
  # apl-source:34
  حالة = بداية
  # apl-source:35
  خطوات = 0
  # apl-source:36
  while حالة != نهاية and خطوات < 1000:
    # apl-source:37
    مطبقة = False
    # apl-source:38
    for قاعدة in قواعد:
      # apl-source:39
      if قاعدة[0] == حالة and قاعدة[1] == شريط[موضع] and مطبقة == False:
        # apl-source:40
        شريط[موضع] = قاعدة[2]
        # apl-source:41
        موضع = موضع + قاعدة[3]
        # apl-source:42
        حالة = قاعدة[4]
        # apl-source:43
        مطبقة = True
    # apl-source:44
    خطوات = خطوات + 1
  # apl-source:45
  return [شريط, خطوات, حالة]
# apl-source:46

# apl-source:47
قواعد = [["q0", "1", "1", 1, "q0"], ["q0", "+", "1", 1, "q1"], ["q1", "1", "1", 1, "q1"], ["q1", "=", " ", -1, "q2"], ["q2", "1", " ", 0, "qf"]]
# apl-source:48
ن = آلة_تورينغ("111+11=", قواعد, "q0", "qf")
# apl-source:49
شريط = ن[0]
# apl-source:50
تأكد_يساوي(ن[2], "qf", "توقفت")
# apl-source:51
تأكد_يساوي(ن[1], 8, "عدد الخطوات")
# apl-source:52
تأكد_يساوي(شريط[0] + شريط[1] + شريط[2] + شريط[3] + شريط[4], "11111", "الناتج 3+2=5")
# apl-source:53
تأكد_يساوي(شريط[5], " ", "مسح الأخيرة")
# apl-source:54
ن2 = آلة_تورينغ("1+1=", قواعد, "q0", "qf")
# apl-source:55
ش2 = ن2[0]
# apl-source:56
تأكد_يساوي(ش2[0] + ش2[1], "11", "الناتج 1+1=2")
# apl-source:57
