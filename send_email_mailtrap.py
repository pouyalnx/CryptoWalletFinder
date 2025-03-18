import mailtrap as mt

# create mail object
mail = mt.Mail(
    sender=mt.Address(email="poyalnx@poyalnx.com", name="Mailtrap Test"),
    to=[mt.Address(email="pouyalnx@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
)


client = mt.MailtrapClient(token="272863ac4b088996a77d37c4b5a8990e")
client.send(mail)

lu*dvmg08[q7UWil

sudo apt install libgmp-dev
sudo apt install python3.10-full
sudo apt install build-essential
sudo apt install gcc
sudo apt install libpq-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev libjpeg-dev zlib1g-dev
