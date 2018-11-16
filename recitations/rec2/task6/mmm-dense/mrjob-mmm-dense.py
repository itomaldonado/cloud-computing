from mrjob.job import MRJob
from mrjob.step import MRStep


class MatMult(MRJob):

    def map_1(self, _, line):
        matrix, a, b, v = line.split()

        v = float(v)
        if matrix == 'A':
            i = int(a)
            j = int(b)
            yield j, (matrix, i, v)
        elif matrix == 'B':
            j = int(a)
            k = int(b)
            yield j, (matrix, k, v)

    def reduce_1(self, j, values):
        values_from_A = []
        values_from_B = []
        for v in values:
            if v[0] == 'A':
                values_from_A.append(v)
            elif v[0] == 'B':
                values_from_B.append(v)

        for (m, i, val_1) in values_from_A:
            for (m, k, val_2) in values_from_B:
                yield (i, k), val_1*val_2

    def map_2(self, k, v):
        yield k, v

    def reduce_2(self, k, values):
        yield k, sum(values)

    def steps(self):
        return [MRStep(mapper=self.map_1, reducer=self.reduce_1),
                MRStep(mapper=self.map_2, reducer=self.reduce_2)]


if __name__ == '__main__':
    MatMult.run()
