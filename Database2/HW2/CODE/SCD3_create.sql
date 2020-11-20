CREATE TABLE [dbo].[SCD_3](
	[customer_code] [int] NOT NULL,
	[name] [varchar](200) NULL,
	[branch] [int] NULL,
	[type] [int] NULL,
	[id_code] [varchar](12) NULL,
	[phone] [varchar](12) NULL,
	[original_job] [varchar](100) NULL,
	[effective_date] [date] NULL,
	[current_job] [varchar](100) NULL,
	primary key (customer_code)
)

