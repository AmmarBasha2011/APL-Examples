
# apl-source:1
# مثال 590 — معادلة ديوفانتية
# apl-source:2
# Linear Diophantine equation
# apl-source:3
# Demonstrates: ديوفانتية، إقليدس موسعة، تحقق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/590-linear-diophantine.apl
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
# حل معادلة ديوفانتية خطية: أ س + ب ص = ج
# apl-source:25
# Demonstrates: خوارزمية إقليدس الموسعة, التحقق من الحل بالتعويض
# apl-source:26
# الحل موجود فقط إذا كان ج مضاعفا للقاسم المشترك الأكبر
# apl-source:27

# apl-source:28
def إقليدس_موسع(أ, ب):
  # apl-source:29
  if ب == 0:
    # apl-source:30
    return [أ, 1, 0]
  # apl-source:31
  نتيجة = إقليدس_موسع(ب, أ % ب)
  # apl-source:32
  ق = نتيجة[0]
  # apl-source:33
  س1 = نتيجة[2]
  # apl-source:34
  ص1 = نتيجة[1] - (أ // ب) * نتيجة[2]
  # apl-source:35
  return [ق, س1, ص1]
# apl-source:36

# apl-source:37
def حل_ديوفانتي(أ, ب, ج):
  # apl-source:38
  نتيجة = إقليدس_موسع(أ, ب)
  # apl-source:39
  ق = نتيجة[0]
  # apl-source:40
  if ج % ق != 0:
    # apl-source:41
    return []
  # apl-source:42
  مقياس = ج // ق
  # apl-source:43
  return [نتيجة[1] * مقياس, نتيجة[2] * مقياس]
# apl-source:44

# apl-source:45
حل = حل_ديوفانتي(35, 15, 5)
# apl-source:46
print("الحل:", حل)
# apl-source:47
تأكد_يساوي(len(حل), 2, "يوجد حل")
# apl-source:48
تأكد_يساوي(35 * حل[0] + 15 * حل[1], 5, "التحقق بالتعويض")
# apl-source:49
تأكد_يساوي(len(حل_ديوفانتي(6, 9, 5)), 0, "لا حل عندما لا يقسم القاسم")
# apl-source:50
حل2 = حل_ديوفانتي(6, 9, 12)
# apl-source:51
تأكد_يساوي(6 * حل2[0] + 9 * حل2[1], 12, "حل ثان بالتعويض")
# apl-source:52
