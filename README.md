# Tricrypt

Obfuscated 2FA to protect codes in sensitive situations

Tricrypt is a Two factor authentication tool designed to make shoulder surfing
just a little bit harder. Current applications like Authy, google Authenticator,
Microsoft Authenticator, etc. all display codes in the clear. This is the
easiest to read, and mostly secure. But if your phone is stolen, or you are
logging in at a public place like an airport where you are concerned about
people shoulder surfing the codes, then it may not be enough.

Tricrypt uses a pattern to hide the OTP code, providing that little extra
security for the most sensitive situations, or just the most paranoid of users.

Intrigued? then lets get started.

## Installing
`pip install Tricrypt`
It's that easy.

## Configuring
This is currently not as easy as it should be, so for brevity, you can read
about that in [CONFIGURING.MD](configuring.md)

## Running
If you have successfully configured Tricrypt, then running is a breeze.

`tricrypt <service_name>`

It's that easy!