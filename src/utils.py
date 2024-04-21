import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "vijender.in@gmail.com"
password = "jxgfjvrayihbjooe"

def send_new_post(receiver_emails, article_id):
    article_url = f"http://localhost:3000/articles/{article_id}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            # Send email to each recipient
            for i in receiver_emails:
                # Create a new MIMEMultipart message for each recipient
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = i  # Set the recipient
                message["Subject"] = "New Post Alert !!!"

                body = f"""
                       Hello,
                       
                       New Post Created from. !!!
                       
                       Click below to view the post.
                       
                       {article_url}
                       
                       Regards,
                       BQP
                """
                message.attach(MIMEText(body, "plain"))
                text = message.as_string()
                
                server.sendmail(sender_email, i, text)
                print(f"Email sent successfully to {i}!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def send_new_comment(receiver_emails, article_id):
    article_url = f"http://localhost:3000/articles/{article_id}"
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Set up the SMTP server connection
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, password)
    except Exception as e:
        print(f"Failed to connect or log in to the SMTP server: {e}")
        return

    # Send email to each recipient
    for receiver_email in receiver_emails:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "New Comment Alert !!!"

        body = f"""
               Hello,
               
               A new comment has been created! Check it out.
               {article_url}
               Regards,
               BQP
               """
        message.attach(MIMEText(body, "plain"))

        try:
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"Email sent successfully to {receiver_email}!")
        except Exception as e:
            print(f"An error occurred while sending email to {receiver_email}: {e}")

    # Close the server connection
    server.quit()
