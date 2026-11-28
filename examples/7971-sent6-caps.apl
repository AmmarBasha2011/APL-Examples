# مثال 7971 — أول حرف كبير لكل كلمة في الجملة رقم 7
# caps for sentence 7
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7971-sent6-caps.apl

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

تأكد_يساوي(ف("tea for two and two for tea"), "Tea For Two And Two For Tea", "حالة 1")
تأكد_يساوي(ف("in the end the end is the start"), "In The End The End Is The Start", "حالة 2")
تأكد_يساوي(ف("nile river nile delta river"), "Nile River Nile Delta River", "حالة 3")
