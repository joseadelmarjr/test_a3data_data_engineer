# Teste Engenheiro de dados

## Respostas práticas
As respostas das questões 1 a 4 podem ser encontradas no  [arquivo de respostas](workspace/Answers.ipynb).


## Resposta dissertativas


*1 - Quais etapas são necessárias para construção de uma solução de armazenamento e disponibilização desses dados?*

R: Para otimizar o processamento dos dados, seria interessante implementar uma lógica para definir períodos de tempo em que os dados já foram processados, evitando assim um processamento completo diário. Além disso, sugeriria coletar os novos registros existentes utilizando uma tecnologia de processamento distribuído, visto que os arquivos têm um tamanho pequeno, porém alto volume, o que resultaria em um desempenho mais adequado. Esses dados coletados seriam armazenados em um formato mais performático, como o Parquet, para facilitar o manuseio.

Para integrar os novos registros aos dados históricos, um processo de ETL seria realizado, incluindo modelagens e tratamentos de qualidade, a fim de disponibilizá-los na camada utilizada pelo time de cientistas. 

Como o processo é executado em uma periodicidade definida, seria recomendável o uso de ferramentas de orquestração em batch para o controle e acompanhamento da carga.


*2– Quais tecnologias você usaria para processar essas informações?*

Em relação às tecnologias, recomendaria a utilização das seguintes ferramentas:

Para armazenamento do delta de carga e delta de novos registros, seria interessante utilizar buckets, como o AWS S3, GCS ou AzureBlob.
Para processar os arquivos no storage, sugiro utilizar o Apache Spark, que pode ser implementado por meio de serviços gerenciados, como o AWS Glue, DataFlow ou Azure DataFactory.
Para orquestração, o Apache Airflow seria uma boa opção, podendo ser implantado em um provedor de kubernetes, como o AWS EKS, GCP GKE ou Azure AKS.
Para armazenamento e análise dos dados processados, seria necessário uma ferramenta de armazenamento e análise, como o AWS RedShift/Athena, GCP BigQuery ou Azure Synapse. Cada uma dessas ferramentas possui recursos que podem ser explorados, dependendo da necessidade do projeto.

## Respostas práticas - Para replicar
Optei pelo uso do GCP como provedor do banco de dados e para replicar no seu ambiente, salve seu arquivo de credenciais no diretório workspace/keys/google_application_credentials.json.

Para execução do notebook, adicionei um container com uma versão básica do Jupyter notebook. Para utiliza-la basta executar o comando ```docker compose up``` na raiz do diretório e acessar o endereço [http://localhost:8888](http://localhost:8888/tree/workspace)