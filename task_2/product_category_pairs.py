from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_product_category_pairs(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_df: DataFrame
) -> DataFrame:
    """
    Возвращает DataFrame со столбцами:
      - product_name: имя продукта
      - category_name: имя категории или None, если категория отсутствует

    Каждая строка — пара «продукт–категория», а для продуктов без категорий
    будет одна запись с category_name = None.
    """
    return (
        products_df.alias("p")
        .join(
            product_category_df.alias("pc"),
            col("p.product_id") == col("pc.product_id"),
            how="left"
        )
        .join(
            categories_df.alias("c"),
            col("pc.category_id") == col("c.category_id"),
            how="left"
        )
        .select(
            col("p.product_name"),
            col("c.category_name")
        )
    )
