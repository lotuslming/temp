import email
import os
def parse_email(file_name):
    fp=open(file_name,'r')
    msg=email.message_from_file(fp)
    subject=msg.get('subject')
    h=email.Header.Header(subject)
    dh=email.Header.decode_header(h)
    subject=dh[0][0]
    print 'subject:',subject
    print 'from:',email.utils.parseaddr(msg.get("from"))[1]
    print 'to:',email.utils.parseaddr(msg.get("to"))[1]

    for par in msg.walk():
        if not par.is_multipart():
            name=par.get_param("name")
            if name:
                h=email.Header.Header(name)
                dh=email.Header.decode_header(h)
                fname=dh[0][0]
                print 'Attach:',fname
                data=par.get_payload(decode=True)
                try:
                    f=open(fname,'wb')
                except:
                    print "invaild file name"
                    f=open("temp",'wb')
                f.write(data)
                f.close()
            else:
                print par.get_payload(decode=True)
            print '+'*60
    fp.close()

def get_file_extension(file_name):
    file_extension=os.path.splitext(file_name)[1]
    return file_extension

def get_through_dir(root_dir):
    list_dir=os.listdir(root_dir)
    #print len(list_dir)
    for i in range(0,len(list_dir)):
        path=os.path.join(root_dir,list_dir[i])
        if os.path.isfile(path) and get_file_extension(path)=='.eml':
            parse_email(path)
    
def main():
    root_dir=raw_input()
    root_dir=root_dir.replace('\\','/')
    #print root_dir
    get_through_dir(root_dir)
    
if __name__=='__main__':
    main()
