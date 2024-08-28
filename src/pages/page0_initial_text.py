from dash import Dash, html, dcc
import dash_bootstrap_components as dbc





def page0_text_layout(app: Dash):
    
    return html.Div(children = [
        html.H3('Welcome to the Kinetoplastid Gene Annotation Database', className='text-left mt-4'),
        dcc.Markdown('''
                    This database provides a comprehensive annotation of kinetoplastid genes available at TriTrypDB release 65. 
                    The annotation data is collected from various databases, including TriTrypDB and UniProt. 
                    Additionally, we provide the results of our protein structure comparison analysis using the ASC pipeline available at [GitHub](https://github.com/JuanTrinidad/ASC). 
                    The database allows users to search for a specific gene by entering the gene ID and view the corresponding annotation data. 
                    The annotation data includes information on the gene function, protein domains, and structural features.  
                    This database aims to facilitate the study of kinetoplastid genes and their role in parasite biology and pathogenesis.
                    ''', className='text-left mb-5')
        ]
    )