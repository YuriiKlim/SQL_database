-- SELECT * FROM FruitsAndVegetables
-- WHERE Type = 'Vegetable' AND Calories < 50;

-- SELECT * FROM FruitsAndVegetables
-- WHERE Type = 'Fruit' AND Calories BETWEEN 50 AND 100;

-- SELECT * FROM FruitsAndVegetables
-- WHERE Type = 'Vegetable' AND Name ILIKE '%Carrot%';

-- SELECT * FROM FruitsAndVegetables
-- WHERE Description ILIKE '%sweet%';

-- SELECT * FROM FruitsAndVegetables
-- WHERE Color IN ('Yellow', 'Red');

-- SELECT COUNT(*) FROM FruitsAndVegetables 
-- WHERE Type = 'Vegetable';

-- SELECT COUNT(*) 
-- FROM FruitsAndVegetables 
-- WHERE Type = 'Fruit';

-- SELECT COUNT(*) 
-- FROM FruitsAndVegetables 
-- WHERE Color = 'Yellow';

-- SELECT Color, COUNT(*) 
-- FROM FruitsAndVegetables 
-- GROUP BY Color;

-- SELECT Color FROM FruitsAndVegetables 
-- GROUP BY Color 
-- ORDER BY COUNT(*) ASC LIMIT 1;

-- SELECT Color FROM FruitsAndVegetables 
-- GROUP BY Color 
-- ORDER BY COUNT(*) DESC LIMIT 1;

-- SELECT MIN(Calories) FROM FruitsAndVegetables;

-- SELECT MAX(Calories) FROM FruitsAndVegetables;

-- SELECT AVG(Calories) FROM FruitsAndVegetables;

-- SELECT Name FROM FruitsAndVegetables 
-- WHERE Type = 'Fruit' 
-- ORDER BY Calories ASC LIMIT 1;

-- SELECT Name FROM FruitsAndVegetables 
-- WHERE Type = 'Fruit' 
-- ORDER BY Calories DESC LIMIT 1;
