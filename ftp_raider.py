import ftplib
from threading import Thread

fx = open(r'text_file', "w")

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('host', 'anonymous', 'me@me.com', 'frr')
        print('\n [+]' + str(hostname) + ' FTP anonymous logon succeeded')
        scn_text1 = ""
        fx.write(scn_text1)
        # fx.close()
        ftp.quit()
        return True
    except:
        print('\n [+]' + str(hostname) + ' FTP anonymous logon failed')
        scn_text1 = ""
        fx.write(scn_text1)
        # fx.close()
        return False


def main():
    # range2 = ['']
    class_C_IP = '192.168.0.'

    for i in range(1, 256, 1):
        current_IP = str(class_C_IP) + str(i)
        print('Scanning FTP port on IP ' + current_IP)
        scn_text2 = ""
        scn_text2 += "Scanning FTP port on IP " + str(current_IP) + "\n"

        t = Thread(target=anonLogin, args=(i, ))
        t.start()

        print('\n\n' + '#'*32 + '\n')
        fx.write(scn_text2)

if __name__ == '__main__':
    main()
    fx.close()
