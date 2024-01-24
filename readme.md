# Висновки та пояснення

**У завданні 1-2** було змодельовано граф, який демонстурє наскільки тісно пов’язані найпотужніші корпорації членами правління, за допомогою бібліотеки networkX.

А також використано алгоритми DFS і BFS для знаходження шляхів у графі, у результаті ми можемо бачити такі відмінності:

- Шляхи, знайдені DFS, можуть проходити через більшу кількість вершин, перш ніж досягти тієї ж цільової вершини, що і BFS.
- BFS, у свою чергу, знайде шляхи, які проходять через меншу кількість вершин, що робить його ідеальним для знаходження найкоротших шляхів у створеному графі.

**У завданні 3** реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі, а перед цим модифіковано граф, шляхом додавання ваги до ребер.