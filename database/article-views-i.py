import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    read_self = views[views['author_id']==views['viewer_id']]
    #group = read_self.groupby("author_id")["article_id"].count().reset_index()[["author_id"]].rename(columns = {"author_id":"id"}).sort_values("id")
    #当你要用count的sort的时候再使用！！
    group = read_self.sort_values('author_id').rename(columns={"author_id": "id"})
    return group[["id"]].drop_duplicates()
    