from camelot import read_pdf

name = "5_5 SOL"
t = read_pdf(f"{name}.pdf")
t.export(f'{name}.csv', f='csv')

