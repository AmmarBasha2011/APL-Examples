
# apl-source:1
# مثال 1319 — إضافة عمليات
# apl-source:2
# Expression add operators
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1319-expression-add-operators.apl
# apl-source:6

# apl-source:7
# نجرب بين كل رقمين جمعاً أو طرحاً أو ضرباً أو لصقاً
# apl-source:8
# ونحسب القيمة بحذر في الضرب
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
def عبارات(ارقام, هدف):
  # apl-source:19
  ناتج = []
  # apl-source:20
  مكدس = []
  # apl-source:21
  for ط in range(1, len(ارقام) + 1):
    # apl-source:22
    اول = ارقام[:ط]
    # apl-source:23
    if (len(اول) == 1) or (اول[0] != "0"):
      # apl-source:24
      مكدس = مكدس + [[ط, اول, int(اول), int(اول)]]
  # apl-source:25
  while len(مكدس) > 0:
    # apl-source:26
    ح = مكدس.pop()
    # apl-source:27
    ع = ح[0]
    # apl-source:28
    نص_ = ح[1]
    # apl-source:29
    قيمة = ح[2]
    # apl-source:30
    اخير = ح[3]
    # apl-source:31
    if ع == len(ارقام):
      # apl-source:32
      if قيمة == هدف:
        # apl-source:33
        ناتج = ناتج + [نص_]
    # apl-source:34
    else:
      # apl-source:35
      for ط in range(ع + 1, len(ارقام) + 1):
        # apl-source:36
        جزء = ارقام[ع:ط]
        # apl-source:37
        if (len(جزء) > 1) and (جزء[0] == "0"):
          # apl-source:38
          تجاهل = 0
        # apl-source:39
        else:
          # apl-source:40
          ق = int(جزء)
          # apl-source:41
          مكدس = مكدس + [[ط, نص_ + "+" + جزء, قيمة + ق, ق]]
          # apl-source:42
          مكدس = مكدس + [[ط, نص_ + "-" + جزء, قيمة - ق, -ق]]
          # apl-source:43
          مكدس = مكدس + [[ط, نص_ + "*" + جزء, قيمة - اخير + اخير * ق, اخير * ق]]
  # apl-source:44
  return sorted(ناتج)
# apl-source:45

# apl-source:46
تأكد_يساوي(عبارات("123", 6), ["1*2*3", "1+2+3"], "ستة")
# apl-source:47
تأكد_يساوي(عبارات("232", 8), ["2*3+2", "2+3*2"], "ثمانية")
# apl-source:48
تأكد_يساوي(عبارات("105", 5), ["1*0+5", "10-5"], "أصفار")
# apl-source:49
تأكد_يساوي(عبارات("00", 0), ["0*0", "0+0", "0-0"], "أصفار فقط")
# apl-source:50
تأكد_يساوي(عبارات("12", 100), [], "لا حل")
# apl-source:51
