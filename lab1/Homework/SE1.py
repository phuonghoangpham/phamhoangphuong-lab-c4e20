from gmail import GMail, Message

from random import choice

import datetime

gmail = GMail('phphuong0912@gmail.com','haizz123')

html_content = """
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy, em t&ecirc;n l&agrave; Phạm Ho&agrave;ng Phương</p>
<p style="text-align: left;">H&ocirc;m nay bị ốm n&ecirc;n em xin nghỉ v&igrave; l&yacute; do {{sickness}}</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Em xin cảm ơn,</p>
<p style="text-align: left;">Phương.</p>"""

reasons = ["Ốm", "Đau bụng", "Gấu dỗi"]

html_to_send = html_content.replace("{{sickness}}", choice(reasons))

msg = Message ("Đơn xin nghỉ", to="phuong.pham@ematicsolutions.com", html=html_to_send)

while True:
    from datetime import *
    now = datetime.now()
    hour_now = now.time()

    if hour_now >= 00:00 :
        gmail.send(msg) 
        break 

