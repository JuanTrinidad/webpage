
from dash import Dash, html
from dash_bootstrap_components.themes  import BOOTSTRAP
from src.components.layout import create_layout
from src.data.loader import load_annotation_data
from src.data.loader2 import load_annotation_data2




DATA_PATH = "./data/tables/webpage_Table1.tsv"
DATA_PATH2 = "./data/tables/webpage_Table2.tsv"




def main() -> None:
    data = load_annotation_data(DATA_PATH)
    data2 = load_annotation_data2(DATA_PATH2)
    
    app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
    
    app.title = 'Kinetoplastid Structural Annotation Database'
    
    app.layout = create_layout(app, data, data2)
    
    app.run_server(debug=True)





if __name__ == '__main__':
    main()