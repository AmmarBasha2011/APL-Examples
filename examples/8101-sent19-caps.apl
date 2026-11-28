# مثال 8101 — أول حرف كبير لكل كلمة في الجملة رقم 20
# caps for sentence 20
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8101-sent19-caps.apl

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

تأكد_يساوي(ف("yes no yes yes no maybe"), "Yes No Yes Yes No Maybe", "حالة 1")
تأكد_يساوي(ف("apl code is easy code is fun"), "Apl Code Is Easy Code Is Fun", "حالة 2")
تأكد_يساوي(ف("tea for two and two for tea"), "Tea For Two And Two For Tea", "حالة 3")
