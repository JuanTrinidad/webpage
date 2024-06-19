from dash import Dash, html


# importing components
from  ..components import input_geneID_text
from ..components import gene_summary_annotation





def page1_gene_summary_layout(app: Dash) -> html.Div:
    
    return html.Div(
        className="app-div1",
        children=[
            html.Div(style={'marginBottom': '20px'}),
            input_geneID_text.render(app),
            html.Hr(),
            gene_summary_annotation.render(app)
            ],
    )
    
