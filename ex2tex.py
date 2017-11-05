import pandas as pd


def spreadToTex(filename=None,arr=None,outfile=None,headers=None,delimiter=None,sheetname=0,rotate=0,format=None,colalign='c',skiprows = 0):
    if not filename:
        if not arr:
            return
        if not headers:
            headers = range(len(arr[0,:]))
        df = pd.DataFrame(arr, columns=headers)
    else:
        if not delimiter:
            df = pd.read_excel(filename,sheet_name=sheetname)
        else:
            df = pd.read_csv(filename,delimiter=delimiter)
    # TODO: this is a janky way to do row formatting, refactor
    aligncol = ' '.join([colaign for x in range(len(headers))])
    table = ''
    table += '\begin{tabular}{'+aligncol'} \n'
    table += '\hline \n'
    table += ' & '.join(list(df.columns.values))
    table += '\\\hline \n'
    for index,row in df.iterrows():
        if index < skiprows:
            continue
        r = []
        for key, value in row.iteritems():
            r.append(value)
        table += ' & '.join(r)
        table += '\\ \n'
    table += '\hline \end{tabular}'

    
