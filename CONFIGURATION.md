# Configuration

A Tricrypt.yml file was created during installation.
This is the global configuration, and any OTP Secrets stored here will be used
and visible by everyone. Therefor, it is recommended to copy this file to your
home folder. You can also supply a custom config from anywhere on the command 
line.

Editing this file, you will see several fields. Lets break those down.

### pattern
This is the pattern that will be used to hide all of your codes.
It can be any length you want. Patterns shorter than the pin length will be
repeated until the pin length has been met. For example:

|Patttern   | pin length | Final Pattern   |
|:----------|:----------:|:----------------|
| S S T C   |     6      | S S T C S S     |
| C S       |     6      | C S C S C S     |
| S T T T C |     8      | S T T T C S T T |
| T         |    104     | T T T T T T ... |

make sense?

The pattern can be specified one of 3 ways:

```
pattern: 'SSTC'
```

```
pattern: ['S', 'S', 'T', 'C']
```

```
pattern:
	- 'S'
	- 'S'
	- 'T'
	- 'C'
```
The second is recommended, as it is the most clear, space efficent, and 
all future changes will support this format.

### pin_length
Almost all services will expect codes 6 or 8 characters long (like 006321 or 46523546).
Tricrypt will make an A x B sized grid, where A is the number of unique shapes 
(currently 4) and B is pin_length! To avoid creating a 4x10,000 grid, 
I recommend leaving this at 6 unless you need longer codes.

### output
This is the magic. 
Currently supported values are:
- plain
- xml
- html

But you can specify your own if you write your own format.
Support for other formats may be implemented if there is demand.

### sites
This holds all the `<service_name>: 'SECRETKEY'` pairs.

The service name is arbitrary, and can be whatever you want. No testing has
been done with non ASCII names. If your Cyrillic, or emojis, or umlauts dont work,
please sumbit an issue on GitHub, but I make no promises.

The 'SECRETKEY' portion is a base32 encoded string, usually 16 characters, 
provided by your service. This can usually be found in your services' 
`Settings > Security > 2FA` or something of the like. If your service provides
something other than a base32 string, or your secret doesn't work, please 
submit an issue.