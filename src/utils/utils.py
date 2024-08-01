import pandas as pd





### Funtion to determine the background color of each column based on TM scores. Page 1 SRBH table ###
def determine_column_colors(data, row1, row2):
    # Initialize list to hold style conditions for each column
    style_data_conditional = []
    
    # Set 'Specie' column as the index of the DataFrame
    data = data.set_index(['Specie'])

    # Iterate over each column in the DataFrame
    for column in data.columns:
        # Retrieve TM scores for two chains
        tm_score_1 = data.loc['FC TM-score Chain1', column]
        tm_score_2 = data.loc['FC TM-score Chain2', column]
        
        # Determine background color based on TM scores
        if tm_score_1 >= 0.5 and tm_score_2 >= 0.5:
            backgroundColor = '#93c47d'  # Assign green for high scores
        elif tm_score_1 > 0.4 and tm_score_2 > 0.4:
            backgroundColor = '#ffe084'  # Assign yellow for medium scores
        else:
            backgroundColor = '#dd9090'  # Assign red for low scores
        
        # Append style condition for the current column
        style_data_conditional.append({
            'if': {'column_id': column},
            'backgroundColor': backgroundColor,
            'color': 'black'  # Set text color to black
        })
        
    # Return the list of style conditions
    return style_data_conditional