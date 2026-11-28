
# apl-source:1
# مثال 1260 — موقف سيارات
# apl-source:2
# Parking lot with slots by size
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1260-parking-lot-slots.apl
# apl-source:6

# apl-source:7
# لكل حجم عدد أماكن محدد
# apl-source:8
# السيارة تحجز مكاناً من حجمها لو توافر
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
class موقف:
  # apl-source:19
  def __init__(ذات, كبيرة, متوسطة, صغيرة):
    # apl-source:20
    ذات.متاح = {1: كبيرة, 2: متوسطة, 3: صغيرة}
# apl-source:21

  # apl-source:22
  def اركن(ذات, نوع_سيارة):
    # apl-source:23
    if ذات.متاح[نوع_سيارة] > 0:
      # apl-source:24
      ذات.متاح[نوع_سيارة] = ذات.متاح[نوع_سيارة] - 1
      # apl-source:25
      return True
    # apl-source:26
    return False
# apl-source:27

# apl-source:28
م = موقف(1, 1, 0)
# apl-source:29
تأكد_يساوي(م.اركن(1), True, "كبيرة")
# apl-source:30
تأكد_يساوي(م.اركن(2), True, "متوسطة")
# apl-source:31
تأكد_يساوي(م.اركن(3), False, "لا صغيرة")
# apl-source:32
تأكد_يساوي(م.اركن(1), False, "ممتلئ")
# apl-source:33
