# مثال 7931 — أول حرف كبير لكل كلمة في الجملة رقم 3
# caps for sentence 3
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7931-sent2-caps.apl

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

تأكد_يساوي(ف("apl code is easy code is fun"), "Apl Code Is Easy Code Is Fun", "حالة 1")
تأكد_يساوي(ف("we love data and data loves us"), "We Love Data And Data Loves Us", "حالة 2")
تأكد_يساوي(ف("in the end the end is the start"), "In The End The End Is The Start", "حالة 3")
