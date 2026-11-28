# مثال 6436 — العدد: الكلمات التي تبدأ بـ t ثم (أول حرف كبير)
# count of cap over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6436-words-starts_t-cap-count.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: العدد

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
    لو ك[0] == "t":
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع len(ر)

تأكد_يساوي(ف("the cat sat on the mat"), 2, "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), 0, "حالة 2")
تأكد_يساوي(ف("one two three four five six"), 2, "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), 0, "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), 4, "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), 0, "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), 3, "حالة 7")
تأكد_يساوي(ف("hello"), 0, "حالة 8")
