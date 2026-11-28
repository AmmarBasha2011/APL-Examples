# مثال 8091 — أول حرف كبير لكل كلمة في الجملة رقم 19
# caps for sentence 19
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8091-sent18-caps.apl

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

تأكد_يساوي(ف("left right left left right"), "Left Right Left Left Right", "حالة 1")
تأكد_يساوي(ف("to be or not to be"), "To Be Or Not To Be", "حالة 2")
تأكد_يساوي(ف("we love data and data loves us"), "We Love Data And Data Loves Us", "حالة 3")
