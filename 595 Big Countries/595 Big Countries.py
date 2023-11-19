import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country = world[(world['population'] >= 25000000) |
                        (world['area'] >= 3000000)]
    return (big_country.drop(columns=['continent','gdp']))