
# apl-source:1
# مثال 1294 — تقويم بلا تداخل
# apl-source:2
# My calendar no double booking
# apl-source:3
# Demonstrates: مجالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1294-my-calendar.apl
# apl-source:6

# apl-source:7
# لا نقبل مجالاً يتقاطع مع مجال محجوز
# apl-source:8
# والتقاطع لو بدأ الجديد قبل نهاية القديم وانتهى بعد بدايته
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
class تقويم:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.حجوزات = []
# apl-source:21

  # apl-source:22
  def احجز(ذات, بداية, نهاية):
    # apl-source:23
    for ح in ذات.حجوزات:
      # apl-source:24
      if (بداية < ح[1]) and (نهاية > ح[0]):
        # apl-source:25
        return False
    # apl-source:26
    ذات.حجوزات = ذات.حجوزات + [[بداية, نهاية]]
    # apl-source:27
    return True
# apl-source:28

# apl-source:29
ت = تقويم()
# apl-source:30
تأكد_يساوي(ت.احجز(10, 20), True, "أول")
# apl-source:31
تأكد_يساوي(ت.احجز(15, 25), False, "تداخل")
# apl-source:32
تأكد_يساوي(ت.احجز(20, 30), True, "متلاصق")
# apl-source:33
تأكد_يساوي(ت.احجز(5, 10), True, "قبله مباشرة")
# apl-source:34
تأكد_يساوي(ت.احجز(0, 40), False, "يحوي الكل")
# apl-source:35
