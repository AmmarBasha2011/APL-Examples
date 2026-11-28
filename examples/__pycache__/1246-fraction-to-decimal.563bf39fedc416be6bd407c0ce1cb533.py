
# apl-source:1
# مثال 1246 — كسر إلى عشري
# apl-source:2
# Fraction to recurring decimal
# apl-source:3
# Demonstrates: باقي مكرر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1246-fraction-to-decimal.apl
# apl-source:6

# apl-source:7
# نسجل موضع كل باقٍ ظهر
# apl-source:8
# وعند تكراره نضع القوس حول الدورة
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
def عشري(ب, م):
  # apl-source:19
  if ب == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  اشارة = ""
  # apl-source:22
  if (ب < 0) != (م < 0):
    # apl-source:23
    اشارة = "-"
  # apl-source:24
  ب = ب if ب > 0 else -ب
  # apl-source:25
  م = م if م > 0 else -م
  # apl-source:26
  ناتج = اشارة + str(ب // م)
  # apl-source:27
  باق = ب % م
  # apl-source:28
  if باق == 0:
    # apl-source:29
    return ناتج
  # apl-source:30
  ناتج = ناتج + "."
  # apl-source:31
  مواضع = {}
  # apl-source:32
  while باق != 0:
    # apl-source:33
    if باق in مواضع:
      # apl-source:34
      ي = مواضع[باق]
      # apl-source:35
      return ناتج[:ي] + "(" + ناتج[ي:] + ")"
    # apl-source:36
    مواضع[باق] = len(ناتج)
    # apl-source:37
    باق = باق * 10
    # apl-source:38
    ناتج = ناتج + str(باق // م)
    # apl-source:39
    باق = باق % م
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
تأكد_يساوي(عشري(1, 2), "0.5", "نصف")
# apl-source:43
تأكد_يساوي(عشري(2, 1), "2", "صحيح")
# apl-source:44
تأكد_يساوي(عشري(4, 333), "0.(012)", "دورة")
# apl-source:45
تأكد_يساوي(عشري(1, 6), "0.1(6)", "دورة متأخرة")
# apl-source:46
تأكد_يساوي(عشري(-50, 8), "-6.25", "سالب")
# apl-source:47
