from pyspark.sql.functions import asc, dense_rank, desc, format_number, when

from pyspark.sql.window import Window


df_vendas = spark.read.table("vendas")
df_produtos = spark.read.table("produtos")

df_vendas_por_categoria = df_vendas.join(
    df_produtos, df_vendas.cod_produto == df_produtos.cod_produto, "inner"
)

df_vendas_por_categoria = df_vendas_por_categoria[
    "cod_usuario",
    "produtos.cod_produto",
    "nome_produto",
    "categoria_produto",
    "data_compra",
    "quantidade",
    "valor",
]

window_spec = Window.partitionBy("cod_usuario", "categoria_produto").orderBy(
    "data_compra"
)

df_vendas_por_categoria = df_vendas_por_categoria.select(
    "cod_usuario",
    "cod_produto",
    #    "nome_produto",
    "categoria_produto",
    "data_compra",
    "quantidade",
    "valor",
    dense_rank().over(window_spec).alias("ordem_compra"),
)


df_vendas_por_categoria = df_vendas_por_categoria.orderBy(
    asc("categoria_produto"), asc("cod_usuario"), desc("ordem_compra")
)

df_vendas_por_categoria = df_vendas_por_categoria.withColumn(
    "valor_com_desconto",
    when(df_vendas_por_categoria.ordem_compra > 3, col("valor") * 0.9).otherwise(
        col("valor")
    ),
)


df_vendas_por_categoria = df_vendas_por_categoria.withColumn(
    "valor", format_number("valor", 2)
)

df_vendas_por_categoria = df_vendas_por_categoria.withColumn(
    "valor_com_desconto", format_number("valor_com_desconto", 2)
)

df_vendas_por_categoria = df_vendas_por_categoria.filter(col("cod_usuario") == 1334)


df_vendas_por_categoria.show()

print((df_vendas.count(), len(df_vendas.columns)))
print((df_produtos.count(), len(df_produtos.columns)))
print((df_usuarios.count(), len(df_usuarios.columns)))
