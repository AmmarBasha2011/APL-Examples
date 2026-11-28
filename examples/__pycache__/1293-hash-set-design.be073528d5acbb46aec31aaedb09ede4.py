
# apl-source:1
# مثال 1293 — مجموعة بالتجزئة
# apl-source:2
# Design a hash set
# apl-source:3
# Demonstrates: جداول تجزئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1293-hash-set-design.apl
# apl-source:6

# apl-source:7
# المجموعة سطول قوائم
# apl-source:8
# الإضافة لا تكرر العنصر
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
class مجموعة_تجزئة:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.سطول = []
    # apl-source:21
    for ع in range(11):
      # apl-source:22
      ذات.سطول = ذات.سطول + [[]]
# apl-source:23

  # apl-source:24
  def اضف(ذات, م):
    # apl-source:25
    if م not in ذات.سطول[م % 11]:
      # apl-source:26
      ذات.سطول[م % 11] = ذات.سطول[م % 11] + [م]
# apl-source:27

  # apl-source:28
  def ازل(ذات, م):
    # apl-source:29
    if م in ذات.سطول[م % 11]:
      # apl-source:30
      ذات.سطول[م % 11].remove(م)
# apl-source:31

  # apl-source:32
  def يحوي(ذات, م):
    # apl-source:33
    return م in ذات.سطول[م % 11]
# apl-source:34

# apl-source:35
م = مجموعة_تجزئة()
# apl-source:36
م.اضف(1)
# apl-source:37
م.اضف(2)
# apl-source:38
م.اضف(1)
# apl-source:39
تأكد_يساوي(م.يحوي(1), True, "موجود")
# apl-source:40
تأكد_يساوي(م.يحوي(3), False, "غير موجود")
# apl-source:41
م.ازل(2)
# apl-source:42
تأكد_يساوي(م.يحوي(2), False, "بعد الإزالة")
# apl-source:43
م.ازل(1)
# apl-source:44
تأكد_يساوي(م.يحوي(1), False, "إزالة بعد تكرار")
# apl-source:45
