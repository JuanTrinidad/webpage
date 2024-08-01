from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

# importing components
from  ..components import input_geneID_text2
from ..components import data_table_1and2






def page2_data_tables_layout(app: Dash, TABLE1_cols: list[str], TABLE2_cols: list[str]) -> html.Div:
    
    return html.Div(
        children=[
            html.H3('Insert kinetoplastid gene ID', className='text-left mt-4'),
            input_geneID_text2.render(app),
            dcc.Markdown('''
                The first table shows the **MMseqs2 clustering results** of TriTrypDB gene sequences and the functional annotation for each gene (TriTrypDB and UniProt). 
                Given the stringent parameters used, the **annotations are transferable among cluster members**.\n
                The second table shows the results of our approach using **Structural Reciprocal Best Hit** and the functional annotation of the target hits. 
                Additionally, it includes Foldseek values under the prefix FS and the values obtained from FATCAT and TM-align under the prefix FC. 
                As a reference, we consider a good hit to be those SRBH with TM-align values greater than 0.5 for both chains (FC TM-score Chain1 > 0.5 and FC TM-score Chain2   > 0.5).
                ''', className='text-left mb-5'),  
            data_table_1and2.render(app, TABLE1_cols, TABLE2_cols),
            ],
    )
    

