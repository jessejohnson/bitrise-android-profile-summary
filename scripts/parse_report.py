import glob, os, sys
from bs4 import BeautifulSoup

def find_report(report_path):
    os.chdir(report_path)
    return glob.glob("*.html")[0]

def parse_file(file_name):

    output = ""

    with open(file_name) as html_report:
        soup = BeautifulSoup(html_report, 'html.parser')

    # first, we get the total build time
    first_table = soup.find_all('table')[0]
    summary_row = first_table.find_all('tr')[1]
    total_duration_cell = summary_row.find_all('td')[1]
    
    output += "*Total Build Time was {0}*\n".format(total_duration_cell.string)

    # then we print the time it took each module (ignoring subtasks) to build
    last_table = soup.find_all('table')[-1]
    all_rows = last_table.find_all('tr')
 
    output += "Breakdown\n---------\n" + "Module       Duration\n"
    for row in all_rows[1:]:
        first_cell = row.td
        if not first_cell.attrs:
            module_name = row.find_all('td')[0].string
            duration = row.find_all('td')[1].string
            if len(module_name) > 1:
                output += "`{0}`      {1}\n".format(module_name, duration)
    return output