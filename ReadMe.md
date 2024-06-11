
This folder creates a  dataset to translate the isco codes to their corresponding label-names for all detail levels

structure08.docx which contains this information was downloaded from:
http://www.ilo.org/public/english/bureau/stat/isco/docs/structure08.docx

Found on https://www.ilo.org/public/english/bureau/stat/isco/isco08/
(it's ISCO-08  part 2: Classification Structure)
(https://web.archive.org/web/20231203112122/https://www.ilo.org/public/english/bureau/stat/isco/isco08/index.htm)

isco88 formats where also found on https://web.archive.org/web/20231111045310/https://ilo.org/public/english/bureau/stat/isco/isco88/major.htm
(the other links are also old (circa 2023), and might not work anymore, when i tried they were restructuering the website)
They were simply copy-pasted into the isco88.txt file

create_formats.py then turns these files into the datasets, isco08_format.csv and isco88_format.csv with the format keys at 1, 2, 3, and 4 - digit level.
