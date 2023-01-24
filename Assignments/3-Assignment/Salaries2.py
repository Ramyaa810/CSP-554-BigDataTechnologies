from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (name,jobTitle,agencyID,agency,hireDate,annualSalary,grossPay) = line.split('\t')
        actualAnnualSalary = float(annualSalary)
        if actualAnnualSalary >= 100000:
            yield 'High', 1
        if actualAnnualSalary >= 50000:
            yield 'Medium', 1
        if actualAnnualSalary >= 0:
            yield 'Low', 1        

    def combiner(self, jobTitle, counts):
        yield jobTitle, sum(counts)

    def reducer(self, jobTitle, counts):
        yield jobTitle, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


