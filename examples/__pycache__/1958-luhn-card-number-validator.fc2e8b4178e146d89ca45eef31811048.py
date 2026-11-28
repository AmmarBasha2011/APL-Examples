
# apl-source:1
# مثال 1958 — التحقق من رقم البطاقة بخوارزمية لون
# apl-source:2
# Luhn card validator
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1958-luhn-card-number-validator.apl
# apl-source:6

# apl-source:7
# # إن زاد الرقم المضاعف على 9 نطرح منه 9
# apl-source:8
# # الرقم صحيح إذا كان المجموع من مضاعفات عشرة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def لون(س):
  # apl-source:19
  مج = 0
  # apl-source:20
  ثاني = False
  # apl-source:21
  for ك in range(len(س)):
    # apl-source:22
    ر = int(س[len(س) - 1 - ك])
    # apl-source:23
    if ثاني:
      # apl-source:24
      ر = ر * 2
      # apl-source:25
      if ر > 9:
        # apl-source:26
        ر = ر - 9
    # apl-source:27
    مج = مج + ر
    # apl-source:28
    ثاني = ثاني == False
  # apl-source:29
  return مج % 10 == 0
# apl-source:30

# apl-source:31
تأكد_يساوي(لون("4539578763621486"), True, "صحيح")
# apl-source:32
تأكد_يساوي(لون("4539578763621487"), False, "خاطئ")
# apl-source:33
تأكد_يساوي(لون("79927398713"), True, "مثال ويكيبيديا")
# apl-source:34
