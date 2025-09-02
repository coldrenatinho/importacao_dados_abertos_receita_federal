-- Ajustar para o princial e utilizar variaveis
CREATE LOGIN federal
WITH PASSWORD = 'SenhaForte123!';

USE Importacao_Dados_Receita_Federal
CREATE USER federal FOR LOGIN federal

ALTER ROLE db_datareader ADD MEMBER federal;
ALTER ROLE db_datawriter ADD MEMBER federal;