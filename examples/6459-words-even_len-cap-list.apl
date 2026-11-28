# مثال 6459 — قائمة: الكلمات ذات الطول الزوجي ثم (أول حرف كبير)
# list of cap over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6459-words-even_len-cap-list.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: قائمة

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["On"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["Code", "Simple"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Four", "Five"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["Bb", "Dddd"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["To", "Be", "Or", "To", "Be", "That", "Is", "Question"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Data", "Data", "Data", "Code", "Code"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["Learning", "To", "Is", "Learning", "To"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
