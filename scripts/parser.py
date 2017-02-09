#! /usr/bin/env python
# -*- coding: utf-8 -*-
import scipy as sp
import xlrd
import csv
import os
from transliterate import translit, get_available_language_codes
from transliterate.contrib.apps.translipsum import TranslipsumGenerator

class parser:
    def __init__(self, xml_file, csv_out):
        self.xml = xml_file
        self.temp_csv = '../data/temp_csv.csv'
        self.temp_csv2 = '../data/temp_csv2.csv'
        self.csv_out = csv_out

    def xml_csv(self):
        filepath = '/home/ilya/parse'
        wb = xlrd.open_workbook(self.xml)
        sheet = wb.sheet_by_index(0)
        fp = open(self.temp_csv, 'wb')
        wr = csv.writer(fp, quoting=csv.QUOTE_ALL)
        for rownum in xrange(sheet.nrows):
            wr.writerow([unicode(val).encode('utf8') for val in sheet.row_values(rownum)])
        fp.close()


    def add_day(self):
        # -*- coding: utf-8 -*-
        import csv, os, sys
        with open(self.temp_csv, 'r') as inp, open(self.temp_csv2, 'w') as out:
            writer = csv.writer(out)
            table = csv.reader(inp)
            prewrow = ""
            for row in table:
                if row[0] == "Понедельник":
                    writer.writerow(row)
                    prewrow = row[0]
                elif row[0] == "Вторник":
                    writer.writerow(row)
                    prewrow = row[0]
                elif row[0] == "Среда":
                    writer.writerow(row)
                    prewrow = row[0]
                elif row[0] == "Четверг":
                    writer.writerow(row)
                    prewrow = row[0]
                elif row[0] == "Пятница":
                    writer.writerow(row)
                    prewrow = row[0]
                elif not row[0]:
                    row[0] = prewrow
                    writer.writerow(row)
                else:
                    writer.writerow(row)

    def load_translit(self):
        self.xml_csv()
        self.add_day()
        self.data_in = sp.genfromtxt(fname=self.temp_csv2, delimiter=",", dtype="S100")

    def expand(self):
        out = {}
        final_lens = 0
        for j in range(self.data_in.shape[1] - 2):
            bool_tensor = (self.data_in[:, j+2] != "")
            teacher = self.data_in[:, (0,1,j+2)]
            new_prepod = teacher[bool_tensor]
            final_lens += new_prepod.shape[0]-1
            out_tensor = sp.empty([new_prepod.shape[0]-1, 4], dtype="S100")

            for i in range(out_tensor.shape[0]):
                out_tensor[i, 0] = new_prepod[i+1, 0]
                out_tensor[i, 1] = new_prepod[0, 2]
                out_tensor[i, 2] = new_prepod[i+1, 1]
                out_tensor[i, 3] = new_prepod[i+1, 2]
            out[j] = out_tensor

        final_tensor = sp.empty([final_lens, 4], dtype='S100')
        idx = 0
        for i in range(out.__len__()):
            for j in range(out[i].shape[0]):
                temp = out[i]
                final_tensor[idx+j, :] = temp[j, :]
            idx += out[i].shape[0]
        self.data = final_tensor
        sp.savetxt(self.csv_out, fmt='%s', X=final_tensor, delimiter=',')

    def split(self):
        temp = sp.empty((self.data.shape[0], self.data.shape[1] + 2), dtype='|S100')
        temp[:, 0:3] = self.data[:, 0:3]
        for i in range(self.data.shape[0]):
            str = self.data[i, 3]
            token = str.split("а.")
            hall, camp= token[1].split("к.")
            if camp == "11б":
                camp = 12
            temp[i, 3] = camp
            temp[i, 4] = hall
            temp[i, 5] = token[0]
        sp.savetxt(self.csv_out, fmt='%s', X=temp, delimiter=',')
        self.data = temp

if __name__ == "__main__":
    prs = parser('../data/xlsx/start.xlsx', '../data/out.csv')
    prs.load_translit()
    prs.expand()
