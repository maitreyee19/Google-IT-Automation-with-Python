#!/usr/bin/env python3
import shutil
import psutil
import emails
import time
import os


def subjectlineGeneration(issueNo):
    if issueNo ==1:
        return "Error - CPU usage is over 80%"
    elif issueNo ==2 :
        return "Error - Available disk space is less than 20%"
    elif issueNo ==3:
        return "Error - Available memory is less than 500MB"
    elif issueNo ==4:
        return "Error - localhost cannot be resolved to 127.0.0.1"
    else:
        return "New error found"

def systemCheck():
    issueNo =0
    cpu_usage = psutil.cpu_percent()
    #print(cpu_usage)
    if cpu_usage > 80.0:
        issueNo = 1

    total, used, free = shutil.disk_usage("/")
    if (free*100 / total) <20:
        issueNo =2
    netAdress = psutil.net_if_addrs()
    if (netAdress["lo"][0].address) != "127.0.0.1":
        issueNo =4

    memory_info = dict(psutil.virtual_memory()._asdict())
    availabe_memory =memory_info["available"]/(1024*1024)
    if availabe_memory <500:
        issueNo =3
    #print(availabe_memory)

    return issueNo


def main( ):
    # TODO: send the PDF report as an email attachment
    while True:

        issue_no = systemCheck()
        if issue_no >0 :
            subject = subjectlineGeneration(issue_no)
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))

            summary = "Please check your system and resolve the issue as soon as possible."
            body = summary

            message = emails.emailWithoutAttachment(sender, receiver, subject, body)

            emails.send_email(message)
            time.sleep(60)



if __name__ == '__main__':
    main()