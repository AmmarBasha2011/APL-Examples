
# apl-source:1
# مثال 614 — ناقل أحداث
# apl-source:2
# Event bus
# apl-source:3
# Demonstrates: نشر واشتراك، معالجات، أحداث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/614-event-bus.apl
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
# ناقل أحداث: نشر واشتراك بين مكونات منفصلة
# apl-source:25
# Demonstrates: معالجات لكل حدث, حمولة, فصل المرسل عن المستقبل
# apl-source:26
# أساس بنية الأنظمة الموجهة بالأحداث
# apl-source:27

# apl-source:28
def أنشئ_ناقل():
  # apl-source:29
  return {"معالجات": {}, "سجل": []}
# apl-source:30

# apl-source:31
def اشترك(ناقل, حدث, معالج):
  # apl-source:32
  if حدث in ناقل["معالجات"]:
    # apl-source:33
    ناقل["معالجات"][حدث].append(معالج)
  # apl-source:34
  else:
    # apl-source:35
    ناقل["معالجات"][حدث] = [معالج]
# apl-source:36

# apl-source:37
def انشر(ناقل, حدث, حمولة):
  # apl-source:38
  ناقل["سجل"].append(حدث)
  # apl-source:39
  if حدث in ناقل["معالجات"]:
    # apl-source:40
    for معالج in ناقل["معالجات"][حدث]:
      # apl-source:41
      معالج(حمولة)
# apl-source:42

# apl-source:43
وصلت = []
# apl-source:44
def عالج_الطلب(حمولة):
  # apl-source:45
  وصلت.append("طلب:" + حمولة)
# apl-source:46

# apl-source:47
def عالج_الدفع(حمولة):
  # apl-source:48
  وصلت.append("دفع:" + حمولة)
# apl-source:49

# apl-source:50
ناقل = أنشئ_ناقل()
# apl-source:51
اشترك(ناقل, "طلب_جديد", عالج_الطلب)
# apl-source:52
اشترك(ناقل, "دفع_تم", عالج_الدفع)
# apl-source:53
اشترك(ناقل, "طلب_جديد", عالج_الدفع)
# apl-source:54
انشر(ناقل, "طلب_جديد", "٤٢")
# apl-source:55
انشر(ناقل, "دفع_تم", "٩٩")
# apl-source:56
انشر(ناقل, "بدون_مشتركين", "س")
# apl-source:57
print("الوارد:", وصلت)
# apl-source:58
تأكد_يساوي(len(وصلت), 3, "ثلاث رسائل وصلت")
# apl-source:59
تأكد_يساوي(وصلت[0], "طلب:٤٢", "معالج الطلب أولا")
# apl-source:60
تأكد_يساوي(وصلت[1], "دفع:٤٢", "معالج ثان على نفس الحدث")
# apl-source:61
تأكد_يساوي(len(ناقل["سجل"]), 3, "السجل يحفظ حتى بلا مشتركين")
# apl-source:62
