-- Select all top records within @score>=10, on desc order on @second_table.
SELECT score, name FROM second_table WHERE score>=10 ORDER BY score DESC;
