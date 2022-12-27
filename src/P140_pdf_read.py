# Run command: pip install "camelot-py[base]"
# check requirements.txt PyPDF2~=2.0


import camelot

tables = camelot.read_pdf(
    "https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/salary-tables/pdf/2022/DCB.pdf",
    pages="1",
)

print(tables[0].df)
