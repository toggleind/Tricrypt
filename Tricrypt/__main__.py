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
    
    s = Tricrypt.Settings()
    s.importYamlFile(args.settings_file)
    
    try:
        service_name = s.sites[args.service]
        totp = Tricrypt.otp(service_name, s.pin_length) # clean this up
        print Tricrypt.Tricrypt(totp, service_name, s) # make this better, pass settings and shapes, and python3
    except KeyError as e:
        print "'{}' is not a defined service.".format(e.message)
        print "Please update your conf file if needed.\n"

if __name__=="__main__":
    main()