from gmail import GMail, Message

from random import choice

gmail = GMail('phphuong0912@gmail.com','haizz123')

html_content = """
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy, em t&ecirc;n l&agrave; Phạm Ho&agrave;ng Phương</p>
<p style="text-align: left;">H&ocirc;m nay em viết email xin nghỉ n&agrave;y để {{sickness}} &nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-smile.gif" alt="smile" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Em xin cảm ơn</p>
<p style="text-align: left;">Phương.</p>"""

reasons = ["Ốm", "Đau bụng", "Gấu dỗi"]

rand_reason = choice(reasons)

html_to_send = html_content.replace("{{sickness}}", rand_reason)

msg = Message('hi there', to='phuong.pham@ematicsolutions.com', html=html_content)
gmail.send(msg)