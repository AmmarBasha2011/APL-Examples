
# apl-source:1
# مثال 753 — تشكيل الحروف العربية
# apl-source:2
# Arabic letter reshaping
# apl-source:3
# Demonstrates: أشكال عرض، اتصال قبلي وبعدي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/753-arabic-reshaper-lite.apl
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
# إعادة تشكيل الحروف العربية لأشكال العرض (presentation forms)
# apl-source:25
# Demonstrates: أربعة أشكال لكل حرف, اتصال قبلي وبعدي, الألف لا يتصل بعده
# apl-source:26
# الحروف المعزولة تحتاج شكلاً مختلفاً في العرض القديم للنص العربي
# apl-source:27

# apl-source:28
# كل حرف: [معزول, نهائي, أولي, أوسط] — الألف لا يتصل بما بعده
# apl-source:29
أشكال = {
  # apl-source:30
  "ا": ["ﺍ", "ﺎ", "", ""],
  # apl-source:31
  "ب": ["ﺏ", "ﺐ", "ﺑ", "ﺒ"],
  # apl-source:32
  "ت": ["ﺕ", "ﺖ", "ﺗ", "ﺘ"],
  # apl-source:33
  "م": ["ﻡ", "ﻢ", "ﻣ", "ﻤ"],
  # apl-source:34
  "ه": ["ﻩ", "ﻪ", "ﻫ", "ﻬ"],
  # apl-source:35
  "ي": ["ﻱ", "ﻲ", "ﻳ", "ﻴ"],
  # apl-source:36
  "ل": ["ﻝ", "ﻞ", "ﻟ", "ﻠ"],
  # apl-source:37
  "ن": ["ﻥ", "ﻦ", "ﻧ", "ﻨ"]
# apl-source:38
}
# apl-source:39

# apl-source:40
def يتصل_بعده(حرف):
  # apl-source:41
  أشكاله = أشكال.get(حرف, None)
  # apl-source:42
  if أشكاله == None:
    # apl-source:43
    return False
  # apl-source:44
  return أشكاله[2] != ""
# apl-source:45

# apl-source:46
def شكل(كلمة):
  # apl-source:47
  ناتج = ""
  # apl-source:48
  for ي in range(len(كلمة)):
    # apl-source:49
    حرف = كلمة[ي]
    # apl-source:50
    أشكاله = أشكال.get(حرف, None)
    # apl-source:51
    if أشكاله == None:
      # apl-source:52
      ناتج = ناتج + حرف
    # apl-source:53
    else:
      # apl-source:54
      قبلي = False
      # apl-source:55
      if ي > 0:
        # apl-source:56
        قبلي = يتصل_بعده(كلمة[ي - 1])
      # apl-source:57
      بعدي = False
      # apl-source:58
      if ي < len(كلمة) - 1:
        # apl-source:59
        بعدي = يتصل_بعده(حرف) and أشكال.get(كلمة[ي + 1], None) != None
      # apl-source:60
      if قبلي and بعدي:
        # apl-source:61
        ناتج = ناتج + أشكاله[3]
      # apl-source:62
      elif قبلي:
        # apl-source:63
        ناتج = ناتج + أشكاله[1]
      # apl-source:64
      elif بعدي:
        # apl-source:65
        ناتج = ناتج + أشكاله[2]
      # apl-source:66
      else:
        # apl-source:67
        ناتج = ناتج + أشكاله[0]
  # apl-source:68
  return ناتج
# apl-source:69

# apl-source:70
تأكد_يساوي(شكل("باب"), "ﺑﺎﺏ", "باب: أولي نهائي معزول")
# apl-source:71
تأكد_يساوي(شكل("بيت"), "ﺑﻴﺖ", "بيت: أولي أوسط نهائي")
# apl-source:72
تأكد_يساوي(شكل("ب"), "ﺏ", "حرف وحيد معزول")
# apl-source:73
تأكد_يساوي(شكل("ممتاز"), "ﻣﻤﺘﺎز", "ممتاز مع حرف ز غير مغطى")
# apl-source:74
تأكد_يساوي(شكل("ليل"), "ﻟﻴﻞ", "ليل: أولي أوسط نهائي")
# apl-source:75
تأكد_يساوي(شكل("اب"), "ﺍﺏ", "الألف يقطع الاتصال")
# apl-source:76

# apl-source:77
print("بيت ←", شكل("بيت"))
# apl-source:78
