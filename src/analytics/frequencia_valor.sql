SELECT 
idCliente, count (DISTINCT substr(DtCriacao,0,11)) AS qtdeFrequencia,
                sum(
                    CASE WHEN QtdePontos > 0 THEN QtdePontos ELSE 0
                    END
                ) as qtdepontosPos,
                sum(abs(QtdePontos)) as qtdePontosAbs 
               
FROM transacoes

WHERE DtCriacao < '2025-09-01'
and DtCriacao >= date('2025-09-01', '-28 days')

group by idCliente

order by DtCriacao desc