import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, to_email, subject, body, attachment_path=None):
    # 配置邮件服务器
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    # 配置邮件内容
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # 添加邮件正文
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # 添加附件（如果有）
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            attachment_part = MIMEApplication(attachment.read())
            attachment_part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
            message.attach(attachment_part)

    try:
        # 连接到 SMTP 服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 开启 TLS 加密

        # 登录邮箱
        server.login(sender_email, sender_password)

        # 发送邮件
        server.sendmail(sender_email, to_email, message.as_string())

        print("邮件发送成功！")

    except Exception as e:
        print(f"邮件发送失败：{e}")

    finally:
        # 关闭连接
        server.quit()

if __name__ == "__main__":
    # 替换为您的 Gmail 邮箱和密码
    sender_email = "ykntest01@outlook.com"
    sender_password = "Asdfzxcv1234"

    # 替换为收件人的邮箱地址
    to_email = "420610383@qq.com"

    # 邮件主题和内容
    email_subject = "测试邮件"
    email_body = "这是一封测试邮件。"

    # 如果有附件，请提供附件路径；否则，将 attachment_path 设置为 None
    attachment_path = None

    # 调用发送邮件函数
    send_email(sender_email, sender_password, to_email, email_subject, email_body, attachment_path)
