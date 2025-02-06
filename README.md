 Para começar o projeto foi iniciado o airflow com o docker, conforme a documentação disponível do airflow. Após a inicialização do airflow também foi gerado os cointaners para o airflow;

 Após isso foram criados o banco de dados de source (northwind), da fonte das informações e o de destino (destination_db), para receber as informações;

 Nessa parte também foi criado um arquivo .env para ocultar as variáveis de conexão dos bancos, visando trazer mais segurança;

 Os bancos também tiveram seus containers inicializados no docker e foram testadas as conexões através do dbeaver, ambas conectando corretamente. Desta forma foi possível verificar as informações das tabelas e validar o recebimento e passagem de informações;

 Em seguida foi iniciado o projeto do meltano, visando ativá-lo somente  através das tasks contidas nas dags do airflow que foram feitas na sequência;

 O projeto do meltano foi instalado num ambiente virtual (meltano-venv);

 Dentro do ambiente virtual foi instalado o meltano e feita a configuração do yml com o plugin de extração tap-postgres, adaptando para o plugin tap-postgres-orders, pois a ideia era fazer toda a pipeline para uma das tabelas e após replicar para as demais, para tal foi escolhida a tabela orders. Também foi feito o plugin de carregamento loaders para repassar os dados para um arquivo local jsonl;

 Foi realizado um teste rodando os comandos de extração do forma manual e enviado para a pasta output, onde foi possível obter as informações da tabela orders de forma completa;

 Após isso foi feito um dockerfile para definir a imagem do meltano e para o airflow se conectar ao meltano através do dockeroperator

Por fim, foi iniciada a criação da parte de dags do airflow onde foi continuada a ideia de completar primeiramente para a tabela orders. Foi criada a DAG de extração diária de informações do banco de dados para que após fossem enviadas para o arquivo local. Neste trecho foram retornados alguns problemas e a DAG acabava falhando ao tentar rodar de forma manual nos testes.

Foram realizados alguns testes e tentativas de ajuste para a dag de extração através dos logs, porém sem sucesso, não sendo possível atingir o objetivo final do desafio.

