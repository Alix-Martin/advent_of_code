from itertools import product

LARGE = True

map = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########"""

if LARGE:
    map = """##################################################
#.......#....O....O......O..O#.OOOO....#.OO......#
#..O.O..#O..#O..#O.OO......O....O..O....#O.......#
#...O......O...O...O.......#O#.O.#OO.O........O.O#
#..O..#O..#.O....OO..OO.....#.OO.....#.O#OOOOO.O.#
#........O#.....O..OO......#.O..O#...O.O..O......#
##O..O.O...#O.#...#O...#O..##......#............O#
#.OO#O.O..O...O#..OO...#..###O....OO.#.O.##....#.#
#.O...........O.....O..O.OO.O.O...O..OO....OO....#
#OO..........O...O........O..##O.OOO.O..O..O..#.O#
#.#O.....O.OO....#O..O...O.....O...........OO..#O#
##.....O.......O.O.O....O.O...#O.O..O##....OO#...#
#.OO......O.......O..#...O......#.OOOO.OOO...#O..#
#.........O.O....OO..##.....OO...#....O.OO..OO...#
#O....O..O..#...OOO...OOO#..OO......OO..O....OO.O#
#....O.........O....#.#.O..OO......O.O..#O.O#OO..#
#...O.OOO.O.O..O.........O.OO....OO.O.....OO..OOO#
#..O.........#...OO.O#.O....OOO......O..........O#
#........O.O.O.O..OOOOO.#.O.OO#OO.....#...O.O.#O.#
#OO...O.#O.OOO....O....O.#.O.OOO.O..O......OOOO.O#
#...#OO.O..O...O.OOO.....O.O.OO.#..O#...O..OO....#
#O.OOOO.O........#O.##......#....#...OO..O.O.OO..#
#.OOO.O.O#OO...O.O...O.........O........O..O#OOO.#
#.#..O........#......O......O.....O....O.#..O....#
#...#.....O.O.OOO.OO.O.O@O.O.O.O..#O....#.#.OO..O#
#O.......#O...#O....O.#.....OO.#O.O..O.O......O..#
#......O...OO.OO..O#....OOO.#.#....O.O....OO....O#
#...O.O.#..OO#.O.OO...O.#.#..#O..#...##..O.......#
##O...O..OO.O..O.OOO..O.........O#O...#..#.O..O#O#
#O.O....#OO..OOO.#O..#O..O.#...#.#..O....O.O....##
#.O.OOO.O....O...#O.O...OOO..O.....O.O..O.O..O..O#
#......O...O..OO.O........O..........O....#....OO#
#.O..OO.O.OOO..OO...........O........O.O....OO.O##
#.O.OO#....#.........#..O...OO...OO..OO..........#
#...OO...OO..OO.O...O.....#...O.#.....OO.O.O.O#O.#
#OO......#...OO......O..O.O...O...#.....O......OO#
#O...O.....O...O.O.O....O##OO.O..#..O....O#OO...O#
#.O.O#OO..##.#O...O#O..O.O#..O...OO...OOO.......##
#...O.#.O.#......OO.......O.OO..#.OOOOO...OO..O.##
#............O..O.....#O.##.O.O.#....O#.......O.O#
#.O..##..O....#O.O..#....O...OOO#.#...#..O...O...#
#.O.OOOO..#.........O.O#....O....OO.OO.....##OOO.#
#..O#...OO..O...O#...#..OO.OO...#....O........O.O#
#.O.O..O....O...O.O.OO#...OO..O.OO.O.O..O...O....#
#.O#..OO...#.OO...........OO.....OO#O.#..O.O...#.#
#..................O.......O...OO..O..O.O.O.O##..#
#.##.#..OO.#..........O#...O.O.O...##..O......O.O#
#OO.O........####.......O.......O......O...##....#
#.O........O..O..#...O.OO...#....#.#.....OO...O.##
##################################################"""

moves = """<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

if LARGE:
    moves = """<><v>^vv<^<v<>^>^^<^^>>^>><vv^>^>^<v<>>^^>>v^>^<v><v><v>>^<^<<^^>^>^<<v^<<^^v><<><v>v^>^^<v<<<>v<>^>^^^><v<><v^<><vv^v>^>^>><^<vv<^>^<^<<<<<^<^vv><v>^v^^><<>>v<v>vvv^<>v<>v><<<v^<^<^vv<^v<>v<<<<<>v<^<<<^<^v^<^>^>>vv>>^^<>^^<^v<^v<<vv<vvv^<^^<>v^^><^^^v^>^>^^<<<^<v<^<><v^<^v^<>>v><^^v^vv><vv>^v>>^vv>v><v<>>>^>>^v>v^^<vv^<v>vv<^<>^>>^v^v><^v^>>^>^<<<<<><v<v<vvv><><^^v^^^<>v<>vv>v^>>>^<>>^^^><v<^<>v<^>^<vvv^>^>vvv>>v<>v<>v<><><<^vv>^<^<<>^^<v<^^>v^v<v<>>^^><>^>>>^v^<>^^^<>><v><>v><>v>^<>vvv>>><><v<><>v^vv^>v^^>>v<^<^<v^>>>^^>>v<<<v^vvvv>^^v>^v<^>^vv^v^v<^^>v>^vv<<v^^^v^<v<^v^<v><v>^^v<^^><^^<^vvv<v<<><>v^<>><<<^vv<^^<<>^^<^<^>^<><v><^>v>><><v^vv<<>>^^>vvv^><<^v<<^>^<^<<><^<>^<>vv>><v>^^<v<v>v^v^^<<>^>>^^v>>v>^^>^<><^>v<vvv>^>v<><vv<><^v>>^<^^<<<<<>^vv<<<v>^<><^<v>v^<v<v<v^<v^<>^v<vv^vv>v^^>v^>^^<v^<<v>^^v>v><<<<<^vv><v>>v><^^^v<^^vvv^^>^^^>vv<>v^<>><><<><^>^^^v^<v>>>v<>vv>vvvv^>>v<<<^vv>>>^v^v><<^vvv^<<>v<><^v><>^v>>v>^^<<>v^vvv><^^<>>^<<<<>>^>>v^^<>>>>vv>v<v^>^<^v>v>>^^>v^^v<^vv><^<^^<vv
<<^<><v<^vvv<<vv<vv<><v^v><>><<v^<>^>>^>>^^^<^^v<vvv^v>v<>^>><^v>^^vvv^<>>>v>>vvv><^^v>vvv<vv<><v>>vv^^<>^^<^>v^<v>vv^<><v<^<>^vv>^^><>^>^v^<vvv><>^>><^<^>v>v>><v<<vv^^^>^v^vvv>>vv^^<^^<>>v<<vvv^<^<^>>v>>v<<v^<^v><v^><^>v^<v<vvvvv>>>^^v><<^^>v><<<^^<<<^><^<<^v<>^<>v<<<v>v<v<<<^v^^^<v<^^^<^<vv<>>^<^<>v^>>v^v><^vvv>^>>v><<^<<v>v>v>^v<v^<v^^v>^>>^<v^v<>^v><<>>>>>^>^<v<v>>^^v<><><<v>vv><^<>><v>>>v^v<>^><v^v^><<v<^^<vvv<v>^>vvv<>^>>v>^v<^^^v>v>v<>>^<><^<^<<v^<^>vv^v^>v^^^^^v^v><>v<><<<v^vv^>v<v<><>>^^<^<v<>^><>v^^>^^><>v>v^^>v<>>^>^^<v<^^^<<^^>^^>vv<^<^><>^^^v^^^>>^>>v<<^v^^v^<^^^v<^^>>^>^<v<>>^^>><vvv>v<v<>^<vv<v^v>^<v>v>v<>v<v<<<><<<^>>>^>^v>vv>>v^vv^<vv>><<>>v^>^^>>^v>^^v^v^<^<v><><v>v><^^^>^><v>vv<><<^^^<v<^^vv<><v<v>vv^^><><^v^<^v>v<<v>>v<vvv<<^<<v<vvv>>vv<<^<vv><>>v><vv<<>v<vv^><><^v<^<><<>>v<>v^v^<v<><v>^>v>v^vv>v<<v^>>><<<v<^v<v^^v^^>v^v>vvv>v<^v<^<<^>v>><<<v<>>vv>v><vvvvv>vv>v^<^^^<v<v^v<<v^v<^^>>v<vvv<>v>>^<v>^<v^<>^^>>^>vv^<>v^v^<vv^<>>v^^^v^^^^>^v><v<>^>v<v><>>><><^v><^^v<>v^v^>
vv^^>v^^v<v<vvv<v<<v^>vv<>>>^v^>v>^><>v^><><v^^<^>v><vv>>><v<>v<<<^v<<>^^<vvvv^^>v>v<^>v^^<<vv^v>v^><><><<vvv>v>vv^<<<vv^<v<^>v^<^>vv<>>>vv>^^^^>vv>v^^v<>^^^>v><>>v<>v>>v<^<<>^>><^v<<^<^>><>vv>^><>^^^^^^>^<^<v<<^<<v<v^v>^vvv^<>^v^>><<<^^>^^<v>v^v<^>>><^^<v^<vv><<vvv<<^>v^^>v>v<v^v>v<^v>>v^>^<<v><v>^>^<v<><^>><>>^><^<<^v><^<<>v>><>v<<v<><^v>><^<vv>>v^<><>>^^<<v>>>v^>^v>v>^<v<>><v>^<v<v^^^>^>^vv^<vv<<<>><>><^<v<<<v>>v>^>^>v<><><^v<>><>vvv>^><<^^^<vv<vv><>vv>v^>vv>v><><<^vv>^vvvv<<<<v<v^<>>v>v><v^><v<<v>>^v^^v>^v<<v^^>v>><v<<v<^v<v^^<<<v^^<<v^>^^^^^^<><^>v^><><v^<^^<>>v^<v^v^^^<v^>^^v>v<>^><v>^^><^>^>v>>^<>vv<v<^^v<^^>v^^<>^<^>>>^<^v<vvvv>^<v^>v<<^^^<v<>^v<<<>>^<<^vv>>vvv>v<<>><>^^><vv><<<^v>>><<<vv<v><<v>^v^vv<v>^>>v<<v>v>>><v>><^^v^v^v<<>^>v^>><v^>>v><<vvv^<^vv^v>>^^>v^v<<<>^>v^^v<<vv>v^>v<<^^<<>>v<<v<v^>>^><>^vv^><^>v<<v><<<v<^vvv^v^^v^>><v>vv<>^>v^<<v><><v<^v>v>vv^^v^^<<>>^<v><>v^>>>v<^<vvv<<v<>v>v<v>vvvv>^v>v>^^>v>^><v<^>v><<>><v^vvv<^^v>v^^^^>^<v<>>^>v^<^<>^^>>><v^v>>^><^v^vv>^<v>v<
v<^^vv><>><<^v^<^v^>^^<^>vv<<^vvvvvv^<><<vv>^<^v>>>><^v<<^<>><>><>>>><<^>>v>>^>^^>^><^<<v^v>v^v>^<^v^<>vv^v>><>vv>><>^<<v><v^v>v>>^^^<<^v><v<v^^>>^vv^>^^>^^v^<<<^>^>^><>v<<<v^>^^^>v<>^<v^v<>>><<<v<>^>v<^^<>^^v<^v>>^>><v<v>>^><^v<^<><>v>v>>>^<<><^^^<<<vvv<^>>^><^><v^<v<v><^v^v<<<><v<vv><<^v<v<<v^^<^<^^^>v^^>v><>^v^><^>>>v>><^v^v>v^<<>v^v<<^<<vv^^<v^^v<>^>^>^<>v>^v<>v>>v>vv^vv>^><><v<^<><<<>>><<>^>^<v<>>>^^<>>^>v^><^vv><^<^>>v>vv<^<v<><^v<^>>><^v<^><v><v^v^<<^><^<><^^<^v^^v>vv^^<v<<>^>>^^v^^<vv<<^vv<vv^<>vv>^>^<v^><><<><<><^v>^^v^><<<v<^<vvv>^><<>>><<v><>vv^^>>^^><<v><^<v>vv^^<^<^^^>^<v<>^v^>v^^v^<>v^<v^v<v><^>v^^><<<>^^^<<v^v<<<<>>v<v^^v^vv^vv^v>v>>^>>^vv^v^<<^vv^<v^v^<>^<^<v>v^<<v<<>^^>><v^>v^^>v^>>>v><<>><v^^^<><><v<<v<<^v>v^>><v<>^vv>^><v<^v>^<>v<<><>>v^v^>^>v>><^<^^><v><^>vv>v<vv^><^^v>^^>v^v<>v<v^^^<<><v>^^vv>v<^>vv^^v^v>>^vv^<><^<^<<<v<>><>>^>^^^^><^v<<<>v^<^^vv><^v>v^vvv><>v>^<<^^^v^^<>>v<^^v<^^^>>^vv<v^^<vvv<^<<^>v^<>^^^<^v^^<v>^><^>^^^v^^>^<>>^v^>vv<v>^<vv^^><^v^^^>v<^v<<>v<^<v
<^><vv^v^>>^<>>>v><^vv<v^<^vv<<>v^>v<v^^^^>vv^><<v>^^^v<v^<<v<v><^^v>^<v<<^>^^^>v>v<^^>v^v><<vvv^^^>vv^v>^<vvv<vv><<>>>v>v<vv<><<><^v>vv><<^^^vv<><^<<^>^><<>^<v>^>^v<<>>v^<^vvv<v^>>v<<^>^>v<<<^v<><><^^<>^<^<v><<vv<>>^<v^^><^^v<<><vv><^>^^>v^vv^^<>^vv>v^>v>^v>v>^>^>^>><>v<^v>><^<>^v<>vv<^v<^v^<>^<>^<^^v><v^<vv>v<^>>v>>v^v^<^vvv>><v<vvv><<^^<^v<^<vvvvvv<v^^^>^^vv^^v>>>>>^^>v^>^><^><>>^<>v^>v<<<^v><v<v^^vv^<^^v>^v^<vvvv^^<^<^<<<v^v^^<v<<v><^<v><vv<^^>v<vv<^<^v<^>^^^vv^<>^<v>^v^<><>><v>v^<<><^^^>>vv<v^^<v>>^<<>v<vv>^<<v<^<<vv^^<v<vvv>^vv<v^><vv<><v>>^^>v>^<>>^^<v<v<v^<vv>><<^><v<v^<<vv^^^<v><<^<v<<<v>^<vv^><<<^^v<^>vv<>>^>^v^<v>^^v>>v^>>v>vv><<v<<v>v^vv^>vvv^^v<>^>^v><vv>^><v>v^>^v^^><>v<^<v>^<<^vv>^v<<><vv>v^>vv<>>^>>>><<^v<v>^<><v<<<<>>^v>v><^v^^>^<<<v<v^^v^<>v><^>^>^^^v><<<^>v><^><<^vvv<vv^v>v^><<><^>^<<vv^>v><>v>v<>v<vv<>v<<^v>^>^v>^^v<>v>v<<v^v>>>vv>>v>>><^^^v^>>vvv^^vv><^v^<vv^><<^v<vvv<^^v<<vv<<v<><vvv<><<>v<v>^><<>><v<v<>^<v<>vv<<><<v^>^^^^^><<><^v^v<^>v<^^^><<<^<^v><^v<>^>>v^v^<^^
>vvv^<<>vv>vv<^^vvv>vvvv^<^>v^<vv^^v>^v<<^<<v<<vv>^v^v<<><v<><<>>><><v><<>v<<>>v<<<^>><v<v<>>>>vv>>>>^v<>^><v>>^><v<>^v^v<>^v<^v>^v^^v^^v<><^v<<>^<>><v><^<^<<<><^v^vv<<<<>>>^vv<<><<v^^vv<>vv^>v<^v^>vv<>vv<<v^<>^<<<>^><v<vv><>^v>vv^><<^^<v<<v><>^>>v><>^>vv^^>>^^<^>^^<^vv^^<>><v<<^><<v^^^<v^v<<>>>>^v^<v^>>^><<v^<v^^>>v<<<v>>>^<v^^>v^v<>^>>>>>^^^>v>v>>vv<v^^>>^v>v^^vv<<vvv<<>^^v<<>>>^<><<<>v<>>^v^><<>^>v<>^^^>v>vv<vv>^<^^v<^^>v<^^^^<<<v>><<vv<v>v^>>><v^v>v^^^v<<<v^><>><^<^<^>><>^^v>v>v>>v<>>>v^^><^v<^>><v><v^<^<^>^^^>>>v^<>^>^v^v<vvv<^^^<>><<v<<>><^v>v^v<>>vvv<vv<<><v<>^<<^vv<^vv><>v<^v><^<>>>^<v<vvv<^vv<^vv><^v^><<<v^^<<^v^v>^>v^^^^v<>^^^<<><<vv<<^>vvvv^vv>^<vv<^^<^>^<^^^>v>v^<<>^>^<<v><>^v^^^><<><>v><<<><>v^>v>^<<<>v^>^<<^vv>>>^vvv<>>vv<vvv^<v<>>>v^vvv^v>^>>v<v^>><v^<^<^<^v<vv>v>^><><><^v>>v<^^^v>^vvv^^>>^<^<^^><<>^^<v<<^>^>^>v><>v<<v><<>><^v<>v>^<>^v^>v>^<>^>^>v^<v^><<>><<>v<^v>^<<<<<<v><<>><>><>><^v^^^vv<v^v<vv>v>vv<v^^^v^><v^^v<>v><<>v>>><<v><^<><>^v<v<><<<><>>^<v^<v<v<v^v<v<><v^<>vv
<<<v^>v>>^>v>v<v<>^^><<^^><^^vvv>>>^>^><<^^<v<><v<<>^^^^vv<^<v^><<v>>><<<<<<<vv<<><v<<<>v<v<<^vv^<v>^^^^^^><^vvv<>v^>^^vv<vv><^>><v<>><>^<<vv^^<>^>^><v><v>v<^v<v<^^^^><^<^^><^v^^<vv^<><<^>^v<v^^v^^<>><<v<^^^<>vv<^^vv^><v><<v^v>>vv^><v<^^^v<<v<<<>vv>>><v<vv>^<^<v<v<>^>v><^>v>v<^<>v^^>>^^<>^<^<v>><<^<<^^^v<v<^<^<<v<v>>^<>><^v^v^<>vv>><v^^><v>><^<^>>^^<<v^<<<>v<^<v^v<v><<^v<vv<v<<>^v^v<<><v^><>><^v^vv^>>v^^v^^^<v><<<v>>^v^><^<v<<>>>^v>^^v<><vv<^^<>^^<<v<<v<<v^^^<^v^<<>vv><<<vv^^<^^vv<^v>^<v>^^^vv^<>v<<>^vv<<vv^^<>v<><^^<vv<<v^<<^<^vv>><^>><>><v^<<v><>^<<^vvv^>v^^>v>v^^^^^^^^v^^^v^<^^^v^^vv^>>v>v^^<v><><<^>v>><^>^v^><^^v>v^vv<v^>^>^<<^^^vvvv<<>><>v<>vv<vvv<<v^^v^^vv><<>^<^>^^^^^vv>^><^^^<<><>^^v^>^^>>v^^^<^<><>^<<>>v^<v<^v<>>>^<vv>^v^>^<<>^v<<v><^v^>><>^<><<v<>><v<>^>^vvv^^>v^>>v>>^>vvvvvv>>v>^vvvv>>^^^<<v>^^^<vvv<<v<v^v^^v<><<<v^v<><<vv<<<<vvv^^^<^>v^v^v^^>^v>^<>^v>>><^vv>vv<^^^vv<>^<><><>vv^v>v>v>>>^v^<^<>^<v<v<v><^<<>^^<^<>^v>>^v^>v^>v^>v<v^>^<>v^<^<^<vvv<v<vv^v<<>>^<^v<^^^<<<^>^^>^<<v>
^v<v^<^^>>^v><v<><^<><><>v^<>^><>v<<vvv<><>v<><<^^vv>>^^^><^^<>^>><<^^>v><v><^>^>^>><>v^<><><^^^v<^<v^<>v>vv>v>^<><<><^^<^^v<><^<<v^<<^>^^>>>^>>^^^^<^v><><<<^^<^v>v^<^v^><v>^^^><^>^vvv>^v<>v<v><<<^v>^<v<<>^^^<^>^^^<^<v<<>>>>v^>^v^>v^v<v<<^<^^<v^^>v<><^<><^>v^v><<v<v>^vv<^vv><v<v<^><>^v^<<^>vv<^^v<^vv<>>v>>^<>^>>^>>>>^v^<>><v^>vv^^>^v^>^<<<v>^><<>>>><<>^v<<>>>>>^>^^^>>><^>>v^vv^^v><vv>^v^vv^vvv^>^>v>v^vv>^v^^<vvv>vv>><<<<^<<<><>v^v^^^<>^v^<>><<^^^<>vv<<<v>v<<<^>><>^<><v<v>v<v<vv^vv<v^vv^^<<<<vv<>vv^vv<v<<v<v><><>^^><^>^<><^v^>>^<^>>>vv^><<><<^>><v<<v^v<>^v^^v^<><v>^v^^vvv<<v^v<<^^^^^<vvv<><^<>^v<<>><v^v^>>>v^^<^>v<><vv><<<<^<v<v<<<^>v<<<v^v<<^v>^^><<<v>vv<<>v<>v^v<^<>^>>><^v><>^^v><<>vv^v<^v><vvv<<vv<><^>>>v<v><<^^<v>^vv^^>^v<<^<>v^v<v><<>^vv><<<vv^v<>^<v^v<^v>^<<<>^>^vv^><>v^<>v<>>>^vv<vv^<^v^<v><>>v><vv<v>><^v^^^^>>v^>^>v^^<<^^v>vvvvv<>^vv^<^<>^<>v>>vv>v>v<>^><>v^^^vv^>v^<>^vvv<>>>v<<vv<<v>>v>><<^vvv^>v^<<v<v<<>^<><^v<<^>>>v^<^>v<<<<v>^^^^^v><>v>vv<>>^<v^^^v<>v<<>v^<>>v><^^^v^^^>^^>v>
<>^^<<vvvvv^>vv>>>^<>^v^vv<v^<^v>^^><^>><<^^vv>v<v><v^<^<^>><><<<>v^v>vv<v^v^v>><><v>>^<v^<><v<^^^v<v<<v<<^>^v<^^>^^^vv^><>>^<<<<v<^^<v^<<^^<v>>v^^vvvv^vv>v>>vv<^^>v^vv<>v<v<v<^<v>v^>v^>>^<v><<<<<^^<>>^v^<<v^><v><>vv<v>^^<^<><v<^v<^^vv^<><v>^<<^<>^^^^^>^vv>v>^>>vv>v<>v^^<><^^>^>><>^^v>v><v<^<<<^v<>^>^v^^v>v>>^>^vv><^>^>^<><^^v><v<^>v>vv^v>^v^>^>^v<v>>v>>v^<<v^>v^>v^>>v<^<<<><>^vv<>>v<^^^>v><<<><<<vvv<v<>v<^vv^v<v><^^vvv>^^vv^<>>v>^vv^^<^<>><<>v^v^^^^^<v>v^^<<^^<^v>>>^>^^^^v>^^v><^v^>^v>^^^<>^<<^v^v>v><^^v>^vvv<<>>^v^^>^>^v<v^>>>^v><v<>vv^v>v>v^v<^v>vv>>^>v^<^^^^>^<^>v^^>>^<>^^><v>vv<^>^^<^><<>>^>^v>>v>^<^v<<vvvv^vv<>>v<><^v^v>^v^^v^v<v><<^^v><^>^>^v<vv^^^^<^^v^v<v>^><<<v><<<>^v^>v>vv<^<><^^<>^<>>vv<v<<>^><^^^^v>v<>>v<<>vv^>^vv><<vvv><>v><^v^><vvv>vv<v^<>>^v^^<<<<>>><v<>>^^><^><v<^^<<<<^^^>vv^>^v<<v<vvvv<>^^v>^>v^^><<^<^v><v>^^^>v^<>>^>vv>><^^><^^^>^>><^<>>>>vv><><^<>>v<>v>^v^>^>^><v^^>v>>>^v^vv>v>><>v^^^>><v><>v<>v^^^vv<<vv<vv><><<^<<<>vv<vv>v>^^<v>>v^>>v><<v>^^<><>^>v^<>^vvv>^<^v<<vv<
v><^^>v>v>^<^<^<<v^<<v><^^<<<^^>><<<^>^^vv<^>vvv<>^^^<<>^vv^v>^^v>^v^^v^<>^vvvv^>vvv>^^<<v>v>^>vvv>><<<v>>v^><>>^<<v^<^^v>><<^^^^><v^<<^^>^^v>^vv^>vvv>v^v^vv^>>^<^<>>v<v^v><<^^^><^^vv^v>v>^>v<v>^><>^<>^>^>vvv>>^<^>^vv>^^<>^^>^><^>^<v<>>^vvv<vv^v>>><<<v^>^v^><^v^<v>vv<<<><<<vv^^vv>>v<v<>v<><^^vv<>>>^v^^<^<<>^<<^<vv^<v>>>v^<>^>>vv>>>^^v^v<vv<^v>v<<^v<^<v^v>v<v>^^><>v^v><<<<v<>>>v^vv<^>>^><v>^v>^<vv<<^>^>v^^<^^^^vv>><v^^v^>^>><^v<^v<>v^>v<<^<v<vv<<^<>vv<>^<v<>^^vv<^^^^<^>^^v>v>v>v<vv>v>v>vv^^<^^<vvvv>v^<^>vv>>>^^^>>>><^^<^<v>v^^v>>>>>v>^>>vv<v^>vv<<<><>v>vv>^><<>>v^<vv<v^v>^v^>>^v^<>^v<^v^<v<^v><^^>v<v<>>><>><^>>^v<>>><><<v>^>^<v><^<^<<v^>v>vv>>vvvv<^>^><>v^<>^><<v^^^^^v>^>v<v^v<>>>^^vv>v>><^^<>><<v>vv<<<>><^v><v>^^<vvv^^^^^<^v>^<<v>>^^vv><<<v<>v^<<><v<>><^<>v<<^v><vv>>^^^v>v><^^<v^><^<v>vv<v^^^^^>><>^^<<>^>>v^^>v^<><>^v<^v>>v^vv<>v<<^<v^v>>^>><v<^^vv<^^<^<v<><^vvvv^>v^<<<><<v>^^^><^><v>^<<^^vv^vv>v>v<^>>>>^v<^v>^v<<^>>>^<<^<v^^v<^<v^<v>^^^vv>^<>^<^<^><vv>>>^<>^^<<<<<v^^>>>vv<^^>>>v^<vv<^
>>^>^^>vvv<<^^vv^<^>v>^<^<^<^>v^<v>>v>>v>^^>^<<>>vv>>^>>>>>v^<v>><v<>^<vv<>>><v<^^^v<v^<v^>^>>>v>^v^v<^v<>^^v^^^>>>^>v<^>^<<><v<<<<v>v>^<^^^<<>^<v^>>^<<<^>>^>^^>^v^^><vv^<v<v^v^<^>^<v^vv>^><^^^><^v<<>v<^<^<v>^^>v>^v><>^<>v^v^<^<v><>vv<>vvvv<<<^v>v>v^^<<vv<<<<v>>v^^^v>>v><^^^><v<<^v^v>^<<>>><^^v>>^v>><><><<vvv<^^>^vv<^^v<>^vvv><<^^<v>>>^>vvvv^^vv<^v<v<><<vv><><>>>><><v>v^><^vvv>v<<>^^^v>><vv<v<^<v^^<<>><<^<><vv<>^><>>><^v>^<>>vv>><>^>^<>v>v<v>v^^>^^^>^><>><>v<<v<<<<v<<<^v<<<<<^>^v>^v<<<>v>><<><v<<^<>v^v^^v^^<^>>^^^^v^<<<v<>^^<^>>>>^^vvv<><^v<<^^>v>v>^v><v^<^>^^^^><<>^>^v<^v^><<<>^<^v<<v>^<^^^>^^^^^<^^<v<>vv>^<^<<vv<^^>v^vvv<^<vv<^><^^>^^v<^v<><><>>v><v^<><^vvv^v^vv^^<^<^<<><^<^<>>^<<<^^>v><<v^>^v<>>>>^v<^>^^^^v>>^v<^>>v><^^^<<^<<v^>vv>v<^^vvv^v>><<>^><<^v<v><v<><vvvv^>v>>v<^>^>>^<^v^>^v^v<<^<^>^vvv^>>v>^>v^vv>>><<<vvv<v>^><^>vvv<^v<v<<v<v^v^>>^vv^><v>^v>v>v^v<^<v>^vv>v<v>v>>>^^<vvv>>><<>^<>>^<v>>^^^<^^v^v><>>>v^^^vv>>^<^v^>>^v>>^<>vv^vv>^^><v>v><>^><<>^<>^^^<><^><v<<<<>>>v<<<v^^^v^^v>^<
>^^<<>v^><v>>^v^^<v<^<>^>^v<><>^><<>^^>>^^>><>>vv<^v<^<>^^v^v^v^^<>v<<><^vv^>vvv<vvv<v>v^v^<<vv<v><^^>>v<v>v>^vv>^^^v<v<>><v^>>v<^<v>v^v>vv><>v<>>><v^^<v<<v>><^>>><v>>v^>^v>v^^v<>vv^><^v^>^^^vv<v^>v<v>^^v^>>^v<>>><v<^>>v^<<^>>>^<^>>vvv><>^<v<v<^>^^<^<>>^^v><>>><>vvv>^<<v>><>>^>><^<v><^><>^^^<^v><^^<<<<^<<^v<><vv^><^^^>^<^<<><vv^>v^<^>><>>^><^<>^>v><>>v>>>vv>^vv^>^^><v^^v^<<>v^^^vv>v>v^>>v^<<<^vvv><><><vv<><>^v>v^<>>>>^>><v<^^^vv^^<>v>v<^v<<v^<^vvv<<><<^v>vvv^^v^^><^<^^<<v^^<<^<^<<<>v<v<><>v^>vvv^<^^^v^v^v^<><v>vv>>v>vvvv^>>^v<^>>^v^^^^><^<v<^^<><^^<<<><>vv<<>^^vvv><vv^v<v<>vv<<>v<v<v^v>v>><^v<<^>^>>^v^<^vv><^>v<^v><v>^^v>><^>^>^^vv^>^v^^^v<v<<<<<v^>v><>><^v^vv>>^>><^><>v<<>v<<<v>v^^<<^>v<^><^^^><<^<vv<vv<<>^>vv>v><^><<^<>>v><<<^v^^<<<vv<>^><<>v^v>vv<<v^v>>v<<v^^vvv^<>><^v^<v<^^^^>>>>vvv>v^>v>^v>v><^^^<v^^>>>v<v>^>^^>v>vv<>>v^^v^>vv><<>v^>^^v<<>vv^^^><<^<>v<vvvvv^^^>^vv><<v<^>v><><><<v^>^>^v<vvv>v><v>><<>><<^<^<v>>v<v<^<><<v^>>>^>><^^^>^^<><v>^^<^<<<v<^<v>v>>v<v>>^^v^>v>>^v>^^>><<>v^><>
^<v^>^>v<<^^<<<vvvv<^v<v^^^><vvvv^^<>^>v>vv<v>^<<><><^^^v^<^>^>>^^<^>v>vv><^^>vv<>^v<v>^v<^v>^>><<>^<v><v^>v<>^^vv>>^vv>^v^^v^^^>>>^<<>v><><<^<><^^^vv<v>v^>>^><>^^^<<^^v<^vv<<>>>^v<>v>v^<v<>^v>vvvv><<<^v>^>v<vvv<>>>^<>^<v^>^<<^v>^><^<^<vvv>^^>v<v<v<>^vv>^>>>^v^<>^<vv<>v>v^><v<^^<><v<>><vvvv^<<^<^<^v<^<^>^v<><^<^<>^<v<v^<^><v^>^v^vv>>^<>v^<>^<v>v>>v>><>v<>>^<v>>v<vv<v<v><>^<>^^>^vv^v^<v>>^^^v^>vv^^>^^^<<^vv>^<v>vv<^v>^v<^><>>^v<v<>v<v>^v^<v>v>>v^v^>>^^^>^v<^v>^^v>><^v^<>^<v<<v^^v^^><^^v<><<>^v>^>vv>^<>><v>><<<>v>^v^>v>^><<>v<v^^v><^v>^^<^>^^v<vv><vv><><^<>^><^<>>^^<<>^v^^>^>^v<^^><v><^^^<<^><<v^<^v<<v>vvvv>^^v<v^v<<>v<<>^v>>vv>>v><>^^<v>v>v>>^^>^<vv<^v>^>v<<^>^vv<<<v<vv<^>v>v>^^<v<vv>^><^>^v><v<<^v^v^>^<<^^v<<v>^v^>>><^>>^<^v<^v^>^v<>v<^v^<^^><><<^^vvv<^><^^<v>v><v>>v<^>vv^v><^^^v^<>>vvv^v<^<<>v><><v^>^><<>^<v<<v^<v^^<^<><^vvv>^^>v^vv^>vv<v<<>^><<<<v>>v^<>>v^>^><vv^v^<^><^vv<^>>vvv><v^>v^<><^>^^v<^>^>^^<<^<<>><^v^>>><^v<v^^^^v<><>>^v^^v<<v<^<vv>>>v^>^v<<<>^v<<><v>>v<<<vvv>v>><^>><vvvv^^
>^^v<v^<v^<<v<v>^<<<^^><<>v^<^^<>v>^>vv>v>v^>^v^>v<>v<vvv^v>>v>vv<v>vv^>^><^^vvv<v<<><>^<<>>^^^v>>vv^vvv^<<v^v<v<^<<<<<<v>>>>^^^>>>>>>^v^><<v^<v<>^<v<v>>>^><<<v><^^<>>v^<^>^<>v^<^>^>^v^><^<^vvv>v<^v<>vv^^^>v<v>vvv<^<v<v^<<<>^<v<<^^<>^^>v^<vvv^<v^v>><<v>>^v>v>vv<><>>v<^v^><<v<v<^v<v<<><^<^>^<v<>>vv>v>^>v>^<v^v<^<^<<>vv<v^v^^v<>^^><>^<>vvv>>^^^>v>vvv<<><^v>>>^v^<v<><^^^vv>^^v>v>>v><v<^^^>v<<>^><^v<v<v^vv<><>v><<<<^v^>>^v>vv<>v^<vv^v^<^^>vv><^v^^<v<><v^<><^<<>v<<><<>>>^><<<v>^<^<v>v^^<<>>>><<<<<^>^v^v^>>><><>>>>>vv<<>^<v>v^vv><<^^<><^^<^^><<vv^<^v^^vv>>>>v>vv><>v>vv>v>vvv^<v<<^v<>v<<v><<v><><^^^^^>^^>><^v<^^<vv<<<<^v><<^v^<>>^^v<v^vv<><<vv<v<^<v<<><v^v>v><>><>v<^<v<>>>^><>>^^v>>>v>v<<><^<<vv^^><v<v>>vv><<>><<^>v^^v^>>>^v^<>vv<vv<vv<^^><<vvv^>^><^^v>^><>^<<<v^>^<v<<vv><v<^v<<v<>>><<><><<<vv>>v>>><>^v<<<^<^<^^^<<vvv^^>v<v^v<<^<><<v<^>><v<<v<^^v^v<>><<<>>^^^<v>>^<v<>^^>v^^^^<>vvv^<^<<<^^^>^<>vv^<>^^^^^<v^v>><<^<^^<^^vvv>v><<>>v^<<<>^^^><v>^>>v>^^><v<>^v>v<^^>v<^<>^^^<>^<>>v>^v><>v^<^>^>vv<v^
><<^v<>v^v>v>^^>v^v<<^<<v^^>v<v<^>>^<v<^<>><vv>><<<^^v><v<><^>^<<>^>v^v>>>v<v>>v>^v>>v>v^<^<>^vv^><v<^v<v^<^v^<>v^v^v^>>^><><<v>^^<><^<v^>>^<>^<v<<<>>>><<>>v^<^<^<v>^><^v^v^<<^>>^^<v>^^<>v^v><>><<v<v<>^>><>>vvv<v>^<<v>^^<>^v<<^<<^^vv<^v<^>^<>><^v>>vv>v<<>><<>>^><vv^><>v<v^v^^v^>>^v^v>^^<^^<^^^<<vvv><>^^^<^<<<<vv<><v><^vv<>vv>^^>>^<^^v^>^vvv^^<v>^><>>^<<>>>><><v<^<>^>v>^<>v^v<<v>>^^v<^><^<^v><<>>>><><v^<><>>^<vv>>><vv>v<vvv>v^<^vvvvv^v>><<<v^>^>v<<<>^v^^vv<>^vv>^<v><^><><^>vvvvvv>v<^<>>v<><v^><^<>vv>>^^v>>vv<v^>v^v>^^><^^>><<<>>><v>>^v>v><v<^<>>^<^vv><^v<<v<^<^<vv><vv<>^^^>^>>>v>^>v<<><^^<<>>>^>><<v<v<<<^^>v><^>v^<<v^<>><<^<^<>>v^vvv<^^v><^<^v<>^v>v^><>vv<v<v<^v>^^>vv^^>^<v><^<^<><v<v><>>>v^>><<<^<^>vv<^^^>><<<v>^>v<>v^^>vvvv^<<<<>v<><v^>>^>>v^^^<v><vv>v<>>vv<^<^><v<^^<v>v<<v><^>vv>^v^>v>v<^<<><>>^v<<>v>^v^>^<v><<>v>^^<><><v><>>v<<v^<v<^><>^vv<><>v^<vv^^^>v<<vv>>>>>v^<>>^><>>v<<>v<vv^v><>vv<<vv^v<>>^^<v<^v<v>vv>^>>v>vv^v>v<>><>>v^v>>^>v<v^>>>^<v<^^>>v<<<vv<<>v><<><^v<>>vvvvv^v><<>^v<v>^
v>^>v<^v>v><^>vvvv<<v<>^^<<>vvvvvv<v<>^>>><v><v^<<^>^v<>v^>^<<v<><vv>^v^>>^<<v<v^>^>v<><v>^>^^v<^>v<>^><v^>v<v>v^^>^^<>^<<^<<<v>>v^<^>^>><v>>^>>v^<^vv^^^vv>v>v<v>v^>v>^><<^<><<<<>v<vvvvvv<><v>^<>^>>vv<<^vv>^>^^>^v>vvv^vv>>v<^^>^^>v^<<vv^>>vvv^vv>vv><>v^v<^><<>^^vv<<^vv><>^<>>^^^vv^v^>^>^<<vv>><^>>v^vv>^><v<<vv^v>>v<^<>v<v><v<><^^vv^^<^<v^v>>^<vv^<<v^<v^^^><<^>^<<^^^>>vv>^>><><^v^>vv<>^<vv>>v>^<<>><<v>^>>vv<>^>>>v<vv<v^>>>>^v^v^>v^<^v<<>v<<<v<^<>v><<^v^<<v^<vv<^v<><^<^>v^<v>^vv>>v<v><<<^v<v<v^^>>^>v^v^>><<>>vv>>>>v^v<<v^v>^>v<vv<v<<>v><<^<<>vv>^<^>v<vv^^>^^>^<^v<>^<^<v<v^^v<^>>^<><^<<>^>^v^v><<>vv^v<v><>^^v>>^v><<v^^^>^v<><^<^^^^<>><<^^<<<^<^<^v<>^<^<v>vv>><<vv^>vv<>>><^^><^vv>>^v^<<>>>v^^^<>>^^>>vv^<vv^>v>>v<>v><><v>vv>v<<v^<><<<v^v><v^^v<<vvv>^^<^v<>^><v>>>^^v^<^<>^^v<^<>>>><v^>^^^>^v>><v>>v>^>^v>><>v<v<v<>v<^^><<><>^v<<<><>vv><>v><<<>>>>v><<^<^^>v<v^v<<v<^>><vv>^>v<v^v<<^v^^>v^<v^vv^vv><^<v<^v<^<>v<v^>v>^>^>v><^v^<><<v>>^v^><><<>^>^^>^<v^>v>^^vv>>v<v>^<v<v^v^>^>v^v<vv<v^^vv<<v<<^>v>^
^<<>>>v^^vv<>^<>v>^v>>^vvv<><v^^^<<^^v<^v<^><<<><v>^<v^<^^<^v>^>vv^v^vv^>>vvv<vvv<^><>><><^<v<^^><^^v^v^><vv><<^vv<^v<v<^v<^v<<v>^^<<><>v<>>>^v^v<>>v><<<<>><vvv<^<<>>>^v^<<<^v^>>vv^v<^<<>^^v>>^^^^<^>v<^v^<><v^<<<^v^v^v>^>^>vv><<^vv>><>vv><v<>^v>^>>vv<^^<>v^^<^v^<^v^^>v>>^<v<<>>>v>><v>^^v^>^<>><<>>v>v^>>><>vvv><>>>v>^<<^v<^v<^<>^v<^>>^<^^><^^v<^<^<>vv<<v<^^v^<<<>v<><>vv^v>^>v^<v>^^>v<<v^>>>>v<^<<v<>vv<v<^^>>v<^v^^^>^<><>^v<<^><<v>^<v^v^<^>^>vv<v^^^^v^^^v^<>><^>>v<^v>v<>>>^<^<^<v^>>^<<<v<<v^^<>^<v>>v>^<^^v<v>^>^vv>v^>v>>vv<<><v>^v>^v<<<<>^<<<<>v<vvv>>>>><<vv><>v<v^<><^v<>v^^<v^>^^<<><^><<^v<<^>^<v^<^v<^vvv<^^<v<>v^v<><<<v<>>><v<<v^><<^^>^<>>>v^<>>v>><>v><v^><^<>>v^<>v^<^>v^<^<<>v<<<vv>^>>v^<v^>^>v^^<<^>>^<^^>><v>><v<<v<<>^^^vv>vv<<>^<v^><v<>^v>^^^^>v>^^<<^<^<^<<v><vv^^^v^<>v>>vv^><<>^^^<^>>>vv<>>v>^<>^^^v<^vvvvvv^<^^>><^<^v^vv<<v<<<>^vv><>>^v<v^^><<v><v^>^v^v<^v>>v^v><^>vvv<<^^<v>^^<<v^v>><<<>v<^>>^v<v^<^vv^v>v>v<v<vv^^<^<>>vv<v<v^<>v>^>v><^^^^<>^>>v<>>^<v><^vvvv>vvv^>^v^<<v>^>>^<<^>vv<>
vvvv^v^^^<<^>^^vv<<^>v>^v>^>^>^^^^^^>v>>vv^>>^^>^vv<vv^<v<<<^<^<<<<^<<v^^^v^<<><<>^>^>v^<vv<vv>^>>^^v<v<v>^^v^^^^v^<<>^<>v<>>^><><v>^<vv><v^<vv<v^>>^v^^vv^>^v><<^><^^vvv>^^><>>^v>^^>v><>>^<>><^<^>vvv<>v^<><><^v>><^>^>^^^v>><>^>><>^<vv<v>^<v><>^>^vv<vv^^^<^<v^^v>>^>><v^^<>vv>v^vv<vv<v<<<^v>^<v>v^<<^<>vvv^v<<v<<vv>>vv<v<v<>v^>>><><v><^v<<^><vv<^^>^vv>>v<>vv>v^vv>^<^v<<><<^>^>vv<v^<v<<><>^>^><v^^<<>^^><>v<><^^^><v><vv<^^vv><v<^<v<^vv^<<^>vv>^>>>v^v>v^>^>v^vv>>><v<v<<v^>>v^^^<>^>^>v>>^^^>>>><><^<>>^vvvv<vvv^^vvv^<vv>>>>^v^>vvv<vv>^><^><v><<v<^v><v^<v<<>>><<v<v<<^>^v^<v^^<>^v^<^^>><v^>^vv>^v<<v>>v>v<v^vv><<><<^><^<<>^<>>>^vv^^^>v<^^^v>^v<>v^^><vv<<^^>^^^v>v>v><<^^<>><><<<^><>v<^<<>><v<<vvv<<vvv^>v^vv<vv<>^^^<^<^><<vv>v^>>v<<v<v>>v<<v^<><v^^>^^<>^v<><vv^<^v<<<>^<<^^v>v<^vvvvv>v^<^><v<><<<^<v<<<v<vv<^^>^<v<v^>^>v^^v>>^vv^>v<<<v><>^v><v>v<>v>^v^v^<^>^>^^v>><v^v<v>><<>^^^^^<vv^v^^<^>>>v<<vv^><v^v^^>><>^>v^>v>^>v^>vv><v<^<^>^>^v^>v<>><<<>^v>>vv^v<<^v>>><<><<<>^<vvvv<v<^<<>vv<vv<v<><vv><<^^vv>^><
<^^^<v><^<vv^^v^><><^v<^>v^<v<>^v^v>^^v>>v^^>^v<<<vv<^v^><vvv><^vvv>>><>><^>><>>v<>v<<<^^<>^^^^>>^<^v^^<v<><<<vv>v^^^>>^<><^<>>v>v^>^^>>^v^>^^^^>v<^><>^<>>v<^v^<<>v^v^<>^<<<>v>^>>v^^v>v^v>^>v^^>>>v<^^v^^>>v^>><^^<^<<vv>>v^<vv<<v<^^^v<<v<v<v<>^v><^>v^<^vv<>>^v<v>^>v>^>^>><vv<<><<vv^v>>^^v><^<^^<<^vv><vv><<^v<^^^^>>^><v<^v>>v>>^>^<><^vvv^^<v^^><^><^^v^<v<<^v<><^><><<^v<v<^<v>^>v<>vv>^^^vv^^^^^<>v<<>vv<>^vv<^<^>^^>^^<^v<<<>^<v^<v<>vv^<v>^v><^>^v^<<<^<>v<<^<vv^v<^v<v>>v^^v^^v^v><<v<vvv<^<<^vvv^^v>v<<v^>vv><<^<^<^>^>^<>><>v<><>><^^><<<v<>><v>^<<<<^<<^^^^v>><^^v<v><v^v<^v^v>^>>>>v<>v<v^v<vv>^^<v^^^<v^v^<<^>v^><>>>v<>^v>v^^>><>v>^v^<^^v^v^^^v>^><<^v^vv<>>>^<<<>^^<>^^^vv^<v^>v<<<v>v<>>><v^><<^>v^^^v>^<v<^<>^^>vv^>>><><<^<v^^vv^>v><vv^^v<^^><<v>v^>>v<v^^^<vvv^^<<<^><<^>><>^^v<^^v<^^>^<<>^vv^v^^<><>v>v^^^<^^<v>><>v^^vv>>^vv^^>><>v^vv>vvvv^^vv^><v^^^>vv>^vv<v^^^^^v>^^><v^<^vv<>>>v<>>>^^>><<>v<^vv<<><v><>v><v^<<<<><>^^vv^^<^v<^>>>>vv<<^<>v<^<><^v^<<v<<>^<<<>^>><^v<vv>v>><^^>>^>^<>^^>>v<>^<<^v<><v^
^<>vv<vv^^>^<^<vv><>>^<^^>^>^<^^v^>><>v^>v>v>vv><^>^>^>><<>^><vv>vvvvvv<<v>^^<<<><<^v<<^^^<>v<<<<vv^^v<><>^v^^v^>^^><vv><^vvv^^<^v^><>v>v<>v<<v^>>^v^>^^^^>>^v<vv>>><>^<^vv^^<v^vv^^^>^>^v^>>^^>>v><>><v^<>>vv^>^>v>v^<>v<<^<<^>v<<v<>v>vv^>^>v^<v<>^<>^v<>><vv<>><<>vv^^>^>^^v^^>v>^<<^<><v>>^<>v><>^>>v^><^^v<vv^v<v^>v^^<v^>v><>v^^><<><<><>^^<^<>vvv>v>v<>v>^<<>>^v<^><<<vv^>^<<<>v<^v>><^^>>>^<^<>v^^^>>>>v^>^<><^<<^><^^^<>^^>^^^v><^^<^v<>><<>^v<><^<<^^>><<><<^>^<^^>^>^<<>>vv<<<>v<vv>^<>v^>><>v>^^^>^><<^^^>>^^v^^<<><^^vv<>v^<<v>v>^vv>>vv<v<v<v<>v^^<>><^<<v<><>^v>^>v>^^vv<>^v^^>>^<>^<<^><^^^v>^v><v^^<>v^^<^v<<<><><<vv<>^>vv>>^>^<>^>v<<v<<><>><^vvv>>><v^^<^vvvv^v<^><><<>v><><<>v><^^^v><^<^vv>>><^^<^v><^<^^<v><^^<v^vvv<vv>v<<>^^^v><<><<vv<^<<^v<v<v><>v^>^<<<<v^v>>>vv>v^^^<>>>^<v>v<v>^^>><v<>^vv><><<<>v><^><v<v<<<vv><<vv^<<>^v^v<<^<<>>^>^^vv^>>>v>^><^vv><v<vv>^>><<^>>>^>>^>^>>v^^v>^<v><v^<<<^v<^<<^<>v^<<^<<v<><><v>^^v^^v<<^>v^v^>v>v>v>><>><<v<v<<><^>v^<<<^>^^<<<>^v>><v>v<vv<><^><<^<v>^v<<v<^>^v^^>vv"""

moves = moves.replace('\n', '')

g = map.split('\n')
for i, row in enumerate(g):
    new_row = ''
    for ch in row:
        if ch == '#':
            new_row += '##'
        if ch == '.':
            new_row += '..'
        if ch == 'O':
            new_row += '[]'
        if ch == '@':
            new_row += '@.'
    g[i] = list(new_row)

def find_pos():
    for i, row in enumerate(g):
        if '@' in row:
            return i, row.index('@')

x, y = find_pos()

dir = {'<': (0, -1),
       '>': (0, 1),
       '^': (-1, 0),
       'v': (1, 0)}

def show_grid():
    return
    print(move)
    for row in g:
        print(''.join(row))
    print()

def push_possible(x, y, move):
    dx, dy = dir[move]
    if g[x + dx][y + dy] == '.':
        return True
    if g[x + dx][y + dy] == '#':
        return False
    if g[x + dx][y + dy] == '[':
        if move in '<>':
            return push_possible(x + dx, y + dy, move)
        else:
            return push_possible(x + dx, y + dy, move) and push_possible(x + dx, y + 1 + dy, move)
    if g[x + dx][y + dy] == ']':
        if move in '<>':
            return push_possible(x + dx, y + dy, move)
        else:
            return push_possible(x + dx, y + dy, move) and push_possible(x + dx, y - 1 + dy, move)
    assert False

def push(x, y, move):
    dx, dy = dir[move]
    if g[x + dx][y + dy] == '.':
        g[x][y], g[x + dx][y + dy] = g[x + dx][y + dy], g[x][y]
        return
    if g[x + dx][y + dy] == '[':
        if move in '<>':
            push(x + dx, y + dy, move)
            g[x][y], g[x + dx][y + dy] = g[x + dx][y + dy], g[x][y]
            return
        else:
            push(x + dx, y + dy, move)
            push(x + dx, y + 1 + dy, move)
            g[x][y], g[x + dx][y + dy] = g[x + dx][y + dy], g[x][y]
            return
    if g[x + dx][y + dy] == ']':
        if move in '<>':
            push(x + dx, y + dy, move)
            g[x][y], g[x + dx][y + dy] = g[x + dx][y + dy], g[x][y]
            return
        else:
            push(x + dx, y + dy, move)
            push(x + dx, y - 1 + dy, move)
            g[x][y], g[x + dx][y + dy] = g[x + dx][y + dy], g[x][y]
            return


for move in moves:
    show_grid()
    assert g[x][y] == '@'
    dx, dy = dir[move]
    can_push = push_possible(x, y, move)
    print(f'{can_push=}')
    if can_push:
        push(x, y, move)
        x += dx
        y += dy
    # ahead = list()
    # i, j = x, y
    # while True:
    #     i += di
    #     j += dj
    #     if g[i][j] == '#':
    #         break
    #     ahead.append(g[i][j])
    # if not '.' in ahead:
    #     continue
    # k = ahead.index('.') + 1
    # i, j = x, y
    # while k > 1:
    #     g[i + di * k][j + dj * k] = ahead[k - 2]
    #     k -= 1
    # g[i + di][j + dj] = '@'
    # g[i][j] = '.'
    # x += di
    # y += dj
show_grid()

n = len(g)
assert len(g[0]) == 2 * n

r = 0
for i, j in product(range(n), range(2 * n)):
    if g[i][j] == '[':
        r += 100 * i + j

print(r)
