from pytest_mock import mocker

from sudoku.solver import Solver
from sudoku.strategies import RowStrategy, ColumnStrategy, SectionStrategy
from sudoku.sudoku import Grid


class TestSolver:
    def test_it_calls_all_the_strategies(self, mocker):
        mocker.patch('sudoku.strategies.RowStrategy.execute')
        mocker.patch('sudoku.strategies.ColumnStrategy.execute')
        mocker.patch('sudoku.strategies.SectionStrategy.execute')
        grid = Grid([[1, 2, 3, 4], [None, 3, 4, 1], [3, 4, None, 2], [4, 1, 2, 3]])
        solver = Solver(grid)
        solver.solve()
        RowStrategy.execute.assert_called()
        ColumnStrategy.execute.assert_called()
        SectionStrategy.execute.assert_called()

    def test_it_can_solve_a_sudoku(self):
        grid = Grid([
            [7, 2, None, None, 5, 4, 3, None, None],
            [None, None, 9, None, None, None, None, 5, None],
            [None, 5, None, 1, 7, None, 2, None, 8],
            [None, 6, 2, 4, None, None, 8, None, 9],
            [None, None, None, 7, None, 9, 4, None, None],
            [None, 9, None, None, None, 5, 6, None, 3],
            [None, 7, None, 8, None, 2, None, None, None],
            [2, 4, None, None, None, 6, 9, 8, None],
            [1, 8, None, 3, None, None, 5, None, None]
        ])

        solver = Solver(grid)
        solver.solve()

        assert grid == Grid([
            [7, 2, 8, 9, 5, 4, 3, 6, 1],
            [3, 1, 9, 6, 2, 8, 7, 5, 4],
            [6, 5, 4, 1, 7, 3, 2, 9, 8],
            [5, 6, 2, 4, 3, 1, 8, 7, 9],
            [8, 3, 1, 7, 6, 9, 4, 2, 5],
            [4, 9, 7, 2, 8, 5, 6, 1, 3],
            [9, 7, 5, 8, 4, 2, 1, 3, 6],
            [2, 4, 3, 5, 1, 6, 9, 8, 7],
            [1, 8, 6, 3, 9, 7, 5, 4, 2]
        ])

