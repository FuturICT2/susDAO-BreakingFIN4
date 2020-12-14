with open('report_securify_nocolor.txt', 'r') as file:
    dataraw = file.read()

data = dataraw.split("\n\n")


latexstr="""
\\begin{{table}}[]
\\hskip-1.0cm\\begin{{tabular}}{{|l|l|}}
\\hline
Severity    &  {}\\\\ \\hline
Pattern     &  {}\\\\ \\hline
Description &  {}\\\\ \\hline
Code        &  
\\begin{{lstlisting}}[language=Solidity]
{}
\\end{{lstlisting}}
\\\\ \\hline
\\end{{tabular}}
\\end{{table}}
"""

for d in data:

    if "Severity" not in d:
        continue

    issue = [ i for i in d.split("\n") if i!=""]
    
    beg = [False for i in range(0,6)]
    
    for i in range(0, len(issue)):
        if "Severity" in issue[i]:
            beg[0] = i
        if "Pattern" in issue[i]:
            beg[1] = i
        if "Description" in issue[i]:
            beg[2] = i
        if "Type" in issue[i]:
            beg[3] = i
        if "Source" in issue[i]:
            beg[4] = i
    
    #print(beg)
    
    
    severity = [s for s in issue if "Severity" in s][0].split(":")[1].lstrip()
    
    pattern =[s for s in issue if "Pattern" in s][0].split(":")[1].lstrip()
    
    desc = " ".join([i.lstrip() for i in issue][beg[2]:beg[3]]) 
    
    type = "\n".join(issue[beg[3]:beg[3]])                        
    
    code = "\n".join([i[1:].lstrip() for i in issue if i.lstrip() !="" or i.lstrip()][beg[4]+1:])
    
    code= code.replace("^^^", "")
    code = code.replace("\n\n", "")
    
    extracted=[severity, pattern, desc, type, code]
    
    #print(extracted)
    
    print(latexstr.format(extracted[0], extracted[1], extracted[2], extracted[4]))
