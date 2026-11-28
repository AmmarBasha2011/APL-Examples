# مثال 8061 — أول حرف كبير لكل كلمة في الجملة رقم 16
# caps for sentence 16
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8061-sent15-caps.apl

# نقسم الجملة إلى كلمات
# ونعالجها حسب المطلوب

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    ر = ر + [ك[0].upper() + ك[1:]]
  ارجع " ".join(ر)

تأكد_يساوي(ف("stars and moon and stars again"), "Stars And Moon And Stars Again", "حالة 1")
تأكد_يساوي(ف("left right left left right"), "Left Right Left Left Right", "حالة 2")
تأكد_يساوي(ف("apl code is easy code is fun"), "Apl Code Is Easy Code Is Fun", "حالة 3")
