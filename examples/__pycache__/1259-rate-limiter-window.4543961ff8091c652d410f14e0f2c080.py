
# apl-source:1
# مثال 1259 — محدد المعدل
# apl-source:2
# Sliding window rate limiter
# apl-source:3
# Demonstrates: نافذة زمنية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1259-rate-limiter-window.apl
# apl-source:6

# apl-source:7
# نحتفظ بأوقات الطلبات المقبولة
# apl-source:8
# ونحذف ما خرج من النافذة قبل كل قرار
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
class محدد:
  # apl-source:19
  def __init__(ذات, حد, نافذة):
    # apl-source:20
    ذات.حد = حد
    # apl-source:21
    ذات.نافذة = نافذة
    # apl-source:22
    ذات.اوقات = []
# apl-source:23

  # apl-source:24
  def اسمح(ذات, وقت):
    # apl-source:25
    while (len(ذات.اوقات) > 0) and (ذات.اوقات[0] <= وقت - ذات.نافذة):
      # apl-source:26
      ذات.اوقات.pop(0)
    # apl-source:27
    if len(ذات.اوقات) < ذات.حد:
      # apl-source:28
      ذات.اوقات = ذات.اوقات + [وقت]
      # apl-source:29
      return True
    # apl-source:30
    return False
# apl-source:31

# apl-source:32
م = محدد(2, 10)
# apl-source:33
تأكد_يساوي(م.اسمح(1), True, "أول")
# apl-source:34
تأكد_يساوي(م.اسمح(2), True, "ثان")
# apl-source:35
تأكد_يساوي(م.اسمح(3), False, "ثالث مرفوض")
# apl-source:36
تأكد_يساوي(م.اسمح(11), True, "خرج الأول من النافذة")
# apl-source:37
تأكد_يساوي(م.اسمح(12), True, "خرج الثاني")
# apl-source:38
تأكد_يساوي(م.اسمح(13), False, "ممتلئة")
# apl-source:39
