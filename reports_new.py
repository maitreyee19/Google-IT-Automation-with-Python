#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = ""
    report_table =Table(additional_info,hAlign='LEFT')
    print(report_table)

    #for data in additional_info:
     #   print("data:",data)

        # table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
        #                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        #                ('ALIGN', (0, 0), (-1, -1), 'CENTER')]
        # report_table = Table(data=data)
        # print(report_table)
        #report_info = report_info + Paragraph(report_table, styles["BodyText"]) + Spacer(1, 20)



    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_table, empty_line])
