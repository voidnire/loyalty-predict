SELECT dtRef, descLifeCycle, count(*)
FROM life_cycle
group by dtRef, descLifeCycle
order by dtRef, descLifeCycle;

SELECT * FROM life_cycle;