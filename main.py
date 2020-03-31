#!/usr/bin/env python
import re
import glob

import pynmea2_non_standard
#import pyaml

pco2_line_re = re.compile(r'''
    #start of string is $PCO2-
    ^\$PCO2-
    ''', re.X | re.IGNORECASE)

pco202_line_re = re.compile(r'''
    #start of string is $PCO2_
    ^\$PCO2_
    ''', re.X | re.IGNORECASE)

mstat_line_re = re.compile(r'''
    #start of string is $MST@T
    ^\$MST@T
    ''', re.X | re.IGNORECASE)

meteo_line_re = re.compile(r'''
    #start of string is $METEO
    ^\$METEO
    ''', re.X | re.IGNORECASE)

sbe37_line_re = re.compile(r'''
    #start of string is $SBE37
    ^\$SBE37
    ''', re.X | re.IGNORECASE)


# one file path = "/media/Part500GB/Progetti/e2m3a_vam1/Boa/Dati/raw_cf/A181201A.TXT"
path = "/media/Part500GB/Progetti/e2m3a_vam1/Boa/Dati/raw_cf/2017_03_24_2018_10_09/"
savepath = "/media/Part500GB/Progetti/e2m3a_vam1/Boa/Dati/raw_elaborati/"
    #legge tutti i files A*.TXT
for files in sorted(glob.glob(path+'A*.TXT')):
    infile = open(files)
    #print ("a file {}\r".format(infile))
    for line in infile:
        try:
            line = re.sub(pco2_line_re, '$PCO2_', line)
            line = re.sub(pco202_line_re, '$PCO2_', line)
            line = re.sub(mstat_line_re, '$MSTAT', line)
            line = re.sub(meteo_line_re, '$METEO', line)
            line = re.sub(sbe37_line_re, '$SBE37', line)
            msg = pynmea2_ogs.parse(line)
            with open(savepath + msg.identifier() + '.TXT',"a+") as outfile:
                outfile.write(line)
                    #outfile.write(a[0])
                    #outfile.write("\n")
                    #print(a[0], file=outfile, end='')
        except AttributeError as e:
            print ('attribute error ' + str(e))
            #print (e)
        except pynmea2_ogs.ParseError as e:
            print ('parse error')
            print (e)
        except pynmea2_ogs.SentenceTypeError as e:
            print ('sentence_type_error')
            print (e)

infile.close()
outfile.close()
print ("done")
