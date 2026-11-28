
# apl-source:1
# مثال 1116 — نظام بنكي بسيط
# apl-source:2
# Simple bank system
# apl-source:3
# Demonstrates: التحقق قبل التنفيذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1116-bank-system.apl
# apl-source:6

# apl-source:7
# كل عملية تتحقق من وجود الحساب وكفاية الرصيد
# apl-source:8
# فلا تنفذ جزئياً أبداً
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
class بنك:
    # apl-source:19
    def __init__(ذات, ارصدة):
        # apl-source:20
        ذات.ارصدة = list(ارصدة)
# apl-source:21

    # apl-source:22
    def صالح(ذات, حساب):
        # apl-source:23
        return (حساب >= 1) and (حساب <= len(ذات.ارصدة))
# apl-source:24

    # apl-source:25
    def اودع(ذات, حساب, مبلغ):
        # apl-source:26
        if not ذات.صالح(حساب):
            # apl-source:27
            return False
        # apl-source:28
        ذات.ارصدة[حساب - 1] = ذات.ارصدة[حساب - 1] + مبلغ
        # apl-source:29
        return True
# apl-source:30

    # apl-source:31
    def اسحب_مبلغ(ذات, حساب, مبلغ):
        # apl-source:32
        if not ذات.صالح(حساب):
            # apl-source:33
            return False
        # apl-source:34
        if ذات.ارصدة[حساب - 1] < مبلغ:
            # apl-source:35
            return False
        # apl-source:36
        ذات.ارصدة[حساب - 1] = ذات.ارصدة[حساب - 1] - مبلغ
        # apl-source:37
        return True
# apl-source:38

    # apl-source:39
    def حول(ذات, من, الى, مبلغ):
        # apl-source:40
        ص1 = ذات.صالح(من)
        # apl-source:41
        ص2 = ذات.صالح(الى)
        # apl-source:42
        if not ص1:
            # apl-source:43
            return False
        # apl-source:44
        if not ص2:
            # apl-source:45
            return False
        # apl-source:46
        if not ذات.اسحب_مبلغ(من, مبلغ):
            # apl-source:47
            return False
        # apl-source:48
        ذات.اودع(الى, مبلغ)
        # apl-source:49
        return True
# apl-source:50

# apl-source:51
ب = بنك([10, 100, 20, 50, 30])
# apl-source:52
تأكد_يساوي(ب.اسحب_مبلغ(3, 10), True, "سحب ناجح")
# apl-source:53
تأكد_يساوي(ب.حول(5, 1, 20), True, "تحويل ناجح")
# apl-source:54
تأكد_يساوي(ب.اودع(5, 20), True, "إيداع")
# apl-source:55
تأكد_يساوي(ب.حول(3, 4, 15), False, "رصيد غير كاف")
# apl-source:56
تأكد_يساوي(ب.اسحب_مبلغ(10, 50), False, "حساب غير موجود")
# apl-source:57
تأكد_يساوي(ب.ارصدة, [30, 100, 10, 50, 30], "الأرصدة النهائية")
# apl-source:58
