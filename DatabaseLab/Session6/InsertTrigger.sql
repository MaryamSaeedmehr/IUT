-- ================================================
-- Template generated from Template Explorer using:
-- Create Trigger (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- See additional Create Trigger templates for more
-- examples of different Trigger statements.
--
-- This block of comments will not be included in
-- the definition of the function.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Maryam Saeedmehr
-- Create date: 12/9/2019 12:08AM
-- Description:	Make Logs for 'Insert'
-- =============================================
CREATE TRIGGER [Production].InsertLog
   ON [Production].[Product]
	AFTER INSERT 
AS
BEGIN
		INSERT INTO ProductLog 
		SELECT * , 'Inserted'
		FROM inserted
END
GO
