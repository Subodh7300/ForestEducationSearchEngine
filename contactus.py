import requests

EMAIL = "s.subodh7976@gmail.com"
API = "7cc9a383efmshef7c0e439566187p1daf4djsn858181172c55"
VALUE = "we received your response and will try to solve respond to your query as soon as possible and also thankful " \
        "for you to contact us.\n\n\nThe recorded query is---\n\n"
HOST = "rapidprod-sendgrid-v1.p.rapidapi.com"


class ContactUs:
    def __init__(self, to: str, des: str, name: str):
        self.url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
        self.to = to
        self.payload = {
            "personalizations": [
                {
                    "to": [{"email": self.to}],
                    "subject": "Auto-Generated Response"
                }
            ],
            "from": {"email": EMAIL},
            "content": [
                {
                    "type": "text/plain",
                    "value": f"Hello {name}, {VALUE} {des}"
                }
            ]
        }
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": API,
            "X-RapidAPI-Host": HOST
        }

    def send(self):
        response = requests.request('POST', self.url, json=self.payload, headers=self.headers)
        print(response.text)
        return response.status_code
