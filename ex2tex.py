import pandas as pd


def spreadToTex(filename=None,arr=None,outfile=None,headers=None,delimiter=None,sheetname=0,rotate=0,format=None,colalign='c',skiprows = 0,verbatimcols=[],mathcols=[]):
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
    aligncol = ' '.join([colalign for x in range(len(df.columns.values))])
    table = ''
    table += '\\begin{tabular}{'+aligncol+'} \n'
    table += '\\hline  \n'
    headernames = list(df.columns.values)
    for i in range(len(headernames)):
        if i in mathcols:
            headernames[i] = "$" + headernames[i] + "$"
    table += ' & '.join(headernames)
    table += '\\\\ \\hline  \n'
    for index,row in df.iterrows():
        if index < skiprows:
            continue
        r = []
        i = 0
        for key, value in row.iteritems():
            r.append(value)
            if i in verbatimcols:
                it = " \\verb| "
                it += str(r[i])
                it += " | "
                r[i] = it
                i += 1
                continue
            if i in mathcols:
                it = " $"
                it += str(r[i])
                it += " $"
                r[i] = it
                i += 1
                continue
            r[i] = str(r[i])
            i += 1
        table += ' & '.join(r)
        table += '\\\\ \n'
    table += '\hline \end{tabular}'
    print(table)


