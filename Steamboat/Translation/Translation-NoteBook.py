# -*- coding: utf-8 -*-
# @Time     :   2020/3/25 5:41
# @Author   :   Payne
# @File     :   Translation-NoteBook.py
# @Software :   PyCharm


import random
from time import time

'''
i: 编程
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15850823623239
sign: f10cce5f60d121d0685574dfff6d3d9f
ts: 1585082362323
bv: 70244e0061db49a9ee62d341c5fed82a
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''

'''
        i = n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bbk/translate_m.do",
            data: {
                i: e.i,
                client: e.client,
                salt: a.salt,
                sign: a.sign,
                ts: a.ts,
                bv: a.bv,
                tgt: e.tgt,
                from: e.from,
                to: e.to,
                doctype: "json",
                version: "3.0",
                cache: !0
            },
            dataType: "json",
            success: function(t) {
                t && 0 == t.errorCode ? e.success && e.success(t) : e.error && e.error(t)
            },
            error: function(e) {}
        })
    }
}),
'''


# ts = round(time())
# salt = str(random.randint(0, 9)) + str(ts)
# print(salt)


a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
print(a.strip('/')[0::])