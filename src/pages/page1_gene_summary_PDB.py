from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


# importing components
from  ..components import input_geneID_text
from ..components import gene_summary_annotation
from ..components import PDB_viewer
from ..components import drop_down_for_pdb



def page1_gene_summary_layout(app: Dash):
    
    return html.Div(children = [
        html.H3('Insert kinetoplastid gene ID', className='text-left mt-4'),
        input_geneID_text.render(app), 
        dcc.Markdown('''
                    In this section, we summarize the annotation data from TriTrypDB and UniProt for genes with SRBH in our approach. If your gene of interest is not here go to **Cluster information and SRBH results**. \n \n
                     The first two tables present the functional annotation data from the TriTrypDB and UniProt databases, respectively. \n
                     The third table provides the functional annotation data for each SRBH result obtained from our proteins structure comparisons.
                     Each column represents an organism and the corresponding SRBH annotation for the selected gene.
                     ''', className='text-left mb-5'),
        gene_summary_annotation.render(app),
        dcc.Markdown('''
                    Select a specie from the previous table to visualize the proteins structure aligment against the Kinetoplastid proteins structure.
                     ''', className='text-left mt-5'),  
        drop_down_for_pdb.render(app),
        PDB_viewer.render(app)
        ]
    )
            
    
