from sudoku.strategies import RowStrategy, ColumnStrategy, SectionStrategy
from sudoku.sudoku import Grid


class TestRowStrategy:
    def test_it_excludes_cells_from_the_row(self):
        class Grid:
            def get_row(self, row):
                return [1, 3, 7]

        grid = Grid()
        strategy = RowStrategy(grid=grid, row=1)

        assert strategy.solve(range(1, 10)) == [2, 4, 5, 6, 8, 9]


class TestColumnStrategy:
    def test_it_excludes_cells_from_the_column(self):
        class Grid:
            def get_col(self, col):
                return [5, 6, 7]

        grid = Grid()
        strategy = ColumnStrategy(grid=grid, col=2)

        assert strategy.solve(range(1, 10)) == [1, 2, 3, 4, 8, 9]


class TestSectionStrategy:
    def test_it_excludes_cells_from_the_section(self):
        class Grid:
            def get_section(self, row, column):
                return [[1, None, None], [None, 3, 5], [6, 7, 8]]

        grid = Grid()
        strategy = SectionStrategy(grid=grid, row=1, col=2)

        result = strategy.solve(range(1, 10))
        result.sort()

        assert result == [2, 4, 9]