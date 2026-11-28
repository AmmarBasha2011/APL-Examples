
# apl-source:1
# مثال 657 — أوتومات اللواحق
# apl-source:2
# Suffix automaton
# apl-source:3
# Demonstrates: لواحق، حالات، روابط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/657-suffix-automaton.apl
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
# أوتومات اللواحق: بنية نصية مدمجة
# apl-source:25
# Demonstrates: حالات وروابط لاحقة, استنساخ, فحص وجود نص فرعي
# apl-source:26
# كل النصوص الفرعية في بنية خطية الحجم
# apl-source:27

# apl-source:28
def حالة_جديدة(طول_أقصى, رابط):
  # apl-source:29
  return {"طول": طول_أقصى, "رابط": رابط, "انتقالات": {}}
# apl-source:30

# apl-source:31
def ابن(نص):
  # apl-source:32
  حالات = [حالة_جديدة(0, -1)]
  # apl-source:33
  آخر = 0
  # apl-source:34
  for حرف in نص:
    # apl-source:35
    حالات.append(حالة_جديدة(حالات[آخر]["طول"] + 1, 0))
    # apl-source:36
    جديد = len(حالات) - 1
    # apl-source:37
    ع = آخر
    # apl-source:38
    while ع != -1 and حالات[ع]["انتقالات"].get(حرف, None) == None:
      # apl-source:39
      حالات[ع]["انتقالات"][حرف] = جديد
      # apl-source:40
      ع = حالات[ع]["رابط"]
    # apl-source:41
    if ع == -1:
      # apl-source:42
      حالات[جديد]["رابط"] = 0
    # apl-source:43
    else:
      # apl-source:44
      ت = حالات[ع]["انتقالات"][حرف]
      # apl-source:45
      if حالات[ع]["طول"] + 1 == حالات[ت]["طول"]:
        # apl-source:46
        حالات[جديد]["رابط"] = ت
      # apl-source:47
      else:
        # apl-source:48
        نسخة = {"طول": حالات[ع]["طول"] + 1, "رابط": حالات[ت]["رابط"], "انتقالات": حالات[ت]["انتقالات"].copy()}
        # apl-source:49
        حالات.append(نسخة)
        # apl-source:50
        رقم_نسخة = len(حالات) - 1
        # apl-source:51
        while ع != -1 and حالات[ع]["انتقالات"].get(حرف, None) == ت:
          # apl-source:52
          حالات[ع]["انتقالات"][حرف] = رقم_نسخة
          # apl-source:53
          ع = حالات[ع]["رابط"]
        # apl-source:54
        حالات[ت]["رابط"] = رقم_نسخة
        # apl-source:55
        حالات[جديد]["رابط"] = رقم_نسخة
    # apl-source:56
    آخر = جديد
  # apl-source:57
  return حالات
# apl-source:58

# apl-source:59
def موجود(حالات, نمط):
  # apl-source:60
  ع = 0
  # apl-source:61
  for حرف in نمط:
    # apl-source:62
    تالي = حالات[ع]["انتقالات"].get(حرف, None)
    # apl-source:63
    if تالي == None:
      # apl-source:64
      return False
    # apl-source:65
    ع = تالي
  # apl-source:66
  return True
# apl-source:67

# apl-source:68
حالات = ابن("abbc")
# apl-source:69
تأكد_يساوي(موجود(حالات, "abb"), True, "abb موجود")
# apl-source:70
تأكد_يساوي(موجود(حالات, "bbc"), True, "bbc موجود")
# apl-source:71
تأكد_يساوي(موجود(حالات, "b"), True, "b موجود")
# apl-source:72
تأكد_يساوي(موجود(حالات, "acb"), False, "acb مفقود")
# apl-source:73
تأكد_يساوي(موجود(حالات, "ba"), False, "ba مفقود")
# apl-source:74
تأكد_يساوي(موجود(حالات, "abbc"), True, "النص كله موجود")
# apl-source:75
print("عدد الحالات:", len(حالات))
# apl-source:76
