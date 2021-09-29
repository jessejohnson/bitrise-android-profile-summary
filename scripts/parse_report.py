import glob, os, sys
from bs4 import BeautifulSoup

REPORT_DIR = sys.argv[1] # local path/to/report is ../build/reports/profile/

def find_report(report_path):
    os.chdir(report_path)
    return glob.glob("*.html")[0]

def parse_report(file_name):

    with open(file_name) as html_report:
        soup = BeautifulSoup(html_report, 'html.parser')

    # first, we get the total build time
    first_table = soup.find_all('table')[0]
    summary_row = first_table.find_all('tr')[1]
    total_duration_cell = summary_row.find_all('td')[1]
    print("*Total Build Time was {0}*".format(total_duration_cell.string))

    # then we print the time it took each module (ignoring subtasks) to build
    last_table = soup.find_all('table')[-1]
    all_rows = last_table.find_all('tr')
    print("Breakdown\n---------")
    print("Module       Duration")
    for row in all_rows[1:]:
        first_cell = row.td
        if not first_cell.attrs:
            module_name = row.find_all('td')[0].string
            duration = row.find_all('td')[1].string
            if len(module_name) > 1:
                print("`{0}`      {1}".format(module_name, duration))

try:
    report = find_report(REPORT_DIR)
    parse_report(report)
except FileNotFoundError:
    print("There was no profile report in the given directory. :'(")
    print("Did you `--profile` your Gradle task?")
    return 1