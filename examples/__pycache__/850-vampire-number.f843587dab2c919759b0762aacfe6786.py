
# apl-source:1
# مثال 850 — الأعداد المصاصة
# apl-source:2
# Vampire numbers
# apl-source:3
# Demonstrates: أنياب بأرقام العدد نفسها
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/850-vampire-number.apl
# apl-source:6

# apl-source:7
# الأعداد المصاصة: عدد = جداء "أنياب" يشكلان معاً أرقامه نفسها
# apl-source:8
# 1260 = 21 * 60 وكلاهما من أرقام 1260
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
def بصمة_أرقام(ن):
  # apl-source:19
  بصمة = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # apl-source:20
  م = ن
  # apl-source:21
  if م == 0:
    # apl-source:22
    بصمة[0] = 1
  # apl-source:23
  while م > 0:
    # apl-source:24
    بصمة[م % 10] = بصمة[م % 10] + 1
    # apl-source:25
    م = م // 10
  # apl-source:26
  return بصمة
# apl-source:27

# apl-source:28
def مصاص(ن):
  # apl-source:29
  # أربعة أرقام: أنياب من رقمين
  # apl-source:30
  if ن < 1000 or ن > 9999:
    # apl-source:31
    return False
  # apl-source:32
  بصمة_ن = بصمة_أرقام(ن)
  # apl-source:33
  for س in range(10, 100):
    # apl-source:34
    for ص in range(س, 100):
      # apl-source:35
      if س * ص == ن:
        # apl-source:36
        # لا ينتهي الاثنان بصفر معاً
        # apl-source:37
        if س % 10 != 0 or ص % 10 != 0:
          # apl-source:38
          بس = بصمة_أرقام(س)
          # apl-source:39
          بص = بصمة_أرقام(ص)
          # apl-source:40
          متطابق = 1 == 1
          # apl-source:41
          for ر in range(10):
            # apl-source:42
            if بس[ر] + بص[ر] != بصمة_ن[ر]:
              # apl-source:43
              متطابق = False
          # apl-source:44
          if متطابق:
            # apl-source:45
            return 1 == 1
  # apl-source:46
  return False
# apl-source:47

# apl-source:48
مصاصة = []
# apl-source:49
for ن in range(1000, 2000):
  # apl-source:50
  if مصاص(ن):
    # apl-source:51
    مصاصة = مصاصة + [ن]
# apl-source:52

# apl-source:53
print("مصاصة تحت 2000:", مصاصة)
# apl-source:54

# apl-source:55
تأكد_يساوي(len(مصاصة), 5, "خمسة تحت 2000")
# apl-source:56
تأكد_يساوي(مصاصة[0], 1260, "الأول 1260 = 21*60")
# apl-source:57
تأكد_يساوي(مصاصة[1], 1395, "الثاني 1395 = 15*93")
# apl-source:58
تأكد_يساوي(مصاصة[4], 1827, "الخامس 1827 = 21*87")
# apl-source:59

# apl-source:60
تأكد_يساوي(مصاص(1200), False, "1200 ليس مصاصاً")
# apl-source:61
