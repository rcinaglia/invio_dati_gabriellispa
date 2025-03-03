SELECT * FROM 
(
SELECT
    TO_CHAR(MIN(INC_DATA), 'YYYY-MM-DD') AS day,
    PDV_COD AS pdvcode,  -- Codice del PDV
    CCO_COD AS ccocode,  -- Codice del CCO
    SUM(INC_VALORE) AS sales,  -- Somma delle vendite per ogni combinazione PDV_COD e CCO_COD
    SUM(INC_BATTUTE_TOT) AS tickets  -- Somma dei ticket per ogni combinazione PDV_COD e CCO_COD
FROM DM.FAT_INCASSI
INNER JOIN 
    DM.DIM_ANA_PDV ON DM.FAT_INCASSI.PDV_KEY = DM.DIM_ANA_PDV.PDV_KEY
INNER JOIN 
    DM.DIM_ANA_CCO_REP ON DM.FAT_INCASSI.PDV_KEY = DM.DIM_ANA_CCO_REP.PDV_KEY
WHERE 
    INC_DATA = TO_DATE('2025-01-03', 'YYYY-MM-DD')
GROUP BY 
    PDV_COD,  -- Raggruppamento per PDV_COD
    CCO_COD  -- Raggruppamento per CCO_COD
) WHERE PDVCODE = 410;