import pandas as pd
from ddbapi import zp_pages


def article_extractor(search_dict):
    """
    This function extracts newspaper articles in a given language between two given dates. It takes a dictionary with 
    three keys as its only argument, like the following example:
    """

    
    newspapers = zp_pages(language=search_dict['language'], 
                  publication_date= f"[{search_dict['date_begin']}T12:00:00Z TO {search_dict['date_end']}T12:00:00Z]")

    return newspapers




def create_year_list(start_year, end_year):

    """
    With this function you can create a list of years. If you pass two years to this function, 
    it creates a list of the time period in between. 
    """

    if start_year > end_year:
        raise ValueError("Start year must be less than or equal to end year.")
    return list(range(start_year, end_year + 1))





years = create_year_list(1914, 1945)
path = newspapers

if not os.path.exists(path):
    os.makedirs(path)


for year in years:


    search_dict= {
        'language': 'ger',
        'date_begin': f'{year}-01-01',
        'date_end': f'{year}-04-30'
        }
        
    df_challenge= article_extractor(search_dict)
    df_challenge.to_pickle(f"{path}/newspapers_{search_dict['language']}_{year}_part_1")



    search_dict= {
        'language': 'ger',
        'date_begin': f'{year}-05-01',
        'date_end': f'{year}-08-31'
        }
        
    df_challenge= article_extractor(search_dict)
    df_challenge.to_pickle(f"{path}/newspapers_{search_dict['language']}_{year}_part_2")



    search_dict= {
        'language': 'ger',
        'date_begin': f'{year}-09-01',
        'date_end': f'{year}-12-31'
        }
        
    df_challenge_ger= article_extractor(search_dict)
    df_challenge_ger.to_pickle(f"{path}/newspapers_{search_dict['language']}_{year}_part_3")