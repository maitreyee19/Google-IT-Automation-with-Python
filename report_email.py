#!/usr/bin/env python3

import json
import locale
import os
import sys
import reports_new
import emails
from datetime import datetime
from os.path import isfile, join
def main(argv):
    """Process the JSON data and generate a full report out of it."""
    inPath = "/home/bhabani/Work/googleITAutomation/Week4/descriptions/"
    textfiles = [f for f in os.listdir(inPath) if isfile(join(inPath, f))]
    fruitDetails = []
    for file in textfiles:
        descForFruit = {}

        with open(join(inPath, file), 'r') as f:
            Lines = f.readlines()
            descForFruit["name"] = Lines[0].rstrip()
            descForFruit["weight"] = Lines[1].rstrip("\n")
            for k, v in descForFruit.items():
                fruitDetails.append([k, v])
            fruitDetails.append(["", ""])

    date_time = datetime.now()

    dateInfo = date_time.strftime("%B %d, %Y")

    reportHeading = "processed Update on " + dateInfo

    reports_new.generate("/tmp/processed.pdf", reportHeading, fruitDetails)

    # TODO: send the PDF report as an email attachment

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    summary ="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    body = "\n".join(summary)

    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")

    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
