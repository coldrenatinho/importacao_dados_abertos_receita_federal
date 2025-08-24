-- Criando o bando de dados 
DECLARE @NomeBancoDeDados char(100) = 'Importação dados receita federal';
DECLARE @DataDados DATE = '2025-08-01' --Dado importados de Agosto de 2025

IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = @NomeBancoDeDados
)
BEGIN
    CREATE DATABASE MeuBancoDeDados;
END;

USE @NomeBancoDeDados


