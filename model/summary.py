import pandas as pd
from potara.summarizer import Summarizer
from potara.document import Document

file_list = ['Boeing Crisis.csv', 'Brexit.csv', 'Hong Kong Protests.csv', 'Iran Sanctions.csv', 'US China Trade War.csv']

def summarize(file):
    s = Summarizer()
    to_display = {}
    # for i in range(len(file_list)):
    issue = file.split('.')[0]
    df = pd.read_csv(file).sort_values(by=['probability'], ascending=False)
    articles = df['content'].tolist()

    output = []
    
    print('Preparing Documents for Summarization')
    print('------------------------------------------------------')
    for k in range(0,10):    
        output.append(Document(articles[k]))
    print('------------------------------------------------------')

    print('Summarization Process:', issue)
    print('------------------------------------------------------')
    s.clearDocuments

    # Adding docs, preprocessing them and computing some infos for the summarizer
    s.setDocuments(output)

    # Summarizing, where the actual work is done
    s.summarize(wordlimit=200)

    # You can then print the summary
    summary = s.summary
    print('------------------------------------------------------')

    print(summary)
    
    to_display[0] = {'group': issue, 'summary': ' '.join(summary)}

    output_df = pd.DataFrame.from_dict(to_display)
    output_df = output_df.transpose()
    output_file = issue +'_summary.csv'
    print(output_file)
    output_df.to_csv(output_file, encoding='utf-8-sig')

summarize(file_list[4])