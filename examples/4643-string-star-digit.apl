# مثال 4643 — استبدال بنجمة (رقم) في نص
# String: replace with star digit
# Demonstrates: نصوص وحلقات وشروط
#
# Run:  python apl.py examples/4643-string-star-digit.apl

# نمرّ على حروف النص واحدًا واحدًا
# ونطبّق الشرط على كل حرف

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(س):
  ن = ""
  لكل خ في س:
    لو خ.isdigit():
      ن = ن + "*"
    والا:
      ن = ن + خ
  ارجع ن

تأكد_يساوي(ف("apple PIE 7 and 9"), "apple PIE * and *", "حالة 1")
تأكد_يساوي(ف("ZZtop and the Beatles"), "ZZtop and the Beatles", "حالة 2")
تأكد_يساوي(ف("quick brown fox"), "quick brown fox", "حالة 3")
تأكد_يساوي(ف("Data Science 101"), "Data Science ***", "حالة 4")
تأكد_يساوي(ف(""), "", "حالة 5")
