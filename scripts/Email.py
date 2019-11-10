import yagmail


class Email:

    def __init__(self):
        """Setup"""

        import json

        with open('config.json', 'r') as f:
            config = json.load(f)

        self.my_email = config['EMAIL']['MYEMAIL']
        self.password = config['EMAIL']['APP_PASSWORD']

    def Send(self, subject, body, attach=False):

        receiver = self.my_email
        password = self.password

        if attach:
            filename = "app.log"
        else:
            filename = None

        try:
            yag = yagmail.SMTP(self.my_email, self.password)
            yag.send(
                to=receiver,
                subject=subject,
                contents=body,
                attachments=filename,
            )
        except:
            raise
