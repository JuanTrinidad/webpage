from dash import Dash, dcc
from . import ids






def render(app:Dash) -> dcc.Input:
    
    return dcc.Input(
        id=ids.TEXT_INPUT1, 
        type="text", 
        placeholder="Input geneID: ej. Tb927.10.13280",
        #value='Tb927.3.1760',
        style={
        'borderRadius': '15px',  # Rounded corners
        'border': '1px solid #ccc',  # Subtle border
        'boxShadow': '2px 2px 5px rgba(0,0,0,0.1)',  # Shadow effect
        'padding': '10px',  # Increased padding
        'fontFamily': '"Helvetica Neue", Helvetica, Arial, sans-serif',  # Modern font
        'fontSize': '16px',  # Adjusted font size
        'transition': 'all 0.3s ease',  # Smooth transition effect
        'width': '300px'
        }
        )













#, style={'marginRight':'10px'})