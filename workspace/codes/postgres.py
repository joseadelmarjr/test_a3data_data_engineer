import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class PostgresDB:
    def __init__(self):
        self.host = "db"
        self.database = "postgres"
        self.schema = "public"
        self.user = "postgres"
        self.password = "admin123"
        self.port = "5432"
        self.conn = None
        self.engine = None

    def __connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
        except psycopg2.Error as e:
            print("db connection error.")
            print(e)

    def __set_engine(self):
        self.engine = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

    def __close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        self.__connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            col_names = [desc[0] for desc in cursor.description]
            df_query_result = pd.DataFrame(cursor.fetchall(), columns=col_names)
            self.conn.commit()
            return df_query_result
        except psycopg2.Error as e:
            print("Somenthing was wrong.")
            print(e)
        finally:
            self.__close()

    def import_df(self, df, table_name):
        self.__connect()
        self.__set_engine()

        try:
            df.to_sql(
                name=table_name, con=self.engine, if_exists="replace", index=False
            )

        except Exception as e:
            print("Something wrong")
            print(e)

        finally:
            self.__close()


## Exemplo de uso

# postgres = PostgresDB()
# dim_tables = ["DimAccount", "DimDepartmentGroup", "DimOrganization", "DimScenario"]
# fact_table = "FactFinance"

# for table in dim_tables:
#     print(f"Insert {table} in database")
#     df_table = pd.read_csv(f"land/{table}.csv", sep=";")
#     postgres.import_df(df_table, table)

# fact_df = pd.read_csv(f"land/{fact_table}.csv", sep=";")
# fact_df["Amount"] = fact_df["Amount"].str.replace("R\$","")
# fact_df["Amount"] = fact_df["Amount"].str.replace(",","")
# fact_df["Amount"] = fact_df["Amount"].astype(float)
# postgres.import_df(fact_df, fact_table)
