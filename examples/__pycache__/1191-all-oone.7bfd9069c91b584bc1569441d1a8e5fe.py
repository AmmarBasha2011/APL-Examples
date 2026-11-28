
# apl-source:1
# مثال 1191 — أكبر وأصغر عدّاد
# apl-source:2
# All O(1) data structure
# apl-source:3
# Demonstrates: قاموس عدّادات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1191-all-oone.apl
# apl-source:6

# apl-source:7
# نخزن عدّاد كل مفتاح
# apl-source:8
# ونحسب الأكبر والأصغر عند الطلب
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
class عدادات:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.ع = {}
# apl-source:21

  # apl-source:22
  def زد(ذات, م):
    # apl-source:23
    ذات.ع[م] = ذات.ع.get(م, 0) + 1
# apl-source:24

  # apl-source:25
  def انقص(ذات, م):
    # apl-source:26
    if م in ذات.ع:
      # apl-source:27
      ذات.ع[م] = ذات.ع[م] - 1
      # apl-source:28
      if ذات.ع[م] == 0:
        # apl-source:29
        ذات.ع.pop(م)
# apl-source:30

  # apl-source:31
  def مفتاح_اكبر(ذات):
    # apl-source:32
    افضل = ""
    # apl-source:33
    قيمة = -1
    # apl-source:34
    for م in ذات.ع:
      # apl-source:35
      if ذات.ع[م] > قيمة:
        # apl-source:36
        قيمة = ذات.ع[م]
        # apl-source:37
        افضل = م
    # apl-source:38
    return افضل
# apl-source:39

  # apl-source:40
  def مفتاح_اصغر(ذات):
    # apl-source:41
    افضل = ""
    # apl-source:42
    قيمة = 1000000000
    # apl-source:43
    for م in ذات.ع:
      # apl-source:44
      if ذات.ع[م] < قيمة:
        # apl-source:45
        قيمة = ذات.ع[م]
        # apl-source:46
        افضل = م
    # apl-source:47
    return افضل
# apl-source:48

# apl-source:49
ع = عدادات()
# apl-source:50
ع.زد("a")
# apl-source:51
ع.زد("b")
# apl-source:52
ع.زد("b")
# apl-source:53
تأكد_يساوي(ع.مفتاح_اكبر(), "b", "الأكبر")
# apl-source:54
تأكد_يساوي(ع.مفتاح_اصغر(), "a", "الأصغر")
# apl-source:55
ع.انقص("b")
# apl-source:56
ع.انقص("b")
# apl-source:57
تأكد_يساوي(ع.مفتاح_اكبر(), "a", "بعد الحذف")
# apl-source:58
ع.انقص("a")
# apl-source:59
تأكد_يساوي(ع.مفتاح_اكبر(), "", "فارغ")
# apl-source:60
