import Tricrypt
# license/copyright block here

def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("service", help="a service name stored in the conf file.")
    parser.add_argument("-x", "--xml", help="enable xml output", action="store_true")
    parser.add_argument("-l", "--length", help="code length", type=int, default=6)
    parser.add_argument("--settings-file", help="Alternate Settings File", default="Tricrypt.yml")
    args = parser.parse_args()
    
    s = Settings()
    s.importYamlFile(args.settings_file)
    
    if args.service in s.sites:
        totp = otp.otp(s.sites[args.service], args.length) # clean this up
        print Tricrypt(totp, args, s) # make this better, pass settings and shapes, and python3


if __name__=="__main__":
    main()