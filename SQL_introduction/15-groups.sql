-- lists number of recors with the same scote on @second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
