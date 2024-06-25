import imaplib
import email
from email.header import decode_header

def get_latest_email(email, password):
    # 连接到 QQ 邮箱的 IMAP 服务器
    mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)

    # 登录邮箱
    mail.login(email, password)

    # 选择收件箱
    mail.select(mailbox='INBOX', readonly=False)

    # 搜索最新的一封邮件
    status, messages = mail.search(None, "UNSEEN")

    if status == "OK":
        latest_mail_id = messages[0].split()[-1]  # 获取最新邮件的邮件号

        # 获取最新邮件的内容
        _, msg_data = mail.fetch(latest_mail_id, "(RFC822)")
        raw_email = msg_data[0][1]

        # 解析邮件
        try:
            msg = email.message_from_bytes(raw_email)
            subject, encoding = decode_header(msg["Subject"])[0]
            subject = subject.decode(encoding) if encoding else subject
            print(f"Subject: {subject}")
            # 遍历邮件的各个部分
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    # 获取纯文本部分的内容
                    body = part.get_payload(decode=True)
                    print(f"Body: {body}")
        except Exception as e:
            print("Error occurred while connecting to the mail server: ", str(e))

    # 关闭连接
    mail.close()
    mail.logout()

if __name__ == "__main__":
    # 替换为您的 QQ 邮箱和密码
    email = "ykntest01@outlook.com"
    password = "Asdfzxcv1234"

    # 调用获取最新邮件函数
    get_latest_email(email, password)